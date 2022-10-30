from opcode import hasfree
import Grid

class Etat():
    def __init__(self, path):
        file = open(path, 'r')
        lines = file.readlines()
        file.close()
        self.h = len(lines)
        self.w = len(lines[0])-1
        self.grid = []
        for j in range(self.h):
            l = []
            for i in range(self.w):
                l.append(Grid.code2flag[lines[j][i]])
            self.grid.append(l)

    def __str__(self):
        log = ""
        for y in range(self.h):
            for x in range(self.w):
                log += self.logAtPos(y,x)
            log += '\n'
        return log

    def getRules(self):
        self.rules = {}

    def logAtPos(self, y,x):
        flags = self.grid[y][x]
        log = ""
        for flag in Grid.Flags:
            if flags.hashflag(flag):
                if (Grid)
        if flags.hasflag(Grid.Flags.baba):
            log = Grid.flag2code[Grid.Flags.baba]
        else:
            log = ' '
        if flags.hasflag(Grid.Flags.wall):
            log = '[' + log + ']'
        elif flags.hasflag(Grid.Flags.water):
            log = '{' + log + '}'
        else:
            log = ' ' + log + ' '
        return log


    def copy(self, other):
        pass


    def checkwin(self):
        return False    


    def isInBounds(self, pos):
        return pos[0]>=0 and pos[0]<self.h and pos[1]>=0 and pos[1]<self.w


    def play(self):
        inp = input("move: ").lower()

        if inp == 'r':
            print("rewind")
        else:
            dir = [0,0]

            if inp == 'z': dir[0]-=1
            if inp == 'd': dir[1]+=1
            if inp == 's': dir[0]+=1
            if inp == 'q': dir[1]-=1    

            if dir != [0,0]:
                self.move(dir)


    def move (self, dir):
        pos2 = (self.pos[0]+dir[0], self.pos[1]+dir[1])
        if self.isInBounds(pos2):
            if pos2 in self.data:
                pass
            else:
                self.data[pos2] = {baba}
                self.data[self.pos].remove(baba)
                if len(self.data[self.pos]) == 0:
                    self.data.pop(self.pos)
                self.pos = pos2
        else:
            print("out of bounds move")
            pass