from genericpath import isfile


level0_path = "level_0.txt"
empty = '.'
baba = 'b'
wall = 'w'
flag = 'f'

you = baba

print("  -- BABA IS YOU! --\nmove with ZQSD keys")


class Etat():
    def __init__(self, path):
        file = open(path, "r")
        lines = file.readlines()
        file.close()
        self.h = len(lines)
        self.w = len(lines[0])-1
        self.data = {}
        for j in range(self.h):
            for i in range(self.w):
                pos = (j,i)
                e = lines[j][i]
                if e != empty:
                    self.data[pos] = {e}
                if e == baba:
                    self.pos = pos
    

    def logAtPos(self, pos):        
        if pos in self.data:                
            log = ""
            atpos = self.data[pos]

            if you in atpos:
                log = you
            else:
                log = " "

            if wall in atpos:
                log = "[" + log + "]"
            else:
                log = " " + log + " "

            return log
        else:
            return " . "


    def __str__(self):
        log = ""
        for y in range(self.h):
            for x in range(self.w):
                log += self.logAtPos((y,x))
            log += "\n"
        return log


    def copy(self, other):
        pass


    def checkwin(self):
        return False    
    

    def isInBounds(self, pos):
        return pos[0]>=0 and pos[0]<self.h and pos[1]>=0 and pos[1]<self.w
    

    def addToPos(self,pos,object):
        self.data[pos[0]][pos[1]] = empty
        self.data[self.pos[0]][self.pos[1]] = object


    def play(self):

        inp = input("move: ").lower()
        dir = [0,0]

        if inp == "z": dir[0]-=1
        if inp == "d": dir[1]+=1
        if inp == "s": dir[0]+=1
        if inp == "q": dir[1]-=1    

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


if __name__ == "__main__":    

    if isfile(level0_path):
        etat = Etat(level0_path)
        while not etat.checkwin():
            print(etat)
            etat.play()
    else:
        print("no savefile at: " + level0_path)    

    print("FIN")

