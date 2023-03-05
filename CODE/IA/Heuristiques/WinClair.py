import math
from IA.EtatIA import EtatIA
import sortedcontainers.sortedset


def heuristique_min(self:EtatIA):
    dist = math.inf
    for you in self.yous:
        dist = min(dist, self.dists[you.pos.i])
    return dist


def heuristique_moy(self:EtatIA):
    dists = sortedcontainers.sortedset.SortedSet()
    for you in self.yous:
        dists.add(self.dists[you.pos.i])
    count = len(dists)    
    man = 0
    for i,dist in enumerate(dists):
        man += dist * (count-i)
    man /= count*(count+1)/2    
    return man
