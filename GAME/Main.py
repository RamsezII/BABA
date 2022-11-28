import os.path

import Etat


up_right_down_left = [(0,-1),(1,0),(0,1),(-1,0)]


class Main():
    def __init__(self, levelname):
        file = open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "levels", levelname), 'r')
        lines = file.readlines()
        file.close()
        self.etat = Etat.Etat()
        self.etat.readtext(lines)
        self.etats = []
        self.tried = [self.etat]
        self.running = True
        self.changed = True
    
    
    def move(self, dir):
        etat = self.etat
        self.etats.append(etat)
        etat = etat.clone()
        etat.move(dir)
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
        succ = []
        for dir in up_right_down_left:
            etat = self.etat.clone()
            etat.move(dir)
            if etat != self.etat and etat not in self.tried:
                print("succs:", dir)
                succ.append(etat)
        print()
        return succ


if __name__ == "__main__":
    print("FIN")