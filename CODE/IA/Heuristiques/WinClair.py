
import sortedcontainers.sortedset

from CORE.Etat import *
from IA.EtatIA import *
import IA.Distances as Distances
from UTIL.Util import *


def heuristique(etatIA:EtatIA):
    if len(etatIA.wins) > 0:
        distances = Distances.getDistances(etatIA, etatIA.wins)
        return heuristique_min(etatIA.yous, distances)
    return MAX_INT


def heuristique_min(yous, distances:list):
    dist = MAX_INT
    for you in yous:
        dist = min(dist, distances[you.i])
    return dist


def heuristique_moy(yous, distances:list):
    dists = sortedcontainers.sortedset.SortedSet()
    for you in yous:
        dists.add(distances[you.i])
    count = len(dists)    
    man = 0
    for i,dist in enumerate(dists):
        man += dist * (count-i)
    man /= count*(count+1)/2    
    return man
