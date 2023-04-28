
from CORE.Etat import *
from UTIL.Util import *

class EtatIA(Etat):
    def __init__(self, levelname):
        super().__init__(levelname)
        self.cout = 0
        self.heur = MAX_INT
        self.reachables:dict = {}
        self.distances:dict = {}
        self.distYous:list


    def __lt__(self, other):
        return self.heur < other.heur

    def __le__(self, other):
        return self.heur <= other.heur

    def __gt__(self, other):
        return self.heur > other.heur

    def __ge__(self, other):
        return self.heur >= other.heur

    def __ne__(self, other):
        return self.heur != other.heur
    

    def getLawTree(self):
        pass



"""
- ARBRE DES LOIS : 
    recherche d'un etat avec WIN clair et geographiquement atteignable

- quels mots peuvent bouger, quelles lois peuvent changer
    - possible que pour la racine...

- generer l'arbre des lois en largeur sans reevaluer de combinaison
    - 
"""
