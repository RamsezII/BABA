import math

from CORE.Etat import *
from IA.EtatIA import *
import IA.Heuristiques.WinClair as WinClair
import IA.Heuristiques.WinPresqueClair as WinPresqueClair
    

distances:list[int]

def heuristique(etatIA:EtatIA):
    if etatIA.refreshMask & GETf.getPaths:
        etatIA.refreshMask &= ~GETf.getPaths
        calculations(etatIA)
    if len(etatIA.wins) != 0:
        value = WinClair.heuristique_moy(etatIA, distances)
    elif WinPresqueClair.eligible(etatIA, distances):
        value = WinPresqueClair.heuristique(etatIA, distances)
    else:
        value = math.inf
    return value


def calculations(etatIA:EtatIA):
    intInf = 1 << 32 - 1
    etatIA.refreshMask &= ~GETf.getPaths
    global distances
    distances = etatIA.count*[intInf]
    depth = 0
    courants = etatIA.wins
    while len(courants) != 0:
        # ouverts
        suivants = set()
        # parcours des départs (wins)
        for ouvert in courants:
            if distances[ouvert.i] == intInf:
                distances[ouvert.i] = depth
                # si pas de collision, parcours et ajout des voisins aux prochaines cases à parcourir dans un ensemble pour éviter duplicat
                if etatIA.grid[ouvert.i] & etatIA.m_cols == 0:
                    for dir in Etat.yxi_dirs:
                        suivant = ouvert+dir
                        if etatIA.isInBounds(suivant) and distances[suivant.i] == intInf:
                            suivants.add(suivant)
        depth += 1
        courants = suivants
    return distances