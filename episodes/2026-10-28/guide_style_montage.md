# Guide de style montage — AlkoriomAi

> **État des mesures (28/10, après ouverture du réseau).** Les données publiques des 20 vidéos ont été relevées sur la page « Vidéos » de chaque chaîne : titre, vues, durée, miniature. Les miniatures ont été téléchargées pour analyse interne et ne sont pas versionnées. **Le téléchargement des vidéos est refusé par YouTube** (« Sign in to confirm you're not a bot ») depuis les serveurs cloud. Je ne contourne pas cette protection. Les mesures qui exigent le fichier vidéo (débit, coupes/min, plans, musique, appels à l'action, 30 premières secondes) restent donc marquées « non mesuré ». On les obtient avec `python3 outils/analyse_style.py`, lancé depuis un ordinateur personnel, ou en fournissant les fichiers vidéo.
> Les vues sont celles du 28/10. Les vidéos les plus récentes (AesHUcW-B3s, 1kQ_1_QL5Es) ont quelques heures et ne sont pas comparables.
> Les titres de SamouraiDansant s'affichent **en anglais** : YouTube les traduit automatiquement pour la région du serveur. Les miniatures, elles, sont en français. Les titres originaux restent à relever.

## 1. Tableau comparatif (20 vidéos)

Colonnes non mesurables sans le fichier vidéo : mots/min, coupes/min, plan moyen, mélange de visuels, 30 premières s, sommaire, transitions, musique, position des appels à l'action, écran de fin.

| Chaîne | Vidéo | Titre (tel qu'affiché) | Durée | Vues (28/10) | Car. titre | Miniature |
|---|---|---|---|---|---|---|
| SamouraiDansant | [AesHUcW-B3s](https://www.youtube.com/watch?v=AesHUcW-B3s) | Microsoft: The Two Shock Absorbers | 24:33 | 4,5 k (très récente) | 34 | Portrait N&B détouré à droite, logos Microsoft en couleur, 4 mots blancs en capitales |
| SamouraiDansant | [IHs3jiBz6yU](https://www.youtube.com/watch?v=IHs3jiBz6yU) | New MacBooks & AI: The Real Math Before Buying Apple This Year | 28:47 | 60 k | 62 | Portrait N&B, produit (MacBook) en couleur, chiffre « 24 Go » + 3 mots |
| SamouraiDansant | [O8LpZbK8dgg](https://www.youtube.com/watch?v=O8LpZbK8dgg) | The web is broken: What the last 48 hours have revealed | 34:47 | 93 k | 55 | Portrait N&B, illustration d'engrenages, 3 mots en capitales |
| SamouraiDansant | [QzgsvzV7c8Y](https://www.youtube.com/watch?v=QzgsvzV7c8Y) | "They've annihilated my field": The job we thought was untouchable has just fallen | 28:31 | 58 k | 82 | Groupe de six personnalités en N&B, 4 mots en capitales |
| SamouraiDansant | [6C4dc7VhzmY](https://www.youtube.com/watch?v=6C4dc7VhzmY) | Nobody is ready for the world Elon Musk showed us last night | 26:41 | 64 k | 60 | Portrait N&B, 3 logos de marques, véhicule, 3 mots |
| VisionIA-FR | [gvh9JpAC7GI](https://www.youtube.com/watch?v=gvh9JpAC7GI) | Voici ce que l'IA vient de trouver dans le cerveau | 23:22 | 112 k | 50 | Visage du créateur (mains jointes, inquiet), halo rouge, 2 blocs de texte jaune et blanc |
| VisionIA-FR | [Cd4VaFWb4U8](https://www.youtube.com/watch?v=Cd4VaFWb4U8) | La robotique vient de basculer en 7 jours (et personne n'en parle) | 18:01 | 238 k | 66 | Créateur (mains sur la tête), robots en usine, personnalité, drapeau, texte blanc sur bandeau rouge + texte jaune |
| VisionIA-FR | [ugNTkcvND08](https://www.youtube.com/watch?v=ugNTkcvND08) | Voici ce que l'IA vient de trouver au cœur d'Internet | 16:53 | 111 k | 53 | Créateur (main sur le visage), logos OpenAI et Google, flèche rouge, « FAILLE CRITIQUE » en rouge |
| VisionIA-FR | [8GMoD4Subss](https://www.youtube.com/watch?v=8GMoD4Subss) | L'IA vidéo vient de briser sa plus grosse limite | 22:30 | 103 k | 48 | Créateur (mains sur la tête), puce dorée cerclée de rouge, question en capitales blanches |
| VisionIA-FR | [H2a8MuxpDWw](https://www.youtube.com/watch?v=H2a8MuxpDWw) | Cette IA ne sait pas écrire (et OpenAI la copie déjà) | 16:21 | 105 k | 53 | Créateur (mains sur la tête), logo produit néon rose, texte jaune avec « ! » |
| AILABS-393 | [1kQ_1_QL5Es](https://www.youtube.com/watch?v=1kQ_1_QL5Es) | This Is Microsoft's New Plan To Fix Claude's Usage Limits | 13:08 | 6,8 k (très récente) | 57 | Fond anthracite, logos plats reliés par un schéma, 2 mots dont 1 surligné jaune |
| AILABS-393 | [xxf6D9jynFw](https://www.youtube.com/watch?v=xxf6D9jynFw) | EGM: Google's New Way To Use Claude Code Is Insane | 15:54 | 158 k | 50 | Fond anthracite, logo Google + icône produit, 2 mots dont 1 surligné |
| AILABS-393 | [92ZDgn8bgLM](https://www.youtube.com/watch?v=92ZDgn8bgLM) | Anthropic Just Revealed How Their Engineers Use Claude Code | 11:48 | 48 k | 59 | Fond anthracite, personnalité détourée, orbite d'icônes, 3 mots dont 2 surlignés |
| AILABS-393 | [y2ifUC9_zuU](https://www.youtube.com/watch?v=y2ifUC9_zuU) | Vercel's CEO's AI Coding Workflow Is Actually Insane | 14:22 | 51 k | 52 | Fond anthracite, personnalité détourée sur bande papier, icônes d'outils, 2 mots |
| AILABS-393 | [NZjjmf3I6I4](https://www.youtube.com/watch?v=NZjjmf3I6I4) | 6 Insane Trending GitHub AI Design Repos You Need to Use | 10:21 | 62 k | 56 | Fond anthracite, faux bouton GitHub « Star 163K », flèche rouge, 3 mots |
| theAIsearch | [EfyQOAJjx1A](https://www.youtube.com/watch?v=EfyQOAJjx1A) | Cyber hacks, Kimi K3.1, AI for DNA, AI for engineering, new TTS, Claude Duet, Dessa: AI NEWS | 43:06 | 357 k | 93 | Bandeau bleu « huge AI news » + 2 images tirées des sujets |
| theAIsearch | [1Aqhg0FVm-w](https://www.youtube.com/watch?v=1Aqhg0FVm-w) | Deepseek strikes again | 27:22 | 922 k | 22 | Bandeau bleu « they're back », portrait sur explosion + logo baleine lumineux |
| theAIsearch | [cUeZMUGCxrw](https://www.youtube.com/watch?v=cUeZMUGCxrw) | New top local AI image generator is here! | 21:56 | 393 k | 41 | Bandeau bleu « free & unlimited », photo + exemples d'images générées |
| theAIsearch | [tDWtcyeNNew](https://www.youtube.com/watch?v=tDWtcyeNNew) | Quantum breakthrough, Gemini 4 Argon, MOSS Image, KLING 4, OpenAI spy, Muse Wonder: AI NEWS | 40:55 | 579 k | 91 | Bandeau bleu « huge AI news » + 2 images tirées des sujets |
| theAIsearch | [X0_GDOkLKzQ](https://www.youtube.com/watch?v=X0_GDOkLKzQ) | New AI enzymes, 700+ math breakthroughs, AI for DNA mutations, room temp semiconductors: AI NEWS | 45:12 | 398 k | 96 | Bandeau bleu « huge AI news » + 2 images tirées des sujets |

## 2. Moyennes par chaîne

| Chaîne | Durée moy. (min-max) | Vues moy. | Vues médiane | Long. titre moy. | Visage du créateur sur la miniature | Mots sur la miniature |
|---|---|---|---|---|---|---|
| SamouraiDansant | 28:39 (24:33-34:47) | 55,9 k | 60 k | 59 car. | 0/5 (personnalités en N&B) | 2-4, capitales blanches |
| VisionIA-FR | 19:25 (16:21-23:22) | 133,8 k | 111 k | 54 car. | 5/5 (expression choquée) | 2-5, jaune/rouge, « ! » ou « ? » |
| AILABS-393 | 13:06 (10:21-15:54) | 65,2 k | 51 k | 55 car. | 0/5 | 2-3, 1 mot surligné jaune |
| theAIsearch | 35:42 (21:56-45:12) | 529,8 k | 398 k | 69 car. | 0/5 | 2-3, minuscules blanches sur bandeau fixe |
| **AlkoriomAi (épisode 28/10)** | ≈ 25:37 | — | — | cible ≤ 60 | 0 (règle 10) | 2-4, or pâle |

Mots/min, coupes/min, plan moyen, % face caméra et niveaux sonores : **non mesuré** (le téléchargement des vidéos est bloqué par YouTube).

**Ce que montrent les données publiques**
- **Un gabarit fixe.** Chaque chaîne garde la même charte sur 5/5 miniatures : bandeau bleu chez theAIsearch, fond anthracite et surlignage jaune chez AI LABS, noir et blanc chez Samouraï, visage choqué chez Vision IA. La chaîne est reconnaissable avant même de lire le titre.
- **Un sujet fort bat une liste.** Chez theAIsearch, le titre de 22 caractères sur un seul sujet (DeepSeek, 922 k) bat les récapitulatifs de 91-96 caractères (357-579 k).
- **Une formule répétée.** Vision IA utilise « vient de… » dans 4 titres sur 5, et 2 sur 5 se terminent par une parenthèse. Leur meilleure vidéo, la robotique (238 k), fait le double de la médiane de la chaîne.
- **La durée.** Les deux chaînes francophones durent 16 à 35 min. Nos ≈ 25 min sont dans la fourchette.
- **Les logos.** Ils sont présents sur 10/20 miniatures (5/5 chez AI LABS ; Microsoft, Google, OpenAI, Tesla, DeepSeek…). C'est cohérent avec la règle « logos à l'écran » de Léandre.

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
10. **Miniature et titre : un sujet, une promesse vraie, un gabarit fixe.** Comme les 4 concurrents (5/5 miniatures cohérentes chez chacun), un seul gabarit AlkoriomAi pour toutes les vidéos : fond noir, un mot surligné en or pâle, logo du sujet en couleur, accent bleu électrique. Titre de 60 caractères maximum, un sujet principal (le plus gros nom du jour) et au plus une marque ou un chiffre en plus. Pas de liste de 5 noms. Miniature à 3 éléments maximum (objet ou robot, logo, 2 à 4 mots en or pâle sur fond noir et bleu électrique), lisible à 160 px de large. Interdits : faux visage choqué, flèches rouges, promesse absente de la vidéo.

## 4. Garde-fous

- Ne jamais reprendre une phrase, une image, une miniature ou un plan d'une vidéo concurrente. Les captures du script sont réservées à l'analyse interne et restent hors du dossier de montage.
- Chaque visuel factuel vient de la source officielle listée dans sources.md, avec son lien exact.
