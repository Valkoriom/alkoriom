"""Mesure la qualité de production des 5 dernières vidéos de chaque chaîne concurrente.

Usage interne uniquement (analyse). Rien n'est republié : les vidéos basse résolution
sont supprimées après mesure, seules quelques captures et les chiffres sont gardés.

Prérequis : pip install yt-dlp "scenedetect[opencv-headless]" ; ffmpeg dans le PATH.
Lancement  : python3 outils/analyse_style.py            (5 vidéos par chaîne)
             python3 outils/analyse_style.py --n 3 --chaines @theAIsearch
Sorties    : resultats/style_videos.csv, resultats/moyennes.md, captures/<chaine>/*.jpg
"""
import argparse
import bisect
import csv
import json
import pathlib
import re
import shutil
import statistics
import subprocess

import cv2
import yt_dlp
from scenedetect import ContentDetector, detect

CHAINES = {
    "@SamouraiDansant": "fr",
    "@VisionIA-FR": "fr",
    "@AILABS-393": "en",
    "@theAIsearch": "en",
}
CTA = {
    "abonnement": r"abonne|subscribe",
    "like": r"\blike[zs]?\b|pouce|thumbs? up",
    "cloche": r"cloche|notification bell",
    "sponsor": r"sponsor|partenaire de (cette|la) vid|thanks to .{0,30} for sponsoring",
    "lien_description": r"description|lien (en|dans)|link (in|below)",
}
SOMMAIRE = r"au programme|on va voir|aujourd'hui on|sommaire|in this video|today we|here's what"
RACINE = pathlib.Path(__file__).resolve().parent.parent
TMP = RACINE / "tmp_videos"
CAPTURES = RACINE / "captures"
RESULTATS = RACINE / "resultats"


def dernieres_videos(handle, n):
    opts = {"extract_flat": True, "playlistend": n, "quiet": True}
    with yt_dlp.YoutubeDL(opts) as ydl:
        info = ydl.extract_info(f"https://www.youtube.com/{handle}/videos", download=False)
    return [e["id"] for e in info["entries"]][:n]


def telecharger(video_id, langue):
    """Métadonnées + sous-titres auto (json3) + vidéo ≤240p avec audio léger."""
    TMP.mkdir(exist_ok=True)
    opts = {
        "quiet": True,
        "outtmpl": str(TMP / "%(id)s.%(ext)s"),
        "format": "worstvideo[height>=144][height<=240]+worstaudio/worst[height<=360]",
        "merge_output_format": "mp4",
        "writeautomaticsub": True,
        "writesubtitles": True,
        "subtitleslangs": [langue, f"{langue}-orig"],
        "subtitlesformat": "json3",
    }
    with yt_dlp.YoutubeDL(opts) as ydl:
        info = ydl.extract_info(f"https://www.youtube.com/watch?v={video_id}", download=True)
    return info


def lire_sous_titres(video_id):
    """Renvoie [(début_s, fin_s, texte)] depuis le json3 YouTube."""
    fichiers = sorted(TMP.glob(f"{video_id}*.json3"))
    if not fichiers:
        return []
    data = json.loads(fichiers[0].read_text(encoding="utf-8"))
    cues = []
    for ev in data.get("events", []):
        texte = "".join(s.get("utf8", "") for s in ev.get("segs", []) or []).strip()
        if texte:
            debut = ev["tStartMs"] / 1000
            cues.append((debut, debut + ev.get("dDurationMs", 0) / 1000, texte))
    return cues


def debit(cues):
    mots = sum(len(re.findall(r"[\w'’-]+", t)) for _, _, t in cues)
    if not cues:
        return 0, 0.0
    duree_parole = max(cues[-1][1] - cues[0][0], 1)
    return mots, mots / (duree_parole / 60)


def positions(cues, motif, duree):
    """Positions (en % de la durée) des phrases qui matchent le motif."""
    return [round(100 * d / duree) for d, _, t in cues if re.search(motif, t, re.I)]


def coupes(video):
    scenes = detect(str(video), ContentDetector(threshold=27.0))
    return [(s.get_seconds(), e.get_seconds()) for s, e in scenes]


def part_visage(video, scenes):
    """Part des plans où un visage de face est détecté sur l'image du milieu (proxy « face caméra »)."""
    cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    cap = cv2.VideoCapture(str(video))
    avec_visage, total = 0.0, 0.0
    for debut, fin in scenes:
        cap.set(cv2.CAP_PROP_POS_MSEC, 1000 * (debut + fin) / 2)
        ok, img = cap.read()
        if not ok:
            continue
        gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        visages = cascade.detectMultiScale(gris, 1.1, 5, minSize=(img.shape[0] // 8,) * 2)
        total += fin - debut
        if len(visages):
            avec_visage += fin - debut
    cap.release()
    return 100 * avec_visage / total if total else 0.0


def dans_intervalles(intervalles):
    """Test rapide « t est-il dans un des intervalles triés ? » (bisect)."""
    debuts = [d for d, _ in intervalles]

    def test(t):
        i = bisect.bisect_right(debuts, t) - 1
        return i >= 0 and t <= intervalles[i][1]
    return test


def niveau_musique(video, cues):
    """Volume moyen (dB) pendant la parole vs dans les silences ≥1,5 s : proxy du niveau de la musique."""
    sortie = subprocess.run(
        ["ffmpeg", "-i", str(video), "-af", "astats=metadata=1:reset=1,"
         "ametadata=print:key=lavfi.astats.Overall.RMS_level", "-f", "null", "-"],
        capture_output=True, text=True).stderr
    temps = [float(x) for x in re.findall(r"pts_time:([\d.]+)", sortie)]
    niveaux = [float(x) if x not in ("-inf", "inf") else -90.0
               for x in re.findall(r"RMS_level=(-?[\d.]+|-?inf)", sortie)]
    trous = [(cues[i][1], cues[i + 1][0]) for i in range(len(cues) - 1)
             if cues[i + 1][0] - cues[i][1] >= 1.5]
    parle = dans_intervalles([(d, f) for d, f, _ in cues])
    dans_trou = dans_intervalles(trous)
    voix = [n for t, n in zip(temps, niveaux) if parle(t)]
    fond = [n for t, n in zip(temps, niveaux) if dans_trou(t)]
    moy = lambda l: round(statistics.mean(l), 1) if l else None
    return moy(voix), moy(fond)


def captures(video, video_id, chaine, duree):
    """Captures clés : 0, 5, 10, 20, 30 s, milieu, dernières 15 s + planche contact (1 image/20 s)."""
    dossier = CAPTURES / chaine.strip("@")
    dossier.mkdir(parents=True, exist_ok=True)
    for t in [0, 5, 10, 20, 30, duree / 2, max(duree - 15, 0)]:
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-ss", str(t), "-i", str(video),
                        "-frames:v", "1", str(dossier / f"{video_id}_t{int(t):04d}.jpg")])
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(video), "-vf",
                    "fps=1/20,scale=192:-1,tile=8x8", "-frames:v", "1",
                    str(dossier / f"{video_id}_planche.jpg")])


def analyser(video_id, chaine, langue):
    info = telecharger(video_id, langue)
    video = next(TMP.glob(f"{video_id}.mp4"))
    duree = info.get("duration") or 1
    cues = lire_sous_titres(video_id)
    mots, wpm = debit(cues)
    scenes = coupes(video)
    plans = [f - d for d, f in scenes] or [duree]
    coupes_30s = sum(1 for d, _ in scenes if 0 < d <= 30)
    voix_db, fond_db = niveau_musique(video, cues)
    captures(video, video_id, chaine, duree)
    ligne = {
        "chaine": chaine,
        "id": video_id,
        "url": f"https://www.youtube.com/watch?v={video_id}",
        "titre": info.get("title"),
        "date": info.get("upload_date"),
        "vues": info.get("view_count"),
        "duree_s": duree,
        "mots": mots,
        "mots_min": round(wpm),
        "coupes_min": round(len(scenes) / (duree / 60), 1),
        "plan_moyen_s": round(statistics.mean(plans), 2),
        "plan_median_s": round(statistics.median(plans), 2),
        "coupes_30_premieres_s": coupes_30s,
        "part_visage_pct": round(part_visage(video, scenes)),
        "chapitres_youtube": len(info.get("chapters") or []),
        "sommaire_dit_pct": positions(cues, SOMMAIRE, duree)[:3],
        "volume_voix_db": voix_db,
        "volume_silences_db": fond_db,
        "miniature": info.get("thumbnail"),
        "texte_30_premieres_s": " ".join(t for d, _, t in cues if d <= 30)[:600],
    }
    for nom, motif in CTA.items():
        ligne[f"cta_{nom}_pct"] = positions(cues, motif, duree)[:5]
    # Analyse uniquement : on supprime la vidéo et les sous-titres bruts.
    for f in TMP.glob(f"{video_id}*"):
        f.unlink()
    return ligne


def moyennes(lignes):
    champs = ["duree_s", "vues", "mots_min", "coupes_min", "plan_moyen_s",
              "coupes_30_premieres_s", "part_visage_pct", "volume_voix_db", "volume_silences_db"]
    out = ["| Chaîne | " + " | ".join(champs) + " |", "|" + "---|" * (len(champs) + 1)]
    for chaine in CHAINES:
        rows = [l for l in lignes if l["chaine"] == chaine]
        vals = []
        for c in champs:
            nums = [r[c] for r in rows if isinstance(r[c], (int, float))]
            vals.append(f"{statistics.mean(nums):.1f}" if nums else "—")
        out.append(f"| {chaine} | " + " | ".join(vals) + " |")
    return "\n".join(out) + "\n"


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--n", type=int, default=5)
    p.add_argument("--chaines", nargs="*", default=list(CHAINES))
    args = p.parse_args()
    RESULTATS.mkdir(exist_ok=True)
    lignes = []
    for chaine in args.chaines:
        for vid in dernieres_videos(chaine, args.n):
            print(f"{chaine} {vid} …", flush=True)
            try:
                lignes.append(analyser(vid, chaine, CHAINES[chaine]))
            except Exception as err:  # une vidéo en échec ne bloque pas les autres
                print(f"  échec : {err}")
    if not lignes:
        raise SystemExit("Aucune vidéo analysée (YouTube accessible depuis cette machine ?)")
    with open(RESULTATS / "style_videos.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(lignes[0]))
        w.writeheader()
        w.writerows(lignes)
    (RESULTATS / "moyennes.md").write_text(moyennes(lignes), encoding="utf-8")
    shutil.rmtree(TMP, ignore_errors=True)
    print(f"OK : {len(lignes)} vidéos → resultats/")


if __name__ == "__main__":
    main()
