import math

import Etat


class EtatIA(Etat.Etat):
    def __init__(self):
        self.parent = None
        self.getDistances()

    def getDistances(self):
        self.dists = self.count*[math.inf]
        for win in self.wins:
            visits = self.count*[False]
            visits[win] = True
            dist = 0
            nexts = set(win)
            while len(nexts)!=0:
                nexts2 = set()
                for n in nexts:
                    if self.grid[n] & self.m_cols:
                        self.dists[n] = -1
                    else:
                        self.dists[n] = math.min(dist, self.dists[n])
                        y,x = i//self.h, i%self.w
                        for dir in self.dirs_iyx:
                            if self.isInBounds_yx(y+dir[1][0], x+dir[1][1]):
                                n2 = n+dir[0]
                                if not visits[n2]:
                                    nexts2.add(n+dir[0])
                dist += 1
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