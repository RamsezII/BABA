
from sortedcontainers.sortedlist import SortedList
from CORE.Data import *
import CORE.Etat
from CORE.Etat import *
from IA.EtatIA import EtatIA
from UTIL.Util import *
from UTIL.YXI import *



def getMinDistance(distances:list, pos):
    dist = MAX_INT
    for p in pos:
        dist = min(dist, distances[p])
    return dist
    

def getDistances(etatIA:EtatIA, targets):
    if not isinstance(targets, int):
        targets = tuple(targets)
    if targets not in etatIA.distances:
        calculDistances(etatIA, targets)
    return etatIA.distances[targets]


def smartDistances(etatIA:EtatIA):
    if BABAf.YOU not in etatIA.distances:
        etatIA.reachables = {}
        distances = etatIA.distances[BABAf.YOU] = etatIA.count*[MAX_INT]
        depth = 0
        courants = etatIA.yous
        while len(courants) != 0:
            # ouverts
            suivants = []
            # parcours des départs (wins)
            for ouvert in courants:
                if distances[ouvert] == MAX_INT:
                    distances[ouvert] = depth
                    # si pas de collision, parcours et ajout des voisins aux prochaines cases à parcourir dans un ensemble pour éviter duplicat
                    flags = etatIA.grid[ouvert]
                    if BABAf.SOLID not in etatIA.rules or not flags & etatIA.rules[BABAf.SOLID]:
                        for dir in Etat.yxi_dirs:
                            ouvert_yxi = CORE.Etat.i2yxi(ouvert)
                            suivant = ouvert_yxi+dir
                            if CORE.Etat.isInBounds(suivant) and distances[suivant.i] == MAX_INT:
                                suivants.append(suivant.i)
                        for _,f in flags.flags(0, BABAb.last_all):
                            if f not in etatIA.reachables:
                                etatIA.reachables[f] = SortedList()
                            etatIA.reachables[f].add(ouvert_yxi)
            depth += 1
            courants = suivants


def calculDistances(etatIA:EtatIA, targets):
    distances = etatIA.distances[targets] = etatIA.count*[MAX_INT]
    depth = 0

    if isinstance(targets, int):
        courants = [targets]
    else:
        courants = targets

    while len(courants) != 0:
        # ouverts
        suivants = []
        # parcours des départs (wins)
        for ouvert in courants:
            if distances[ouvert] == MAX_INT:
                distances[ouvert] = depth
                # si pas de collision, parcours et ajout des voisins aux prochaines cases à parcourir dans un ensemble pour éviter duplicat
                flags = etatIA.grid[ouvert]
                if BABAf.SOLID not in etatIA.rules or not flags & etatIA.rules[BABAf.SOLID]:
                    for dir in Etat.yxi_dirs:
                        suivant = CORE.Etat.i2yxi(ouvert)+dir
                        if CORE.Etat.isInBounds(suivant) and distances[suivant.i] == MAX_INT:
                            suivants.append(suivant.i)
        depth += 1
        courants = suivants
    return distances
