from Codage import *


class Etat():
    def __init__(self, path):
        file = open(path, 'r')
        lines = file.readlines()
        file.close()
        self.h = len(lines)
        self.grid = []
        for j in range(self.h):
            splits = lines[j].split(' ')
            self.w = len(splits)
            l = []
            for i in range(self.w):
                if splits[i].startswith(".."):
                    l.append(Flags(0))
                else:
                    l.append(Flags(1 << int(splits[i])))
            self.grid.append(l)
        self.rules = set()
        self.getRules()


    def __str__(self):
        log = ""
        for y in range(self.h):
            for x in range(self.w):
                log += self.grid[y][x].textcode() + " "
            log += '\n'
        return log


    def getRules(self):
        self.rules.clear()
        for j in range(self.h):
            for i in range(self.w):
                if self.grid[j][i].hasflags(Flags.IS):
                    for dir in ((1,0), (0,1)):
                        if j-dir[0] >= 0 and j+dir[0] < self.h-1 and i-dir[1] >= 0 and i+dir[1] < self.w-1:
                            prefixe = self.grid[j-dir[0]][i-dir[1]]
                            suffixe = self.grid[j+dir[0]][i+dir[1]]
                            if ruleFlags.hasmask(prefixe | suffixe):
                                self.rules.add((prefixe, suffixe))


    def copy(self):
        return self


    def checkwin(self):
        return False    
    

    def isInBounds(self,pos):
        return pos[0]>=0 and pos[0]<self.h and pos[1]>=0 and pos[1]<self.w


    def move(self, dir):
        self = self.copy()
        for j in range(self.h):
            for i in range(self.w):

                # parcours dans le sens contraire de déplacement pour éviter piétinement d'assignation de cases
                j_,i_ = j,i
                if dir[0] > 0:
                    j_ = self.h-j-1
                if dir[1] > 0:
                    i_ = self.w-i-1
                pos2 = [j_+dir[0],i_+dir[1]]
                
                if self.isInBounds(pos2):
                    mask = self.grid[j_][i_]
                    mask2 = self.grid[pos2[0]][pos2[1]]

                    for flag in obj2rule:
                        if mask.hasflags(Flags(flag.value)) and (obj2rule[flag],Flags.YOU) in self.rules:
                            if mask2 == Flags.empty:
                                self.grid[pos2[0]][pos2[1]] |= flag
                                self.grid[j_][i_] &= ~flag
        self.getRules()
        return self