import math

from IA.EtatIA import EtatIA
import IA.Heuristiques.WinClair
import IA.Heuristiques.WinPresqueClair
    

def heuristique(self:EtatIA):
    if len(self.wins) != 0:
        self.eur = IA.Heuristiques.WinClair.heuristique_moy(self)
    elif IA.Heuristiques.WinPresqueClair.eligible(self):
        self.eur = IA.Heuristiques.WinPresqueClair.heuristique(self)
    else:
        self.eur = math.inf
    return self.eur