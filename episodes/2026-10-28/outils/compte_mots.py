"""Compte les mots narrés par chapitre (hors titres, lignes VISUEL et segments AVIS)."""
import pathlib, re, sys

dossier = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "chapitres")
total, cumul, rows = 0, 0, []
for f in sorted(dossier.glob("*.md")):
    mots, avis = 0, False
    for line in f.read_text(encoding="utf-8").splitlines():
        if line.startswith("## S"):
            avis = "| AVIS |" in line
            continue
        if line.startswith("#") or avis or not line.strip():
            continue
        mots += len(re.findall(r"[\w’'-]+", line))
    rows.append((f.name, mots)); total += mots
for name, m in rows:
    debut = cumul / 195; cumul += m
    print(f"{name:22s} {m:5d} mots  début ~{int(debut)}:{int(debut%1*60):02d}")
print(f"TOTAL {total} mots ≈ {total/195:.1f} min à 195 mots/min ; moitié = {total/2:.0f} mots")
