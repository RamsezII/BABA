import Etat


class EtatIA(Etat.Etat):
    def __init__(self):
        self.parent = None
    

    def getDistances(self):
        self.distances = self.width*self.height*(int('inf'))
        for win in self.wins:
            while True:
                for k,flags in enumerate(self.grid):
                    for dir in self.dirs:
                        