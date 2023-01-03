pour jouer au jeu (besoin de pygame): 
python MainUI_player.py -level level_3.txt
(avec level_3.txt le nom d'un niveau présent dans le dossier 'levels')

pour lancer le jeu en mode IA:
(la solution sera sauvegardée dans le dossier 'IA_solutions')
-avec interface:
python MainIA_UI.py -level level_IA_04.txt -fps 5
(fps le nombre de mouvement par seconde)
-sans interface:
python MainIA.py -level level_IA_04.txt

pour (re)regarder le déroulement d'une solution trouvée:
python ReadIA.py -level level_IA_04.txt -fps 5
('level_IA_04.txt' un exemple de solution sauvegardée dans le dossier IA_solutions dont le niveau original avec le même nom est présent dans 'levels')


dans le cas du jeu lancé en mode manuel :

-Mouvement: touches ZQSD
-Revenir en arrière: R

-Condition de fin:
--Victoire:
On gagne quand un objet marqué 'YOU' se trouve sur une case marquée 'WIN'.
--Défaite:
Une situation de blocage donc de défaite est une situation où aucun objet n'est marqué comme 'YOU' et donc nos actions n'ont plus de conséquences sur le jeu.


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Code de BABA :

A chaque mouvement valide du joueur, une copie de l'état du jeu est générée et c'est elle qui opère les changements dus au movement. 
Le nouvel garde en mémoire l'état duquel il est copié. Utile pour revenir en arrière.

-Representation:
Chaque état contient la grille des cases, sous forme d'une liste d'entiers.
Les entiers contenus dans cette grille sont des instances de 'Flags' qui descend de la classe 'IntFlags' de Python.
'IntFlags' nous facilite le travail pour traiter nos entiers comme des masks de bits.
Chaque valeur de 'Flags' correspond à ce qui peut se trouver dans une case: 13 mots, et 6 objets. 
Les bitmasks permettent plusieurs mots et objets par case.

-Lois:
--Lois persistentes:
Les lois d'un état sont gardés dans une liste 'rules' qui compte un bitmask pour chaque objet.
Chaque bitmask contient les propriétés énoncées par les lois immédiatement visibles concernant son objet.
Par exemple si "ROCK IS SOLID" est visible dans le niveau, le bitmask correspondant à 'ROCK' dans 'rules' a son bit 'SOLID' marqué à 1.
Sitôt que "ROCK IS SOLID" n'est plus visible dans le niveau, le bit 'SOLID' du bitmask correspondant à 'ROCK' redevient 0.
--Lois instantanées:
Les lois changeant un objet en un autre sont définitives. 
Par exemple, sitôt que 'BABA IS FLAG' est visible, toutes les cases (qui sont des bitmasks) sont parcourus et pour chaque bit correspondant à 'baba' à 1, 
on le met à zéro et on met le bit correspondant à 'flag' à 1.
De cette manière partout où où il y avait l'objet 'baba' dans le niveau, à présent il y a l'objet 'flag'.

-Mouvements:
--Bouger:
Bouger dans BABA, c'est bouger tous les objets qu'une loi a désigné comme 'YOU' dans la direction du mouvement choisi.
Dans 'Flags', on a noté en majuscules les mots et en minuscules les objets.
Par exemple si la phrase "WALL IS YOU" formée des mots 'WALL', 'IS', 'YOU' est visible dans le niveau, les mouvements joueurs vont déplacer les objets de type 'wall'.
Déplacer un objet ('baba', 'rock', 'wall', 'flag', etc) d'une case courante à une case cible, c'est mettre à zéro le bit correspondant dans la case courante, et le mettre à 1 dans la case cible.
--Collisions:
Dans le cas d'une case cible contenant un ou des objets marqués comme 'PUSH', on appelle une méthode de poussée des objets 
qui parcourt récursivement les cases susceptibles de contenir d'autres objets marqués comme 'PUSH'. Si au bout de ce parcours on ne rencontre pas de condition d'arret
(ex: en dehors des limites de la grille, ou objet marqué comme 'SOLID' mais pas 'PUSH') on pousse tous ces objets. La récursivité de ce parcours nous permet de les pousser dans l'ordre opposé de déplacement et ainsi évitant le piétinement.
Si l'appel récursif de 'push' retourne True on déplace enfin la case qui a poussé les autres. Dans le cas d'un retour 'False', l'appel recursif a été annulé donc qui n'a rien bougé, on passe au YOU suivant.