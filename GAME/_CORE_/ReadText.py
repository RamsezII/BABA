import _CORE_.GetRules
import _CORE_.CheckWinDefeat
from _CORE_.Data import *


def readtext(self, lines):
    self.h = len(lines)
    self.grid = []
    for j in range(self.h):
        splits = lines[j].split(' ')
        self.w = len(splits)
        for i in range(self.w):
            if splits[i].startswith(".."):
                self.grid.append(BABAf.none)
            else:
                self.grid.append(BABAf(1 << int(splits[i])))
    self.count = self.h*self.w
    self.dirs_i = (-self.h,1,self.h,-1)
    self.dirs_yx = ((-1,0),(0,1),(1,0),(-1,0))
    self.dirs_iyx = ((-self.h,(-1,0)), (1,(0,1)), (self.h,(1,0)), (-1,(0,-1)))
    self.eur = 0
    self.yous = []
    self.wins = set()
    _CORE_.GetRules.getRules(self)
    _CORE_.CheckWinDefeat.checkWinDefeat(self)