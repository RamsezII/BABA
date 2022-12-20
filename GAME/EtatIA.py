import Etat


class EtatIA(Etat.Etat):
    def __init__(self):
        self.parent = None
    

    def getDistances(self):
        self.distances = self.width*self.height*(int('inf'))