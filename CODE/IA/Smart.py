
from CORE.Data import BABAf
from CORE.Etat import Etat
from IA.EtatIA import EtatIA
from UTIL.Util import *


def getDistances(etatIA:EtatIA, cibles, onCell=None):
    distances = etatIA.count*[MAX_INT]
    depth = 0
    courants = cibles
    reachables = BABAf(0)
    while len(courants) != 0:
        # ouverts
        suivants = set()
        # parcours des départs (wins)
        for ouvert in courants:
            if distances[ouvert.i] == MAX_INT:
                distances[ouvert.i] = depth
                # si pas de collision, parcours et ajout des voisins aux prochaines cases à parcourir dans un ensemble pour éviter duplicat
                flags = etatIA.grid[ouvert.i]
                if flags & etatIA.m_cols == 0:
                    for dir in Etat.yxi_dirs:
                        suivant = ouvert+dir
                        if etatIA.isInBounds(suivant) and distances[suivant.i] == MAX_INT:
                            suivants.add(suivant)
                    reachables |= flags
                    if onCell:
                        onCell(ouvert, etatIA.grid[ouvert.i])
        depth += 1
        courants = suivants
    return distances, reachables