
from CORE.Data import *
from IA.EtatIA import *
import IA.Distances as Distances
from UTIL.Util import *


def heuristique(etatIA:EtatIA):    
    value = MAX_INT

    # test 1, pousser FLAG vers flag, deux objets qui sont présents dans le niveau IA_lvl_01.txt

    if BABAf.FLAG in etatIA.reachables and BABAf.flag in etatIA.reachables:
        pos_target = etatIA.reachables[BABAf.flag][0]
        dists_target = Distances.getDistances(etatIA, pos_target.i)
        pos_pushed = etatIA.reachables[BABAf.FLAG][0]
        dist_pushed = Distances.getDistances(etatIA, pos_pushed.i)

        dist_yous = MAX_INT
        for you in etatIA.yous:
            dist_yous = min(dist_yous, Distances.getDistance(dist_pushed, you))
        
        value = dist_yous + Distances.getDistance(dists_target, pos_pushed)
        
    return value

