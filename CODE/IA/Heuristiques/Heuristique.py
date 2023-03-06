import math

from CORE.Etat import *
from IA.EtatIA import *
import IA.Heuristiques.WinClair as WinClair
import IA.Heuristiques.WinPresqueClair as WinPresqueClair
import IA.Heuristiques.Distances as Distances
    

dists:list[int]

def heuristique(etatIA:EtatIA):
    if etatIA.m_get & GETf.getPaths:
        etatIA.m_get &= ~GETf.getPaths
        global dists
        dists = Distances.getDistances(etatIA)
    if len(etatIA.wins) != 0:
        value = WinClair.heuristique_moy(etatIA, dists)
    elif WinPresqueClair.eligible(etatIA):
        value = WinPresqueClair.heuristique(etatIA, dists)
    else:
        value = math.inf
    return value