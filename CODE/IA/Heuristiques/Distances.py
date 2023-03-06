
from CORE.Etat import *
from IA.EtatIA import *


intInf = 1 << 32 - 1

def getDistances(etatIA:EtatIA):
    etatIA.m_get &= ~GETf.getPaths
    distances = etatIA.count*[intInf]
    depth = 0
    courants = etatIA.wins
    while len(courants)!=0:
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