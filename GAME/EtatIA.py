import Etat


class EtatIA(Etat.Etat):
    def __init__(self):
        self.parent = None
        self.dirs_yx = ((-1,0),(0,1),(1,0),(-1,0))
        self.dirs_i = (-self.height,1,self.height,-1)
        self.dirs_yxi = (((-1,0),-self.height), ((0,1),1), ((1,0),self.height), ((0,-1),-1))
    

    def getDistances(self):
        self.distances = self.width*self.height*(int('inf'))
        for win in self.wins:
            while True:
                for k,flags in enumerate(self.grid):
                    for dir in self.dirs:
                        