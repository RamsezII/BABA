
from CORE.Data import *
import CORE.Etat
from CORE.Etat import Etat
from IA.EtatIA import EtatIA
from UTIL.Util import *
from UTIL.YXI import *


def getDistance(distances:list, pos:YXI):
    if CORE.Etat.isInBounds(pos):
        return distances[pos.i]
    return MAX_INT


def getMinDistance(distances:list, pos):
    dist = MAX_INT
    for p in pos:
        dist = min(dist, getDistance(distances, p))
    return dist
    

def getDistances(etatIA:EtatIA, targets):
    if not isinstance(targets, int):
        targets = tuple(targets)
    if targets not in etatIA.distances:
        calculDistances(etatIA, targets)
    return etatIA.distances[targets]


def smartDistances(etatIA:EtatIA):
    if BABAf.YOU in etatIA.distances:
        return etatIA.distances[BABAf.YOU]
    
    etatIA.reachables = {}
    distances = etatIA.distYous = etatIA.distances[BABAf.YOU] = etatIA.count*[MAX_INT]
    depth = 0
    courants = etatIA.yous
    while len(courants) != 0:
        # ouverts
        suivants = []
        # parcours des départs (wins)
        for ouvert in courants:
            if distances[ouvert.i] == MAX_INT:
                distances[ouvert.i] = depth
                # si pas de collision, parcours et ajout des voisins aux prochaines cases à parcourir dans un ensemble pour éviter duplicat
                flags = etatIA.grid[ouvert.i]
                if flags & etatIA.m_cols == 0:
                    for dir in Etat.yxi_dirs:
                        suivant = ouvert+dir
                        if CORE.Etat.isInBounds(suivant) and distances[suivant.i] == MAX_INT:
                            suivants.append(suivant)
                    for _,f in flags.flags(0, BABAb.last_all):
                        if f in etatIA.reachables:
                            etatIA.reachables[f].append(ouvert)
                        else:
                            etatIA.reachables[f] = [ouvert]
        depth += 1
        courants = suivants
    return distances


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
                if flags & etatIA.m_cols == 0:
                    for dir in Etat.yxi_dirs:
                        suivant = CORE.Etat.i2yxi(ouvert)+dir
                        if CORE.Etat.isInBounds(suivant) and distances[suivant.i] == MAX_INT:
                            suivants.append(suivant.i)
        depth += 1
        courants = suivants
    return distances
