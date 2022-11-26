import genericpath
import os
import Etat


WDIR = os.path.dirname(os.path.abspath(__file__))
up_right_down_left = [(0,-1),(1,0),(0,1),(-1,0)]


class Main():
    def __init__(self, levelpath):
        if not genericpath.isfile(levelpath):
            self.running = False
        else:
            file = open(levelpath, 'r')
            lines = file.readlines()
            file.close()
            self.etat = Etat.Etat()
            self.etat.readtext(lines)
            self.etats = []
            self.running = True
    
    
    def move(self, dir):
        etat = self.etat
        self.etats.append(etat)
        etat = etat.clone()
        if etat.move(dir):
            self.etat = etat
        else:
            self.etats.pop()
        return self.etat.changed
    

    def apply(self, etat):
        self.etats.append(self.etat)
        self.etat = etat
    

    def rewind(self):
        if len(self.etats) != 0:
            self.etat = self.etats.pop()
            self.etat.changed = True
        return self.etat.changed
    

    def successeurs(self):
        succ = []
        for dir in up_right_down_left:
            etat = self.etat.clone()
            if etat.move(dir):
                succ.append(etat)
        return succ


if __name__ == "__main__":
    print("FIN")