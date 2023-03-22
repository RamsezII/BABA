
from IA.EtatIA import *
import IA.Smart as Smart
from UTIL.Util import *

reachables = BABAf(0)


def heuristique(etatIA:EtatIA):    
    value = MAX_INT

    if GETf.getDistYou in etatIA.refreshMask:
        global reachables
        etatIA.distances_you, reachables = Smart.getDistances(etatIA, etatIA.yous)

    for pair in pairs:
        if pair[0] in reachables and pair[1] in reachables:
            # you->WIN + WIN->IS + 2 * IS->win

            break
        
    etatIA.refreshMask &= ~GETf.getDistYou
    return value