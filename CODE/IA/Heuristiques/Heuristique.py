import math

from CORE.Etat import *
from IA.EtatIA import *
import IA.Heuristiques.WinClair as WinClair
# import IA.Heuristiques.WinPresqueClair as WinPresqueClair
import IA.Heuristiques.WPC_test as WinPresqueClair
from UTIL.Util import *

def heuristique(etatIA:EtatIA):

    value = MAX_INT

    # wins clairs
    if len(etatIA.wins) != 0:
        value = WinClair.heuristique(etatIA)
        if value < MAX_INT:
            return value

    else:
        # wins presque clairs
        value = WinPresqueClair.heuristique(etatIA)
        if value < MAX_INT:
            return value

        # enfermé avec une seule loi?

        # sinon impossible de jauger état
        else:
            return math.inf