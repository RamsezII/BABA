from Codage import *
import copy


class Etat():
    def __init__(self):
        self.changed = True
        self.win = False
        self.defeat = False


    def readtext(self, lines):
        self.height = len(lines)
        self.grid = []
        for j in range(self.height):
            splits = lines[j].split(' ')
            self.width = len(splits)
            l = []
            for i in range(self.width):
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
        for y in range(self.height):
            for x in range(self.width):
                log += self.grid[y][x].textcode() + " "
            log += '\n'
        return log


    def getRules(self):
        # un bitmask par objet (6 au total). si "BABA IS YOU" est visible dans le niveau, le flag 'YOU' dans le bitmask de 'baba' dans 'self.rules' sera à 1
        # dans le cas d'une transformation, par exemple "BABA IS ROCK", toutes les cases sont parcourues et chaque case où le flag 'baba' est à 1 est mis à 0 et le flag 'rock' est mis à 1
        self.rules = 6*[Flags(0)]
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x].hasflags(Flags.IS):
                    for dir in ((1,0), (0,1)):
                        if y-dir[0] >= 0 and y+dir[0] < self.height and x-dir[1] >= 0 and x+dir[1] < self.width:

                            prefixe = self.grid[y-dir[0]][x-dir[1]]
                            suffixe = self.grid[y+dir[0]][x+dir[1]]

                            if prefixe != 0 and suffixe != 0:
                                for _,pref in prefixe.flags():
                                    if pref in word2obj:
                                        for _,suf in suffixe.flags():
                                            if suf in words:
                                                self.rules[word2obj[pref]] |= suf

                                                # si suffixe désigne aussi un objet, c'est une loi de transformation
                                                if suf in word2obj:
                                                    pref_obj = Flags(1 << (word2obj[pref]+first_obj))
                                                    suf_obj = Flags(1 << (word2obj[suf]+first_obj))
                                                    for y2 in range(self.height):
                                                        for x2 in range(self.width):
                                                            if self.grid[y2][x2] & pref_obj:
                                                                self.grid[y2][x2] &= ~pref_obj
                                                                self.grid[y2][x2] |= suf_obj


    def checkWinDefeat(self):
        # on gagne si un des flags représentant les objets d'une case, a son correspondant dans 'self.rules' marqué comme 'YOU' et 'WIN'
        # on perd si aucune case n'a d'objet correspondant dans 'self.rules' marqué comme 'YOU'
        self.defeat = True
        self.win = False
        for y in range(self.height):
            for x in range(self.width):
                you = False
                win = False
                for i,flag in self.grid[y][x].flags():
                    if flag in objects:
                        rule = self.rules[i-first_obj]
                        if rule & Flags.YOU:
                            you = True
                            self.defeat = False
                        if rule & Flags.WIN:
                            win = True
                if you and win:
                    self.win = True
                    return
    

    def isInBounds(self, j, i):
        return j>=0 and j<self.height and i>=0 and i<self.width


    def move(self, dir):
        for y in range(self.height):
            for x in range(self.width):                
                # parcours dans le sens contraire du déplacement pour éviter le piétinement du mouvement des valeurs
                y1,x1 = y,x
                if dir[0] > 0:
                    y1 = self.height-y-1
                if dir[1] > 0:
                    x1 = self.width-x-1     

                mask1 = self.grid[y1][x1]
                if mask1 != 0:               
                    y2 = y1 + dir[0]
                    x2 = x1 + dir[1]
                    
                    if self.isInBounds(y2, x2):
                        for i1,flag1 in mask1.flags():
                            if flag1 in objects and self.rules[i1-first_obj] & Flags.YOU:

                                def move(flag, y1,x1, y2,x2):
                                    self.grid[y1][x1] &= ~flag
                                    self.grid[y2][x2] |= flag

                                def push(y2, x2):
                                    mask2 = self.grid[y2][x2]
                                    if mask2 != 0:
                                        # détecter obstacle non déplaçable
                                        for i2,flag2 in mask2.flags():
                                            if flag2 in objects:  # seul les objets peuvent être solides
                                                rule = self.rules[i2-first_obj]
                                                if rule & Flags.SOLID and not rule & Flags.PUSH:
                                                    return False
                                        
                                        # récursivité pour éviter piétinement
                                        y3, x3 = y2+dir[0], x2+dir[1]
                                        if not self.isInBounds(y3, x3) or not push(y3, x3):
                                            return False
                                        
                                        # pousser tous les poussables
                                        for i2,flag2 in mask2.flags():
                                            if flag2 in words:
                                                move(flag2, y2,x2, y3,x3)
                                            elif flag2 in objects:
                                                rule = self.rules[i2-first_obj]
                                                if not rule & Flags.PUSH:
                                                    return True
                                                else:
                                                    move(flag2, y2,x2, y3,x3)                                        
                                    return True

                                if push(y2, x2):
                                    move(flag1,y1,x1,y2,x2)
                                    self.changed = True

        if self.changed:
            self.getRules()
            self.checkWinDefeat()
        
        return self.changed


    def manhattan(self):
        wins = set()
        yous = set()
        for y in range(self.height):
            for x in range(self.width):
                pos = (y,x)
                flags = self.grid[y][x]
                for i1,flag in flags.flags():
                    if flag in objects:
                        rules = self.rules[i1-first_obj]
                        if rules.hasflags(Flags.WIN):
                            wins.add(pos)
                        if rules.hasflags(Flags.YOU):
                            yous.add(pos)

        man = self.height+self.width
        for win in wins:
            for you in yous:
                dist = abs(win[0]-you[0])+abs(win[1]-you[1])
                if dist < man:
                    man = dist
        return man