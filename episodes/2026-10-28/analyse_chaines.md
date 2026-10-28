# Veille concurrents — épisode du 28/10/2026

> **Limite importante.** Le réseau de cette session bloque youtube.com et les sites des sources officielles (openai.com, salesforce.com, etc.). Seule la recherche web passait. Résultat : **aucune transcription n'a pu être téléchargée** (yt-dlp renvoie « 403 Forbidden ») et les titres, durées et vues ci-dessous viennent des repères déjà relevés ou d'index tiers. Les cases « ? » restent à compléter avec `python3 outils/analyse_style.py`, à lancer depuis une machine qui a accès à YouTube.

## 1. Vidéos relevées

| Chaîne | Titre | Date | Vues | Durée | URL |
|---|---|---|---|---|---|
| @SamouraiDansant (chaîne renommée « IA et Stratégie ») | ? | 26/10 | 55 k | ? | https://www.youtube.com/watch?v=IHs3jiBz6yU |
| @SamouraiDansant | ? | 22/10 | 92 k | ? | https://www.youtube.com/watch?v=O8LpZbK8dgg |
| @VisionIA-FR | ? | 28/10 | 22 k | ? | https://www.youtube.com/watch?v=gvh9JpAC7GI |
| @VisionIA-FR | « La robotique vient de basculer en 7 jours (et personne n'en parle) » | 26/10 | 222 k | ? | https://www.youtube.com/watch?v=Cd4VaFWb4U8 |
| @AILABS-393 | ? (chaîne de tutoriels « construire avec l'IA », éditée par autometa.dev) | ? | 151 k | ? | https://www.youtube.com/watch?v=xxf6D9jynFw |
| @AILABS-393 | ? | ? | ? | ? | https://www.youtube.com/watch?v=92ZDgn8bgLM |
| @theAIsearch | « Cybersecurity chaos, AI for DNA, Kimi K3.1, Claude Duet, Dessa, Fibo 2, Minimax 3.1: AI NEWS » (sponsor : Luma) | ~25/10 | 352 k (263 k selon un index tiers, relevé plus tôt) | 43:06 (index tiers) | https://www.youtube.com/watch?v=EfyQOAJjx1A |
| @theAIsearch | « Deepseek strikes again » (DeepSeek V4.1 Flash + DeepInfer ; sponsor : Higgsfield) | ~23/10 | 909 k | ? | https://www.youtube.com/watch?v=1Aqhg0FVm-w |

## 2. Analyse (limitée aux titres, sujets et descriptions)

**Sujets couverts par les concurrents**
- theAIsearch : récapitulatif hebdomadaire de 43 minutes. Au menu : cyberattaques menées par des IA, IA appliquée à l'ADN, Kimi K3.1 Pro, Claude Duet (agent proactif d'Anthropic), Dessa (voix), Fibo 2, MiniMax M3.1, Hi3D. À côté, une vidéo dédiée à un seul sujet : DeepSeek V4.1 Flash et DeepInfer.
- Vision IA : un bilan robotique de la semaine (« en 7 jours »). Les descriptions renvoient vers leur académie payante.
- IA et Stratégie (ex-Samouraï Dansant) : analyses stratégiques (business, carrière, finance). Le sujet précis des deux dernières vidéos n'a pas pu être lu.
- AI LABS : tutoriels pratiques. Le sujet des deux vidéos n'a pas pu être lu.

**Sujets absents de notre script (et décision)**

| Sujet | Date | Décision |
|---|---|---|
| **Anthropic dépose son S-1 (entrée en Bourse, Nasdaq « ANT »)** | 26/10 | **AJOUTÉ** (chapitre 02c) : moins de 72 h, source officielle trouvée |
| OpenAI annonce trois résultats scientifiques (Kakeya, hypothèse ETH réfutée, physique QCD) | 26/10 | Non ajouté : page officielle openai.com introuvable via la recherche, et les résultats sont en cours de relecture par des experts. À reconsidérer si le lien officiel est vérifié. |
| Claude Duet (agent proactif d'Anthropic, préversion de recherche) | 21/10 | Non ajouté : plus de 72 h |
| MiniMax M3.1 Flash | 19/10 | Non ajouté : plus de 72 h, sources secondaires seulement |
| DeepSeek V4.1 Flash / DeepInfer | ~23/10 | Non ajouté : plus de 72 h |
| Dessa, Fibo 2, Hi3D, « IA pour l'ADN » | ~25/10 | Non ajouté : aucune source officielle trouvée |
| NVIDIA × Oracle (extension OCI en Vera Rubin) | 28/10 | Non ajouté : communiqué NVIDIA introuvable via la recherche. Candidat « en bref » une fois le lien vérifié. |

**Angle et accroche (d'après les titres)**
- theAIsearch empile 5 à 7 noms de marques dans le titre. C'est l'effet « catalogue » : le spectateur repère au moins un sujet qui l'intéresse.
- Vision IA mise sur la rupture et l'urgence (« vient de basculer », « (et personne n'en parle) », « en 7 jours »), avec une parenthèse qui crée de la curiosité.
- Quand un seul sujet très attendu sort (DeepSeek), une vidéo dédiée fait environ 2,6 fois les vues du récapitulatif (909 k contre 352 k).

**Structure, rythme, montage** : non mesurés (pas d'accès aux vidéos). Voir `guide_style_montage.md` et le script de mesure.

## 3. Enseignements

1. **Un gros nom bat un catalogue.** La vidéo DeepSeek seule fait environ 2,6 fois le récapitulatif de la même chaîne. Notre titre doit donc porter un seul sujet fort, par exemple « Le bouton STOP des IA » ou « Anthropic entre en Bourse », plutôt qu'une liste.
2. **La robotique fait des vues en français.** Le bilan robotique de Vision IA atteint 222 k, soit dix fois leur vidéo du jour. Il faut garder le teaser Unitree dans l'accroche et soigner le chapitre robots.
3. **Notre avantage, c'est la fraîcheur.** Salesforce, Terra, Oracle et IBM datent du 27/10, après les récapitulatifs du 25-26/10 des concurrents. L'accroche doit insister sur « hier ».
4. **L'urgence sans exagération.** Les formules « vient de… » marchent, mais notre ligne, c'est le vérifié. Exemple : « Les IA ont maintenant un bouton STOP », sans promesse fausse.
5. **Le sujet finance/Bourse était un trou dans notre script.** C'est l'événement le plus médiatisé du 26/10. Il est ajouté, avec les chiffres expliqués simplement (perte surtout comptable).

## 4. Ce qui a été ajouté ou modifié dans le script

- **Nouveau chapitre `02c_anthropic.md`** (354 mots) : le dépôt du S-1, Nasdaq « ANT », prix pas encore fixé, ce qu'est un S-1, revenus du premier semestre (≈ 16,3 Md$ contre ≈ 1,2 Md$), la perte de ≈ 80,7 Md$ dont ≈ 72,4 Md$ comptables, la société à mission, et pourquoi c'est important. Il contient un bloc AVIS.
- **Accroche et sommaire** : un teaser Anthropic ajouté, et un sommaire renuméroté de un à neuf.
- **L'appel à l'abonnement passe après Kimi** (fichier `03b_abonnement.md`). Il démarre à environ 47 % de la durée (≈ 12:02 sur ≈ 25:37).
- **Transitions réécrites** : Oracle → Anthropic → Kimi → pause → LFM3 → Clover.
- **Bilan** : la ligne Anthropic et son logo sont ajoutés.
- **Voix de synthèse** : « LFM3 » devient « LFM trois », « 3D » devient « en volume » ou « trois D », « S-1 » devient « S un » à l'oral.
- **Total : 4 996 mots hors AVIS** (≈ 25:37 à 195 mots/min).

> ⚠️ Les faits du script d'origine (Salesforce, Terra, Oracle, Kimi, LFM3, Clover, Tellers, Genie 4, robots, NVIDIA/Meta, MAI Image) **n'ont pas pu être revérifiés** dans cette session, faute d'accès aux sites officiels.
