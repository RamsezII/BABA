from CORE.Data import *
from CORE.Etat import *
import CORE.Etat


def deplace(self:Etat, flag, k, dir_i):
    self.grid[k] &= ~flag
    self.grid[k+dir_i] |= flag
    self.changed = True


def push(self:Etat, cell_pos, push_dir):
    cell_f = self.grid[cell_pos.i]
    if cell_f != 0:
        if self.distances:
            self.distances = {}
            self.reachables = {}
            self.distYous = None
        self.refreshMask |= GETf.getWins | GETf.getRules
        obstacles = False

        # détecter obstacle non déplaçable
        for _,f in cell_f.flags(0, BABAb.last_all):
            if f in self.rules[BABAf.PUSH]:
                obstacles = True
            elif BABAf.SOLID in self.rules and f in self.rules[BABAf.SOLID]:
                return False
                                                                                                  
        if obstacles:
            # récursivité pour éviter piétinement (push des cases suivantes avant push immédiat)
            pos2 = cell_pos+push_dir
            if not CORE.Etat.isInBounds(pos2) or not push(self, pos2, push_dir):
                return False                
            # pousser cette case (donc recalcul des chemins)
            for _,flag in cell_f.flags(0, BABAb.last_all):
                deplace(self, flag, cell_pos.i, push_dir.i)
    return True


def move(self:Etat, dir:YXI):
    self.dir = dir
    for you_i in range(len(self.yous)):
        # inverser ordre de parcours selon sens de deplacement
        if dir.i > 0:
            you = i2yxi(self.yous[-you_i-1])
        else:
            you = i2yxi(self.yous[you_i])
        if CORE.Etat.isInBounds(you+dir) and push(self, you+dir, dir):
            for _,flag in self.grid[you.i].flags(0, BABAb.last_all):
                if flag in self.rules[BABAf.YOU]:
                    deplace(self, flag, you.i, dir.i)
                    self.refreshMask |= GETf.getYous
    if self.refreshMask & GETf.getRules:
        self.refreshMask &= ~GETf.getRules
        self.getRules()
    if self.refreshMask & GETf.getWins:
        self.refreshMask &= ~(GETf.getWins | GETf.getYous)
        self.checkWinDefeat()
    if self.refreshMask & GETf.getYous:
        self.refreshMask &= ~GETf.getYous
        self.getYous()