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
        for rule in self.rules:
            log += rule[0].name + " is " + rule[1].name + "\n"
        for y in range(self.h):
            for x in range(self.w):
                log += self.grid[y][x].textcode() + " "
            log += '\n'
        return log


    def getRules(self):
        self.rules = {
            (Flags.WALL, Flags.SOLID)
        }
        for j in range(self.h):
            for i in range(self.w):
                if self.grid[j][i].hasflags(Flags.IS):
                    for dir in ((1,0), (0,1)):
                        if j-dir[0] >= 0 and j+dir[0] < self.h-1 and i-dir[1] >= 0 and i+dir[1] < self.w-1:
                            prefixe = self.grid[j-dir[0]][i-dir[1]]
                            suffixe = self.grid[j+dir[0]][i+dir[1]]
                            if prefixe != 0 and suffixe != 0 and ruleFlags.hasmask(prefixe | suffixe):
                                self.rules.add((prefixe, suffixe))


    def copy(self):
        return self


    def checkwin(self):
        return False    
    

    def isInBounds(self, j, i):
        return j>=0 and j<self.h and i>=0 and i<self.w


    def move(self, dir):
        self = self.copy()
        changed = False
        for j in range(self.h):
            for i in range(self.w):

                def move(j1, i1):
                    changed = False
                    j2 = j1 + dir[0]
                    i2 = i1 + dir[1]
                    
                    if self.isInBounds(j2, i2):
                        mask = self.grid[j1][i1]
                        mask2 = self.grid[j2][i2]
                        
                        for flag in mask.flags():
                            if flag in obj2rule and (obj2rule[flag], Flags.YOU) in self.rules:
                                if mask2 == Flags.empty:
                                    self.grid[j2][i2] |= flag
                                    self.grid[j1][i1] &= ~flag
                                    self.getRules()
                                    changed = True
                    return changed
                
                # parcours dans le sens contraire du déplacement pour éviter le piétinement du mouvement des valeurs
                j1,i1 = j,i
                if dir[0] > 0:
                    j1 = self.h-j-1
                if dir[1] > 0:
                    i1 = self.w-i-1

                changed |= move(j1, i1)

        return self, changed