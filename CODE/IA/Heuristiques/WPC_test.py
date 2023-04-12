
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



def heuristique_OLD_OLD(etatIA:EtatIA):    
    value = MAX_INT

    # test 1, pousser FLAG vers flag, deux objets qui sont présents dans le niveau IA_lvl_01.txt

    if BABAf.FLAG in etatIA.reachables and BABAf.flag in etatIA.reachables:
        pos_target = etatIA.reachables[BABAf.flag][0]
        dists_target = Distances.getDistances(etatIA, pos_target)
        pos_pushed = etatIA.reachables[BABAf.FLAG][0]

        heur_pushed_up = Distances.getDistance(dists_target, pos_pushed+YXI(-1,0,0))
        heur_pushed_down = Distances.getDistance(dists_target, pos_pushed+YXI(1,0,0))
        heur_pushed_left = Distances.getDistance(dists_target, pos_pushed+YXI(0,-1,0))
        heur_pushed_right = Distances.getDistance(dists_target, pos_pushed+YXI(0,1,0))
        heur_pushed = min(heur_pushed_up, heur_pushed_down, heur_pushed_left, heur_pushed_right)

        
        
    return value



def heuristique_OLD(etatIA:EtatIA):    
    value = MAX_INT

    # test 1, pousser FLAG vers flag, deux objets qui sont présents dans le niveau IA_lvl_01.txt

    if BABAf.WIN in etatIA.reachables:
        for win in etatIA.reachables[BABAf.WIN]:
            
            for word in etatIA.reachables:
                if word in word2rule and word2obj[word] in etatIA.reachables:
                    print(True)

                    break
        
    return value