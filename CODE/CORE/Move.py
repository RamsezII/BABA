from CORE.Data import *
from CORE.Etat import *
import CORE.Etat


def deplace(self:Etat, flag, k, dir_i):
    self.grid[k] &= ~flag
    self.grid[k+dir_i] |= flag
    self.changed = True


def push(self:Etat, pos, dir):
    flags = self.grid[pos.i]
    if flags != 0:
        if self.distances:
            self.distances = {}
        obstacles = False
        # détecter obstacle non déplaçable
        for i,_ in flags.flags(0, BABAb.last_all):
            if i < BABAb.first_obj:  # words
                obstacles = True
                self.refreshMask |= GETf.getRules
            else:  # objects
                rule = self.rules[i-BABAb.first_obj]
                if rule & BABAf.PUSH:
                    obstacles = True
                elif rule & BABAf.SOLID:
                    return False                                                                                        
        if obstacles:                                        
            # récursivité pour éviter piétinement (push des cases suivantes avant push immédiat)
            pos2 = pos+dir
            if not CORE.Etat.isInBounds(pos2) or not push(self, pos2, dir):
                return False                
            # pousser cette case (donc recalcul des chemins)
            for _,flag in flags.flags(0, BABAb.last_all):
                deplace(self, flag, pos.i, dir.i)
    return True


def move(self:Etat, dir):
    self.dir = dir
    count = len(self.yous)
    for k in range(count):
        # inverser ordre de parcours selon sens de deplacement
        if dir.i > 0:
            you = self.yous[count-k-1]
        else:
            you = self.yous[k]
        if CORE.Etat.isInBounds(you+dir) and push(self, you+dir, dir):
            for flag in self.grid[you.i]:
                if flag in self.m_yous:
                    deplace(self, flag, you.i, dir.i)
                    self.refreshMask |= GETf.getYous | GETf.getWins
    if self.refreshMask & GETf.getRules:
        self.refreshMask &= ~GETf.getRules
        self.getRules()
    if self.refreshMask & GETf.getWins:
        self.refreshMask &= ~(GETf.getWins | GETf.getYous)
        self.checkWinDefeat()
    if self.refreshMask & GETf.getYous:
        self.refreshMask &= ~GETf.getYous
        self.getYous()