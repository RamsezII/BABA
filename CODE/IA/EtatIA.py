import math

from CORE.Etat import *

class EtatIA(Etat):
    def __init__(self, levelname):
        super().__init__(levelname)
        self.eur = math.inf
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
            print("{} | {}".format(you, self.dists[you.pos.i]))


    def getDistances(self):
        self.m_get &= ~GETf.getPaths
        self.dists = self.count*[math.inf]
        depth = 0
        nexts = self.wins.copy()
        while len(nexts)!=0:
            nexts2 = set()
            for n in nexts:
                if self.dists[n.i] == math.inf:
                    self.dists[n.i] = depth
                    if self.grid[n.i] & self.m_cols == 0:
                        for dir in Etat.yxi_dirs:
                            n2 = n+dir
                            if self.isInBounds(n2) and self.dists[n2.i] == math.inf:
                                nexts2.add(n2)
            depth += 1
            nexts = nexts2


    def getDistances_OLD(self):
        self.dists = self.count*[math.inf]
        for win in self.wins:
            visits = self.count*[False]
            visits[win.i] = True
            depth = 0
            nexts = set()
            nexts.add(win.i)
            while len(nexts)!=0:
                nexts2 = set()
                for n in nexts:
                    if self.grid[n] & self.m_cols:
                        self.dists[n] = -1
                    else:
                        self.dists[n] = min(depth, self.dists[n])
                        for dir in Etat.yxi_dirs:
                            if self.isInBounds(win+dir):
                                n2 = n+dir.i
                                if not visits[n2]:
                                    nexts2.add(n+dir.i)
                                    visits[n2] = True
                depth += 1
                nexts = nexts2


"""
 -  getDistances:
     -  ouverts
     -  fermes
     -  sommet de depart
     -  parcours des fils (directions):
         -  si collision:
             -  marqué -1
         -  sinon, si jamais parcouru:
             -  ajouté à ouverts
"""