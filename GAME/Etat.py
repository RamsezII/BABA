import time
from Codage import *
import copy


class Etat():
    def __init__(self):
        self.win = False
        self.defeat = False


    def readtext(self, lines):
        self.height = len(lines)
        self.grid = []
        for j in range(self.height):
            splits = lines[j].split(' ')
            self.width = len(splits)
            for i in range(self.width):
                if splits[i].startswith(".."):
                    self.grid.append(Flags(0))
                else:
                    self.grid.append(Flags(1 << int(splits[i])))
        self.count = self.height*self.width
        self.yous = []
        self.wins = set()
        self.getRules()
        self.checkWinDefeat()
    

    def isInBounds(self, k):
        return k >= 0 and k < self.count


    def clone(self):
        return copy.deepcopy(self)
    

    def __eq__(self, other):
        return self.grid == other.grid

        
    def logRules(self):
        log = ""
        for f,flags in enumerate(self.rules):
            if flags != 0:
                log += Flags(1 << (f+first_obj)).name + " is " + str(flags) + "\n"
        return log


    def logEtat(self):
        log = ""
        for k in range(self.count):
            log += self.grid[k].textcode() + " "
            if (k+1) % self.width == 0:
                log += '\n'
        return log


    def getRules(self):
        # un bitmask par objet (6 au total). si "BABA IS YOU" est visible dans le niveau, le flag 'YOU' dans le bitmask de 'baba' dans 'self.rules' sera à 1
        # dans le cas d'une transformation, par exemple "BABA IS ROCK", toutes les cases sont parcourues et chaque case où le flag 'baba' est à 1 est mis à 0 et le flag 'rock' est mis à 1
        self.rules = 6*[Flags(0)]
        for k in range(self.count):
            if Flags.IS in self.grid[k]:
                for dir in (self.width, 1):  # les 2 sens de lectures: vers le bas et vers la droite
                    if self.isInBounds(k-dir) + self.isInBounds(k+dir):
                        prefixes = self.grid[k-dir]
                        suffixes = self.grid[k+dir]

                        if prefixes * suffixes != 0:
                            for pref in word2obj:
                                if pref in prefixes:
                                    for _,suf in suffixes.flags(0, first_obj):
                                        self.rules[word2obj[pref]] |= suf
                                        # si suffixe désigne aussi un objet, c'est une loi de transformation
                                        if suf in word2obj:
                                            pref_obj = Flags(1 << (word2obj[pref]+first_obj))
                                            suf_obj = Flags(1 << (word2obj[suf]+first_obj))
                                            for k2 in range(self.count):
                                                if self.grid[k2] & pref_obj:
                                                    self.grid[k2] &= ~pref_obj
                                                    self.grid[k2] |= suf_obj


    def checkWinDefeat(self):
        # on gagne si un des flags représentant les objets d'une case, a son correspondant dans 'self.rules' marqué comme 'YOU' et 'WIN'
        # on perd si aucune case n'a d'objet correspondant dans 'self.rules' marqué comme 'YOU'
        self.defeat = True
        self.win = False
        self.yous.clear()
        self.wins.clear()
        for k,flags in enumerate(self.grid):
            you = False
            win = False
            for i,flag in flags.flags(first_obj, last_all):
                rule = self.rules[i-first_obj]
                if Flags.YOU in rule:
                    you = True
                    self.defeat = False
                    self.yous.append((k,flag))
                if Flags.WIN in rule:
                    win = True
                    self.wins.add(k)
            if you and win:
                self.win = True
                break
    

    def deplace(self, flag, k, dir):
        self.grid[k] &= ~flag
        self.grid[k+dir] |= flag


    def push(self, k, dir):
        mask2 = self.grid[k]
        if mask2 != 0:
            obstacles = False
            # détecter obstacle non déplaçable
            for i2,flag2 in mask2.flags(0, last_all):
                if i2 < first_obj:  # words
                    obstacles = True
                else:  # objects
                    rule = self.rules[i2-first_obj]
                    if rule & Flags.PUSH:
                        obstacles = True
                    elif rule & Flags.SOLID:
                        return False                                                                                        
            if obstacles:                                        
                # récursivité pour éviter piétinement (push des cases suivantes avant push immédiat)
                k2 = k+dir
                if not self.isInBounds(k2) or not self.push(k2, dir):
                    return False                
                # pousser cette case
                for i2,flag2 in mask2.flags(0, last_all):
                    self.deplace(flag2, k, dir)
        return True


    def move(self, dir):
        count = len(self.yous)
        for k in range(count):
            # inverser ordre de parcours selon sens de deplacement
            if dir > 0:
                you = self.yous[count-k-1]
            else:
                you = self.yous[k]
            k_ = you[0]
            if self.isInBounds(k_+dir) and self.push(k_+dir, dir):
                self.deplace(you[1],k_, dir)
        self.getRules()
        self.checkWinDefeat()
    

    def euristique(self):
        return self.manhattan()


    def manhattan(self):
        wins = set()
        yous = set()
        for you in self.yous:
            yous.add((you[0]//self.width, you[0]%self.width))
        for win in self.wins:
            wins.add((win//self.width, win%self.width))

        man = self.height+self.width
        for win in wins:
            for you in yous:
                h = abs(win[0]-you[0])
                w = abs(win[1]-you[1])
                dist = pow(h*h + w*w, 0.5)
                if dist < man:
                    man = dist
        return man