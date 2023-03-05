import math

from CORE.Etat import *

class EtatIA(Etat):
    def __init__(self, levelname):
        super().__init__(levelname)
        self.eur = math.inf
        self.cout = 0
        self.getDistances()


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


    def getDistances(self):
        self.m_get &= ~GETf.getPaths
        self.dists = self.count*[math.inf]
        depth = 0
        nexts = self.wins.copy()
        while len(nexts)!=0:
            # ouverts
            nexts2 = set()
            # parcours des départs (wins)
            for n in nexts:
                if self.dists[n.i] == math.inf:
                    self.dists[n.i] = depth
                    # si pas de collision, parcours et ajout des voisins aux prochaines cases à parcourir dans un ensemble pour éviter duplicat
                    if self.grid[n.i] & self.m_cols == 0:
                        for dir in Etat.yxi_dirs:
                            n2 = n+dir
                            if self.isInBounds(n2) and self.dists[n2.i] == math.inf:
                                nexts2.add(n2)
            depth += 1
            nexts = nexts2
    

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
