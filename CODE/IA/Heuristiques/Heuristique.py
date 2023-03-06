import math

import IA.Heuristiques.WinClair as WinClair
import IA.Heuristiques.WinPresqueClair as WinPresqueClair
    

def heuristique(self):
    if len(self.wins) != 0:
        value = WinClair.heuristique_moy(self)
    elif WinPresqueClair.eligible(self):
        value = WinPresqueClair.heuristique(self)
    else:
        value = math.inf
    return value