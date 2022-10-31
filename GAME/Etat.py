from Codage import *


class Etat():
    def __init__(self, path):
        file = open(path, 'r')
        lines = file.readlines()
        file.close()
        self.changed = True
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
        self.getRules()


    def __str__(self):
        return self.logRules() + self.logEtat()
    

    def logRules(self):
        log = ""
        for i,flags in enumerate(self.rules):
            if flags != 0:
                log += Flags(1 << (i+first_obj)).name + " is " + str(flags) + "\n"
        return log
    

    def logEtat(self):
        log = ""
        for y in range(self.h):
            for x in range(self.w):
                log += self.grid[y][x].textcode() + " "
            log += '\n'
        return log


    def getRules(self):
        self.rules = 19*[0]
        for y in range(self.h):
            for x in range(self.w):
                if self.grid[y][x].hasflags(Flags.IS):
                    for dir in ((1,0), (0,1)):
                        if y-dir[0] >= 0 and y+dir[0] < self.h-1 and x-dir[1] >= 0 and x+dir[1] < self.w-1:

                            prefixe = self.grid[y-dir[0]][x-dir[1]]
                            suffixe = self.grid[y+dir[0]][x+dir[1]]

                            if prefixe != 0 and suffixe != 0:
                                for pref,i in prefixe.flags():
                                    if pref in words:
                                        for suf,_ in suffixe.flags():
                                            if suf in words:
                                                self.rules[i] |= suf


    def copy(self):
        return self


    def checkwin(self):
        return False    
    

    def checkdefeat(self):
        return False
    

    def isInBounds(self, j, i):
        return j>=0 and j<self.h and i>=0 and i<self.w


    def move(self, dir):
        self = self.copy()
        for y in range(self.h):
            for x in range(self.w):                
                # parcours dans le sens contraire du déplacement pour éviter le piétinement du mouvement des valeurs
                y1,x1 = y,x
                if dir[0] > 0:
                    y1 = self.h-y-1
                if dir[1] > 0:
                    x1 = self.w-x-1                    
                y2 = y1 + dir[0]
                x2 = x1 + dir[1]
                
                if self.isInBounds(y2, x2):
                    mask = self.grid[y1][x1]
                    mask2 = self.grid[y2][x2]

                    if mask != 0:                     
                        move = True

                        # collision
                        for flag,_ in mask2.flags():
                            if flag in obj2rule:
                                rule = self.rules[obj2rule[flag]]
                                if rule & Flags.SOLID and not rule & Flags.PUSH:
                                    move = False
                                    break
                        
                        if move:
                            # push
                            for flag2,_ in mask2.flags():
                                if flag2 in words or flag2 in obj2rule and self.rules[obj2rule[flag2]] & Flags.PUSH:
                                    def push():
                                        print("push: " + flag2.name + " in dir:", dir)
                                        return True
                                    move &= push()
                            
                            # move
                            if move: # move
                                for flag,i in mask.flags():
                                    if flag in obj2rule:
                                        if self.rules[obj2rule[flag]] & Flags.YOU:
                                            self.grid[y2][x2] |= flag
                                            self.grid[y1][x1] &= ~flag
                                            self.changed = True
                                    
        if self.changed:
            self.getRules()
        
        return self