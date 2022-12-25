from CORE.Data import *


def deplace(self, flag, k, dir_i):
    self.grid[k] &= ~flag
    self.grid[k+dir_i] |= flag
    self.changed = True


def push(self, pos, dir):
    flags = self.grid[pos.i]
    if flags != 0:
        obstacles = False
        # détecter obstacle non déplaçable
        for i,_ in flags.flags(0, BABAb.last_all):
            if i < BABAb.first_obj:  # words
                obstacles = True
                self.needRules = True
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
            self.needPaths = False
            for _,flag in flags.flags(0, BABAb.last_all):
                deplace(self, flag, pos.i, dir.i)
    return True


def move(self, dir):    
    self.needRules = False
    self.needPaths = False
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
    if self.needRules:
        self.getRules()
        self.checkWinDefeat()