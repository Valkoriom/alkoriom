# Chapitre 6 — Clover : l'IA qui écrit tous les mots en même temps

## S | VISUEL: Animation : une phrase qui apparaît mot par mot, de gauche à droite
Pour comprendre cette nouvelle, il faut savoir comment écrit une IA comme ChatGPT. Elle produit un mot, puis le suivant, puis le suivant. Toujours un par un, de gauche à droite. C'est pour ça qu'on voit la réponse s'afficher petit à petit.

## S | VISUEL: Animation : une phrase floue, pleine de cases grises, qui devient nette d'un coup
Il existe une autre méthode : la diffusion. C'est la technique qu'on utilise déjà pour générer des images. On part d'un brouillon flou, et on le rend net, étape par étape. Appliqué au texte, ça veut dire que l'IA remplit plusieurs mots en même temps, puis corrige l'ensemble.

## S | VISUEL: Logo DiffuSpace, puis capture de la page GitHub Clover-35B-A3B-Preview
Une équipe issue de l'université de Hong Kong, réunie dans l'entreprise DiffuSpace, vient de publier Clover. C'est le premier grand modèle de texte par diffusion à poids ouverts. Il compte trente-cinq milliards de paramètres, mais seulement trois milliards travaillent à chaque mot.

## S | VISUEL: Graphique en barres : « Clover : 515 mots-clés par seconde ; autre méthode accélérée : 365 », source blog DiffuSpace
Le résultat, c'est la vitesse. Sur une seule carte graphique, Clover produit plus de cinq cents mots-clés par seconde dans des tâches d'agent. Bien plus vite qu'un modèle classique de la même taille, même accéléré.

## S | VISUEL: Capture du passage sur la RTX 5070 Ti 16 Go (blog DiffuSpace)
Et DiffuSpace a réussi à le faire tourner sur une carte graphique grand public avec seize gigaoctets de mémoire, en version compressée. Là encore, environ deux fois plus vite que des modèles classiques de même taille.

## S | VISUEL: Extrait de la démo « Route Planning » du blog DiffuSpace (recherche d'itinéraire vers un Wendy's)
DiffuSpace montre une démo parlante. On demande à l'IA combien de temps il faut pour aller en voiture jusqu'au fast-food le plus proche. Le site de cartes se trompe et propose un restaurant dans une autre ville. Clover s'en rend compte, précise la recherche, et trouve le bon : trois minutes de route. Un modèle concurrent, lui, est resté bloqué sur un restaurant à plus de trois cents kilomètres.

## S | VISUEL: Extrait de la démo « GenUI : bureau interactif dans un seul fichier HTML »
Autre démo : on lui demande de créer un faux bureau d'ordinateur dans une seule page web. Avec des fenêtres qu'on déplace, une calculatrice, un bloc-notes, une horloge. Et tout fonctionne.

## S | VISUEL: Capture de la démo « drone dispatch » du blog DiffuSpace
Dernière démo, plus technique : la gestion de drones dans une ville. L'IA reçoit un message compliqué avec cinq ordres mélangés. Clover sort les cinq bonnes réponses en moins d'une seconde. Le modèle concurrent met près de quatre secondes, et se trompe sur une mission.

## S | VISUEL: Animation : un agent qui fait des allers-retours rapides entre « décider » et « agir »
Pourquoi la vitesse compte autant ? Parce qu'un agent IA fait des dizaines d'allers-retours pour une seule tâche. Il réfléchit, il agit, il regarde le résultat, il recommence. Si chaque étape va trois fois plus vite, la tâche entière va trois fois plus vite.

## S | VISUEL: Capture de la mention « Preview » et licence Apache sur Hugging Face
Attention quand même : c'est une version d'essai, une « preview ». Et il est encore trop lourd pour un ordinateur portable classique. Mais il est gratuit, sous licence libre, et c'est peut-être le début d'une nouvelle façon de faire écrire les IA.

## S | AVIS | VISUEL: Carton « L'avis de Léandre »
[AVIS LÉANDRE] Est-ce que tu penses que la diffusion va remplacer la méthode classique, ou rester une curiosité ?

## S | VISUEL: Transition : une timeline de montage vidéo qui se remplit toute seule, logo Tellers
Des IA plus rapides, c'est bien. Mais certaines s'attaquent aussi à des métiers créatifs. Par exemple : le montage vidéo.
