import time
from _CORE_.Data import *
import copy


class Etat():
    def __init__(self):
        self.changed = True
        self.win = False
        self.defeat = False
        self.parent = None
        self.dir = 0
        self.m_cols = BABAf.none
    

    def pullChange(self):
        if self.changed:
            self.changed = False
            return True
        else:
            return False
        

    def __lt__(self, other):
        return self.eur < other.eur

    def __le__(self, other):
        return self.eur <= other.eur

    def __gt__(self, other):
        return self.eur > other.eur

    def __ge__(self, other):
        return self.eur >= other.eur

    def __eq__(self, other):
        return self.eur == other.eur

    def __ne__(self, other):
        return self.eur != other.eur


    def isInBounds(self, k):
        return k >= 0 and k < self.count


    def clone(self):
        # eviter a 'deepcopy' de copier 'parent'
        parent = self.parent
        self.parent = None
        clone = copy.deepcopy(self)
        clone.parent = self.parent = parent
        return clone
    

    def __eq__(self, other):
        return self.grid == other.grid

        
    def logRules(self):
        log = ""
        for f,flags in enumerate(self.rules):
            if flags != 0:
                log += BABAf(1 << (f+BABAb.first_obj)).name + " is " + str(flags) + "\n"
        return log


    def logEtat(self):
        log = ""
        for k in range(self.count):
            log += self.grid[k].textcode() + " "
            if (k+1) % self.w == 0:
                log += '\n'
        return log
    

    def isInBounds_yx(self, y, x):
        return y>=0 and y<self.h and x>=0 and x<self.w


