
from IA.EtatIA import *
import IA.Smart as Smart
from UTIL.Util import *


reachables = BABAf(0)

def heuristique(etatIA:EtatIA):    
    value = MAX_INT

    if GETf.getDistYou in etatIA.refreshMask:
        global reachables
        etatIA.distances_you, reachables = Smart.getDistances(etatIA, etatIA.yous)

    if reachables:
        for pair in pairs:
            if pair[0] in reachables and pair[1] in reachables:
                # value = distance(you->WIN + WIN->IS + 2 * IS->win)

                word = pair[0]
                obj = pair[1]


                break
        
    etatIA.refreshMask &= ~GETf.getDistYou
    return value