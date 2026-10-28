# Guide de style montage — AlkoriomAi

> **État des mesures (à lire d'abord).** Le guide devait s'appuyer sur 20 vidéos mesurées (5 par chaîne). Le réseau de cette session bloque youtube.com : ni téléchargement, ni transcription, ni PySceneDetect, ni captures n'ont été possibles. Je n'ai donc **inventé aucun chiffre concurrent**. Les colonnes mesurées restent vides (« ? »).
> Pour les remplir, sur une machine qui a accès à YouTube :
> `pip install yt-dlp "scenedetect[opencv-headless]"` puis `python3 outils/analyse_style.py`
> Le script récupère les 5 dernières vidéos de chaque chaîne en ≤ 240p. Il mesure le débit (mots/min via les sous-titres auto), les coupes/min, la durée moyenne et médiane des plans, les coupes dans les 30 premières secondes, la part de plans avec visage, la position des appels à l'action et du sommaire, et le volume pendant la parole et dans les silences (indice du niveau de musique). Il sort aussi 7 captures et une planche contact par vidéo, puis **supprime les vidéos**.
> Les **10 règles** ci-dessous sont des **cibles chiffrées pour AlkoriomAi**. Elles s'appuient sur notre script (195 mots/min, ≈ 25 min), sur les retours de Léandre et sur les standards de diffusion YouTube. Il faudra les recaler une fois les moyennes concurrentes mesurées.

## 1. Tableau comparatif (20 vidéos)

| Chaîne | Vidéo | Durée | Vues | Mots/min | Coupes/min | Plan moyen (s) | Face cam / démos / captures / B-roll / texte (%) | 30 premières s | Sommaire | Transitions | Musique (présence / changements / niveau sous voix) | CTA (position) | Écran de fin | Miniature / titre |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SamouraiDansant | IHs3jiBz6yU (26/10) | ? | 55 k | ? | ? | ? | ? | ? | ? | ? | ? | ? | ? | ? |
| SamouraiDansant | O8LpZbK8dgg (22/10) | ? | 92 k | ? | ? | ? | ? | ? | ? | ? | ? | ? | ? | ? |
| SamouraiDansant | 3 autres (à récupérer) | ? | ? | ? | ? | ? | ? | ? | ? | ? | ? | ? | ? | ? |
| VisionIA-FR | gvh9JpAC7GI (28/10) | ? | 22 k | ? | ? | ? | ? | ? | ? | ? | ? | ? | ? | ? |
| VisionIA-FR | Cd4VaFWb4U8 (26/10) | ? | 222 k | ? | ? | ? | ? | ? | ? | ? | ? | ? | ? | Titre : rupture + urgence + parenthèse (« … (et personne n'en parle) ») |
| VisionIA-FR | 3 autres (à récupérer) | ? | ? | ? | ? | ? | ? | ? | ? | ? | ? | ? | ? | ? |
| AILABS-393 | xxf6D9jynFw | ? | 151 k | ? | ? | ? | ? | ? | ? | ? | ? | ? | ? | ? |
| AILABS-393 | 92ZDgn8bgLM | ? | ? | ? | ? | ? | ? | ? | ? | ? | ? | ? | ? | ? |
| AILABS-393 | 3 autres (à récupérer) | ? | ? | ? | ? | ? | ? | ? | ? | ? | ? | ? | ? | ? |
| theAIsearch | EfyQOAJjx1A (~25/10) | 43:06 | 352 k | ? | ? | ? | ? | ? | ? | ? | ? | Sponsor (Luma) : position ? | ? | Titre « catalogue » : 7 noms + « AI NEWS » |
| theAIsearch | 1Aqhg0FVm-w (~23/10) | ? | 909 k | ? | ? | ? | ? | ? | ? | ? | ? | Sponsor (Higgsfield) : position ? | ? | Titre court, un seul nom fort (« Deepseek strikes again ») |
| theAIsearch | 3 autres (à récupérer) | ? | ? | ? | ? | ? | ? | ? | ? | ? | ? | ? | ? | ? |

## 2. Moyennes par chaîne

| Chaîne | Durée moy. | Vues moy. | Mots/min | Coupes/min | Plan moyen (s) | Coupes 0-30 s | % face cam | Voix (dB) | Silences (dB) |
|---|---|---|---|---|---|---|---|---|---|
| SamouraiDansant | ? | ? | ? | ? | ? | ? | ? | ? | ? |
| VisionIA-FR | ? | ? | ? | ? | ? | ? | ? | ? | ? |
| AILABS-393 | ? | ? | ? | ? | ? | ? | ? | ? | ? |
| theAIsearch | ? | ? | ? | ? | ? | ? | ? | ? | ? |
| **AlkoriomAi (cible)** | 22-26 min | — | 185-195 | 10-15 | 4-6 | ≥ 6 | ≤ 10 | −14 LUFS | musique à −32/−34 LUFS |

*(Le script génère ce tableau dans `resultats/moyennes.md`.)*

**Seules observations possibles sans les vidéos** (titres et vues) : chez theAIsearch, la vidéo sur un seul sujet fort fait environ 2,6 fois les vues du récapitulatif. Chez Vision IA, le bilan robotique hebdomadaire fait dix fois la vidéo du jour. Les deux chaînes anglophones affichent un sponsor dans la description.

## 3. Dix règles chiffrées pour AlkoriomAi

1. **Accroche en 15 secondes, rythme d'ouverture soutenu.** Premier changement d'image avant 3 s. Au moins 6 changements de visuel dans les 30 premières secondes. Aucun logo de chaîne ni auto-présentation avant le sommaire. Le sommaire commence avant 0:25 et se termine avant 1:10.
2. **Le visuel = exactement ce qui est dit.** Chaque segment `## S` a son propre visuel. Le visuel change sur la première syllabe du segment (tolérance ±0,5 s). Quand on cite un chiffre ou une phrase officielle, la capture est zoomée à 110-130 % sur la ligne exacte, avec un surlignage qui apparaît au moment où la phrase est dite. Aucun visuel « d'ambiance » sur un fait précis.
3. **Un changement de visuel toutes les 4 à 6 secondes**, soit 10 à 15 par minute. Aucun plan fixe de plus de 8 s, sauf un graphique commenté (12 s maximum, avec une animation interne : barre qui monte, surlignage). Un segment de 40 à 70 mots dure environ 12-22 s : il faut donc 2 à 4 visuels par segment.
4. **Les logos d'abord.** Le logo de l'entreprise s'affiche dans la seconde qui suit sa première mention : 2 à 3 s en grand, puis une pastille dans un coin pendant tout le chapitre. Deux logos (partenariat) : côte à côte, même taille. Toujours les logos officiels issus des kits presse, avec le lien noté dans sources.md.
5. **Une seule musique, sans chevauchement.** Une seule piste de type « Lightless Dawn » pour toute la vidéo, en boucle propre. Jamais deux musiques en même temps, jamais de fondu enchaîné entre deux pistes. Fondu d'entrée de 2 s, fondu de sortie de 3 s sur l'écran de fin. Niveaux : voix à −14 LUFS intégré, musique 18 à 20 dB sous la voix (≈ −32/−34 LUFS). Pendant les blocs AVIS, baisser la musique de 6 dB de plus. Maximum un « whoosh » par transition de chapitre, aucun bruitage sur les coupes internes.
6. **Le sommaire est visible et repris.** Liste à puces à l'écran, chaque ligne apparaît quand elle est dite. À chaque nouveau chapitre, un carton de 1,5-2 s rappelle le sommaire avec le point en cours en bleu électrique et les points passés cochés. Dans la description, au moins 10 chapitres YouTube, le premier à 0:00, chacun d'au moins 10 s.
7. **La vulgarisation se voit aussi.** Chaque terme technique (agent, poids ouverts, diffusion, S-1, MCP…) a son « en clair » oral et un mot-clé à l'écran de 6 mots maximum, au plus un toutes les 10 s. Un schéma simple remplace toute explication de plus de 20 s. Sous-titres incrustés en 2 lignes de 32 caractères maximum, si on les active.
8. **Les appels à l'action sont placés précisément.** Aucun appel avant 60 s. L'appel à l'abonnement (abonnez-vous, likez, partagez, merci) tombe entre 45 et 55 % de la durée (≈ 47 %, soit 12:02, dans l'épisode du 28/10) et dure moins de 20 s. L'appel à commenter vient dans la dernière minute. Écran de fin : 20 s avec 2 éléments (vidéo suivante et abonnement), musique seule, sans nouvelle info.
9. **Le mélange de visuels est maîtrisé.** Captures de sources officielles et démos officielles : au moins 50 % du temps. Schémas et animations explicatives : 30 à 40 %. Carton ou Léandre à l'écran (AVIS) : 10 % maximum. B-roll générique : 10 % maximum, jamais sur un fait chiffré. Toute démo d'entreprise porte un bandeau « Démo officielle [entreprise] » d'au moins 3 s. Toute vidéo promotionnelle (ex. Unitree) porte un bandeau d'avertissement.
10. **Miniature et titre : un sujet, une promesse vraie.** Titre de 60 caractères maximum, un sujet principal (le plus gros nom du jour) et au plus une marque ou un chiffre en plus. Pas de liste de 5 noms. Miniature à 3 éléments maximum (objet ou robot, logo, 2 à 4 mots en or pâle sur fond noir et bleu électrique), lisible à 160 px de large. Interdits : faux visage choqué, flèches rouges, promesse absente de la vidéo.

## 4. Garde-fous

- Ne jamais reprendre une phrase, une image, une miniature ou un plan d'une vidéo concurrente. Les captures du script sont réservées à l'analyse interne et restent hors du dossier de montage.
- Chaque visuel factuel vient de la source officielle listée dans sources.md, avec son lien exact.
