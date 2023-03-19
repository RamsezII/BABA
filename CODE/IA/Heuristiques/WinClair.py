import math

import sortedcontainers.sortedset

from CORE.Etat import *
from IA.EtatIA import *
from UTIL.Util import *
import IA.Smart as Smart


def heuristique(etatIA:EtatIA):
    if GETf.getDistWins in etatIA.refreshMask:
        etatIA.refreshMask &= ~GETf.getDistWins
        etatIA.distances_wins = Smart.getDistances(etatIA, etatIA.wins)
    
    for you in etatIA.yous:
        if etatIA.distances_wins[you.i] < MAX_INT:
            return heuristique_moy(etatIA)
    return MAX_INT


def heuristique_min(etatIA:EtatIA):
    dist = math.inf
    for you in etatIA.yous:
        dist = min(dist, etatIA.distances_wins[you.pos.i])
    return dist


def heuristique_moy(etatIA:EtatIA):
    dists = sortedcontainers.sortedset.SortedSet()
    for you in etatIA.yous:
        dists.add(etatIA.distances_wins[you.i])
    count = len(dists)    
    man = 0
    for i,dist in enumerate(dists):
        man += dist * (count-i)
    man /= count*(count+1)/2    
    return man
