import CODE.Etat
from CODE.Data import *
    

def deplace(self, flag, k, dir):
    self.grid[k] &= ~flag
    self.grid[k+dir] |= flag
    self.changed = True


def push(self, k, dir):
    mask2 = self.grid[k]
    if mask2 != 0:
        obstacles = False
        # détecter obstacle non déplaçable
        for i2,flag2 in mask2.flags(0, BABAb.last_all):
            if i2 < BABAb.first_obj:  # words
                obstacles = True
            else:  # objects
                rule = self.rules[i2-BABAb.first_obj]
                if rule & BABAf.PUSH:
                    obstacles = True
                elif rule & BABAf.SOLID:
                    return False                                                                                        
        if obstacles:                                        
            # récursivité pour éviter piétinement (push des cases suivantes avant push immédiat)
            k2 = k+dir
            if not self.isInBounds(k2) or not push(self, k2, dir):
                return False                
            # pousser cette case
            for i2,flag2 in mask2.flags(0, BABAb.last_all):
                deplace(self, flag2, k, dir)
    return True


def move(self, dir):
    self.dir = dir

    if dir == 1:
        dir = -self.w
    elif dir == 2:
        dir = 1
    elif dir == 3:
        dir = self.w
    elif dir == 4:
        dir = -1
    else:
        print("ERROR: " + str(dir))
        
    count = len(self.yous)
    for k in range(count):
        # inverser ordre de parcours selon sens de deplacement
        if dir > 0:
            you = self.yous[count-k-1]
        else:
            you = self.yous[k]
        k_ = you[0]
        if self.isInBounds(k_+dir) and push(self, k_+dir, dir):
            deplace(self, you[1],k_, dir)
    CODE.GetRules.getRules(self)
    CODE.CheckWinDefeat.checkWinDefeat(self)