from Codage import *
import copy


class Etat():
    def init(self, path):
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


    def clone(self):
        return copy.deepcopy(self)


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
        self.rules = 6*[0]
        for y in range(self.h):
            for x in range(self.w):
                if self.grid[y][x].hasflags(Flags.IS):
                    for dir in ((1,0), (0,1)):
                        if y-dir[0] >= 0 and y+dir[0] < self.h-1 and x-dir[1] >= 0 and x+dir[1] < self.w-1:

                            prefixe = self.grid[y-dir[0]][x-dir[1]]
                            suffixe = self.grid[y+dir[0]][x+dir[1]]

                            if prefixe != 0 and suffixe != 0:
                                for pref,_ in prefixe.flags():
                                    if pref in word2obj:
                                        for suf,_ in suffixe.flags():
                                            if suf in words:
                                                self.rules[word2obj[pref]] |= suf


    def checkwin(self):
        return False    
    

    def checkdefeat(self):
        return False
    

    def isInBounds(self, j, i):
        return j>=0 and j<self.h and i>=0 and i<self.w


    def move(self, dir):
        for y in range(self.h):
            for x in range(self.w):                
                # parcours dans le sens contraire du déplacement pour éviter le piétinement du mouvement des valeurs
                y1,x1 = y,x
                if dir[0] > 0:
                    y1 = self.h-y-1
                if dir[1] > 0:
                    x1 = self.w-x-1     

                mask1 = self.grid[y1][x1]
                if mask1 != 0:               
                    y2 = y1 + dir[0]
                    x2 = x1 + dir[1]
                    
                    if self.isInBounds(y2, x2):
                        for flag1,i1 in mask1.flags():
                            if flag1 in objects and self.rules[i1-first_obj] & Flags.YOU:

                                def move(flag, y1,x1, y2,x2):
                                    self.grid[y1][x1] &= ~flag
                                    self.grid[y2][x2] |= flag

                                def push(y2, x2):
                                    mask2 = self.grid[y2][x2]
                                    if mask2 != 0:
                                        # détecter obstacle non déplaçable
                                        for flag2,i2 in mask2.flags():
                                            if flag2 in objects:  # seul les objets peuvent être solides
                                                rule = self.rules[i2-first_obj]
                                                if rule & Flags.SOLID and not rule & Flags.PUSH:
                                                    return False
                                        
                                        # récursivité pour éviter piétinement
                                        y3, x3 = y2+dir[0], x2+dir[1]
                                        if not self.isInBounds(y3, x3) or not push(y3, x3):
                                            return False
                                        
                                        # pousser tous les poussables
                                        for flag2,i2 in mask2.flags():
                                            if flag2 in words:
                                                move(flag2, y2,x2, y3,x3)
                                            elif flag2 in objects:
                                                rule = self.rules[i2-first_obj]
                                                if not rule & Flags.YOU and rule & Flags.PUSH:
                                                    move(flag2, y2,x2, y3,x3)
                                        
                                    return True

                                if push(y2, x2):
                                    move(flag1,y1,x1,y2,x2)
                                    self.changed = True                                    
        if self.changed:
            self.getRules()