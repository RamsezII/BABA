from opcode import hasfree

import Flags

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
                l.append(Flags.Flags(1 << int(Flags.Objs(int(splits[i])))))
            self.grid.append(l)
        self.rules = set()
        self.getRules()


    def __str__(self):
        log = ""
        f = "{value:02d} "
        for y in range(self.h):
            for x in range(self.w):
                log += f.format(value=self.grid[y][x].value)
            log += '\n'
        return log


    def getRules(self):
        self.rules.clear()
        for j in range(self.h):
            for i in range(self.w):
                val = self.grid[j][i]
                if val.hasflags_OR(Flags.Flags.is_word):
                    self.rules.add("BABAisYOU")


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

                j_,i_ = j,i
                if dir[0] > 0:
                    j_ = self.h-j-1
                if dir[1] > 0:
                    i_ = self.w-i-1
                pos2 = [j_+dir[0],i_+dir[1]]
                
                if self.isInBounds(pos2):
                    val = self.grid[j_][i_]
                    val2 = self.grid[pos2[0]][pos2[1]]
                    if val.hasflags_OR(Flags.Flags.baba_obj) and "BABAisYOU" in self.rules:
                        if val2 == Flags.Flags.empty:
                            self.grid[pos2[0]][pos2[1]] |= Flags.Flags.baba_obj
                            self.grid[j_][i_] &= ~Flags.Flags.baba_obj
        return self