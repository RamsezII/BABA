import os.path
import time

import _CORE_.Etat
import _CORE_.Move
import _CORE_.ReadText

class Main():
    def __init__(self, levelname):
        levelpath = os.path.abspath(__file__)
        levelpath = os.path.dirname(levelpath)
        levelpath = os.path.dirname(levelpath)
        levelpath = os.path.dirname(levelpath)
        levelpath = os.path.join(levelpath, "levels")
        levelpath = os.path.join(levelpath, levelname)
        file = open(levelpath, 'r')
        lines = file.readlines()
        file.close()
        self.etat = _CORE_.Etat.Etat()
        _CORE_.ReadText.readtext(self.etat, lines)
        self.etats = []
        self.tried = [self.etat]
        self.running = True
        self.changed = True
    
    
    def move(self, dir):
        etat = self.etat
        self.etats.append(etat)
        etat = etat.clone()
        _CORE_.Move.move(etat,dir)
        if etat == self.etat:
            self.etats.pop()
        else:
            self.etat = etat
            self.tried.append(etat)
            self.changed = True
        return self.changed
    

    def apply(self, etat):
        self.etats.append(self.etat)
        self.etat = etat
        self.tried.append(etat)
        self.changed = True
    

    def rewind(self):
        if len(self.etats) != 0:
            self.etat = self.etats.pop()
            self.changed = True
        return self.changed
    

    def successeurs(self):
        succs = []
        for dir in range(1, 5):
            etat = self.etat.clone()
            etat.move(dir)
            if etat != self.etat and etat not in self.tried:
                succs.append(etat)
        return succs


if __name__ == "__main__":
    print("FIN")