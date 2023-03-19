import math

from CORE.Etat import *

class EtatIA(Etat):
    def __init__(self, levelname):
        super().__init__(levelname)
        self.eur = math.inf
        self.cout = 0
        self.distances_wins:list[int]
        self.distances_you:list[int]
        self.refreshMask |= GETf.getDistWins | GETf.getDistYou


    def __lt__(self, other):
        return self.eur < other.eur

    def __le__(self, other):
        return self.eur <= other.eur

    def __gt__(self, other):
        return self.eur > other.eur

    def __ge__(self, other):
        return self.eur >= other.eur

    def __ne__(self, other):
        return self.eur != other.eur
    

    def logDistances(self):
        for j in range(Etat.h):
            log = ""
            for i in range(Etat.w):
                log += "{:^5}".format(self.dists[yx2yxi(j,i).i])
            print(log)
    

    def logYousDistances(self):
        for you in self.yous:
            print(you, '|', self.dists[you.pos.i])
    

    def getLawTree(self):
        pass



"""
- ARBRE DES LOIS : 
    recherche d'un etat avec WIN clair et geographiquement atteignable

- quels mots peuvent bouger, quelles lois peuvent changer
    - possible que pour la racine...

- generer l'arbre des lois en largeur sans reevaluer de combinaison
    - 
"""
