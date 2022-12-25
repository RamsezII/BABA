from CORE.Data import *
from CORE.Etat import GETf


def deplace(self, flag, k, dir_i):
    self.grid[k] &= ~flag
    self.grid[k+dir_i] |= flag
    self.changed = True


def push(self, pos, dir):
    flags = self.grid[pos.i]
    if flags != 0:
        self.m_get |= GETf.getPaths
        obstacles = False
        # détecter obstacle non déplaçable
        for i,_ in flags.flags(0, BABAb.last_all):
            if i < BABAb.first_obj:  # words
                obstacles = True
                self.m_get |= GETf.getRules
            else:  # objects
                rule = self.rules[i-BABAb.first_obj]
                if rule & BABAf.PUSH:
                    obstacles = True
                elif rule & BABAf.SOLID:
                    return False                                                                                        
        if obstacles:                                        
            # récursivité pour éviter piétinement (push des cases suivantes avant push immédiat)
            pos2 = pos+dir
            if not self.isInBounds(pos2) or not push(self, pos2, dir):
                return False                
            # pousser cette case (donc recalcul des chemins)
            for _,flag in flags.flags(0, BABAb.last_all):
                deplace(self, flag, pos.i, dir.i)
    return True


def move(self, dir):
    self.m_get = GETf.none
    self.dir = dir
    count = len(self.yous)
    for k in range(count):
        # inverser ordre de parcours selon sens de deplacement
        if dir.i > 0:
            you = self.yous[count-k-1]
        else:
            you = self.yous[k]
        if self.isInBounds(you.pos+dir) and push(self, you.pos+dir, dir):
            deplace(self, you.flag, you.pos.i, dir.i)
            self.m_get |= GETf.getYous | GETf.getWins
    if self.m_get & GETf.getRules:
        self.getRules()
    if self.m_get & GETf.getWins:
        self.checkWinDefeat()
    if self.m_get & GETf.getYous:
        self.getYous()