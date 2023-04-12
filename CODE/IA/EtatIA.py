import math

from CORE.Etat import *

class EtatIA(Etat):
    def __init__(self, levelname):
        super().__init__(levelname)
        self.eur = math.inf
        self.cout = 0
        self.reachables:dict = {}
        self.distances:dict = {}


    def __lt__(self, other):
        return self.eur < other.eur

    def __le__(self, other):
        return self.eur <= other.eur

    def __gt__(self, other):
        return self.eur > other.eur

    def __ge__(self, other):
        return self.eur >= other.eur

    def __ne__(self, other):
        return self.eur != other.eur
    

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
