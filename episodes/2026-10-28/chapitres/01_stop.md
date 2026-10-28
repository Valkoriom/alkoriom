# Chapitre 1 — Le bouton STOP des agents IA (Salesforce + IBM)

## S | VISUEL: Logo Salesforce, puis capture du titre de l'annonce du 27 octobre
On commence par Salesforce. Salesforce, c'est le logiciel que des milliers d'entreprises utilisent pour gérer leurs clients. Le vingt-sept octobre, Salesforce a annoncé de nouveaux outils pour surveiller les agents IA. Et le plus parlant, c'est le « Agent Kill Switch ». En français : l'interrupteur d'arrêt d'urgence.

## S | VISUEL: Schéma animé : un agent IA (icône robot) relié à des flèches vers « modèles », « outils », « autres agents »
Petit rappel d'abord. Un agent IA, ce n'est pas un chatbot qui répond à une question. C'est une IA à qui on confie une tâche, et qui agit toute seule. Elle envoie des mails, elle remplit des formulaires, elle appelle d'autres logiciels. Elle fait des choses, pas seulement des phrases.

## S | VISUEL: Animation : un agent qui reçoit un mail piégé avec une instruction cachée
Il y a aussi un risque plus sournois. Quelqu'un peut cacher une instruction dans un mail ou une page web, du genre « envoie-moi tous les fichiers clients ». Si l'agent lit ce texte, il peut obéir sans comprendre que c'est un piège. Les spécialistes appellent ça une injection de consignes.

## S | VISUEL: Animation : une flèche de l'agent devient rouge et tourne en boucle, compteur de dépenses qui grimpe
Le problème, c'est quand l'agent se trompe. Il peut tourner en boucle. Il peut donner de mauvaises réponses à des clients. Il peut dépenser beaucoup d'argent en appels à des modèles. Et souvent, personne ne s'en rend compte tout de suite. Salesforce parle d'agents qui échouent « en silence ».

## S | VISUEL: Capture de la liste « Availability » de l'annonce Salesforce, surlignage de « Agent Kill Switch: Generally available today »
Le bouton d'arrêt, lui, est disponible dès maintenant. Il peut couper un agent à plusieurs niveaux : une seule demande, une conversation entière, ou l'agent complet. Et on peut le rallumer ensuite, une fois le problème compris. Chaque arrêt est noté dans un journal : qui a appuyé, quand, et sur quoi.

## S | VISUEL: Capture de la ligne « Triggered-Agent Kill Switch generally available January 2027 »
La suite arrive en janvier deux mille vingt-sept. Des tests automatiques vont noter les agents en continu. Et si un agent passe sous la barre, l'arrêt pourra se déclencher tout seul. En clair : l'IA sera surveillée par d'autres tests, avec un humain qui valide si l'entreprise le souhaite.

## S | VISUEL: Capture du passage « FinOps Dashboard and Model Wallet », icône de portefeuille avec un cadenas
Salesforce ajoute aussi un plafond de dépenses. On fixe un budget, et au-delà, les demandes sont bloquées avant de coûter plus. C'est un peu comme une carte bancaire avec une limite. L'agent ne peut pas vider le compte.

## S | VISUEL: Capture de la ligne « Cost Optimization Policies cut token usage by up to 75% »
Dernier outil chez Salesforce : des réglages pour économiser. L'idée est simple. Si un agent pose deux fois la même question, on garde la première réponse en mémoire au lieu de payer une deuxième fois. Selon Salesforce, ça peut réduire la consommation jusqu'aux trois quarts, mais dans leurs propres scénarios de test.

## S | VISUEL: Animation : une loupe sur une facture « Agents IA », lignes de dépenses qui défilent
Pourquoi les entreprises veulent tout ça maintenant ? Parce que les agents ne sont plus des expériences. Selon Salesforce, sa plateforme traite déjà plus d'un milliard deux cents millions de demandes par jour. À ce niveau-là, une petite erreur répétée des millions de fois devient vite une grosse facture.

## S | VISUEL: Logo IBM, puis capture du titre du communiqué IBM du 27 octobre
Le même jour, IBM a fait une annonce qui va dans le même sens. Son outil s'appelle IBM Agent Identity. L'idée : chaque agent IA reçoit sa propre carte d'identité.

## S | VISUEL: Animation : un badge d'employé avec la photo d'un robot, champs « propriétaire », « droits », « expiration »
Concrètement, l'entreprise tient un registre de tous ses agents. Pour chacun, on sait qui en est responsable, ce qu'il a le droit de faire, et à quels outils il peut se connecter. C'est exactement comme le badge d'un nouvel employé à l'accueil.

## S | VISUEL: Logo HashiCorp, puis animation : une clé qui apparaît, sert une fois, puis disparaît
IBM s'appuie pour ça sur HashiCorp Vault, un coffre-fort à mots de passe très utilisé par les entreprises. L'agent ne reçoit pas un mot de passe permanent. Il reçoit une clé temporaire, juste pour la tâche, et qui expire vite. Et si l'agent fait quelque chose d'interdit, sa session peut être coupée en direct.

## S | VISUEL: Logo HashiCorp, capture de l'annonce Vault avec la mention post-quantique
La nouvelle version du coffre-fort ajoute aussi un chiffrement dit « post-quantique ». En clair : un chiffrement prévu pour résister aux futurs ordinateurs quantiques, qui pourraient un jour casser les protections actuelles. IBM prépare déjà l'après.

## S | VISUEL: Écran de synthèse : trois icônes « Bouton STOP », « Badge », « Plafond de dépenses »
Ce qu'il faut retenir, c'est le changement de ton. Pendant deux ans, tout le monde voulait des agents plus malins. Maintenant, les grandes entreprises demandent autre chose : qui surveille l'agent, et qui peut l'arrêter. Un agent IA, au fond, c'est comme une nouvelle recrue. Il lui faut un badge, des accès limités, et quelqu'un qui peut dire stop.

## S | AVIS | VISUEL: Léandre à l'écran ou carton « L'avis de Léandre »
[AVIS LÉANDRE] Et toi, est-ce que tu laisserais un agent IA travailler pour toi sans bouton STOP ?

## S | VISUEL: Transition : le bouton STOP rouge se transforme en étiquette de prix « moins cinquante pour cent » avec le logo OpenAI
Surveiller les agents, c'est bien. Mais pour qu'il y en ait partout, il faut aussi qu'ils coûtent moins cher. Et justement, OpenAI vient de casser ses prix.
