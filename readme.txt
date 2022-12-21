lancer GAME/Main_UI.py
( besoin de pygame )

ZQSD - mouvement
R - rewind
P - revenir dans le terminal (pasfini)


A chaque mouvement valide du joueur, une copie de l'état du jeu est empilée sur une liste. 
C'est cette liste qu'on utilise pour revenir en arrière.

-Representation:
Chaque état contient la grille des cases, sous forme d'une liste à deux dimensions d'entiers.
Les entiers contenus dans cette grille sont des instances de 'Flags' qui descend de la classe 'IntFlags' de Python.
'IntFlags' nous facilite le travail pour traiter nos entiers comme des masks de bits.
Chaque valeur de 'Flags' correspond à ce qui peut se trouver dans une case: 13 mots, et 6 objets. 
Les bitmasks permettent plusieurs mots et objets par case.

-Lois:
--Lois persistentes:
Les lois d'un état sont gardés dans une liste 'rules' qui compte un bitmask pour chaque objet.
Chaque bitmask contient les propriétés énoncées par les lois immédiatement visibles concernant son objet.
Par exemple si "ROCK IS SOLID" est visible dans le niveau, le bitmask correspondant à 'ROCK' dans 'rules' a son bit 'SOLID' marqué à 1.
Sitôt que "ROCK IS SOLID" n'est plus visible dans le niveau, le bit 'SOLID' du bitmask correspondant à 'ROCK' est marqué à 0.
--Lois instantanées:
Les lois changeant un objet en un autre sont définitives. 
Par exemple, sitôt que 'BABA IS FLAG' est visible, toutes les cases (qui sont des bitmasks) sont parcourus et pour chaque bit correspondant à 'baba' à 1, 
on le met à zéro et on met le bit correspondant à 'flag' à 1.
De cette manière partout où où il y avait l'objet 'baba' dans le niveau, à présent il y a l'objet 'flag'.

-Mouvements:
--Bouger:
Bouger dans BABA, c'est bouger tous les objets qu'une loi a désigné comme 'YOU' quelque part dans le niveau.
Dans 'Flags', on a noté en majuscules les mots et en minuscules les objets.
Par exemple si la phrase "WALL IS YOU" formée des mots 'WALL', 'IS', 'YOU' est visible dans le niveau, les mouvements joueurs vont déplacer les objets de type 'wall'.
Déplacer un objet ('baba', 'rock', 'wall', 'flag', etc) d'une case courante à une case cible, c'est mettre à zéro le bit correspondant dans la case courante, et le mettre à 1 dans la case cible.
--Collisions:
Dans le cas d'une case cible contenant un ou des objets marqués comme 'PUSH', on appelle une méthode de poussée des objets 
qui parcourt récursivement les cases susceptibles de contenir d'autres objets marqués comme 'PUSH'. Si au bout de ce parcours on ne rencontre pas de condition d'arret
(ex: en dehors des limites de la grille, ou objet marqué comme 'SOLID' mais pas 'PUSH') on pousse tous ces objets. La récursivité de ce parcours nous permet de les pousser dans l'ordre opposé de déplacement et ainsi évitant le piétinement.
Si l'appel récursif de 'push' retourne True on déplace enfin la case qui a poussé les autres.

-Fin:
--Victoire:
On gagne quand un objet marqué 'YOU' se trouve sur une case marquée 'WIN'.
--Défaite:
Une situation de blocage donc de défaite est une situation où aucun objet n'est marqué comme 'YOU' et donc nos actions n'ont plus de conséquences sur le jeu.