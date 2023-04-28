
from CORE.Etat import *
from IA.EtatIA import *
import IA.Distances as Distances
import IA.Heuristiques.WinClair as WinClair
import IA.Heuristiques.WinPresqueClair as WinPresqueClair
import IA.Heuristiques.Enfermement as Enfermement
from UTIL.Util import *

currentHeuristique = 0

def heuristique(etatIA:EtatIA)->int:
    global currentHeuristique
    
    Distances.smartDistances(etatIA)
    if len(etatIA.yous) == 0:
        return MAX_INT

    # wins clairs
    value = WinClair.heuristique(etatIA)
    if value < MAX_INT:
        if currentHeuristique != 1:
            print("win clair")
        currentHeuristique = 1
        return value

    else:
        # wins presque clairs
        value = WinPresqueClair.heuristique(etatIA)
        if value < MAX_INT:
            if currentHeuristique != 2:
                print("win presque clair")
            currentHeuristique = 2
            return value

        # enfermé avec une seule loi?
        value = Enfermement.heuristique(etatIA)
        if value < MAX_INT:
            if currentHeuristique != 3:
                print("enfermement")
            currentHeuristique = 3
            return value

    if currentHeuristique != 0:
        print("nope")
    currentHeuristique = 0

    # sinon impossible de jauger état    
    return MAX_INT