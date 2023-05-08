
import copy
from CORE.Data import *
from UTIL.Path import *
from UTIL.YXI import YXI


class GETf(IntFlag):
    none = 0
    getWins = 1 << 0
    getYous = 1 << 1
    getRules = 1 << 2
    getAll = getWins | getYous | getRules


class Etat():
    yxi_up: YXI = YXI(0,0,0)
    yxi_down: YXI = YXI(0,0,0)
    yxi_left = YXI(0,-1,-1)
    yxi_right = YXI(0,1,1)
    yxi_dirs = (YXI(0,0,0))
    h = w = count = 0

    def __init__(self, levelname):
        self.changed = True
        self.win = False
        self.defeat = False
        self.parent: Etat = None
        self.refreshMask = GETf.none
        self.rules:dict
        self.dir:YXI

        levelpath = os.path.join(rootpath(), "levels", levelname)
        lines = getlines(levelpath)

        Etat.h = len(lines)
        self.grid = []
        for j in range(Etat.h):
            splits = lines[j].split(' ')
            Etat.w = len(splits)
            for i in range(Etat.w):
                if splits[i].startswith(".."):
                    self.grid.append(BABAf.none)
                else:
                    self.grid.append(BABAf(1 << int(splits[i])))

        Etat.count = Etat.h*Etat.w
        Etat.yxi_up = YXI(-1,0,-Etat.w)
        Etat.yxi_down = YXI(1,0,Etat.w)
        Etat.yxi_dirs = (Etat.yxi_up, Etat.yxi_down, Etat.yxi_left, Etat.yxi_right)
        
        self.yous = []  # l'ordre est important pour les YOU
        self.wins = set()
        self.distances:dict = None
        self.getRules()
        self.checkWinDefeat()
    

    def __iter__(self):
        for i in range(self.count):
            yield (i2yxi(i),self.grid[i])
    

    def pullChange(self):
        if self.changed:
            self.changed = False
            return True
        else:
            return False


    def copy(self):
        clone = copy.copy(self)
        clone.parent = self
        clone.grid = self.grid.copy()
        return clone
    

    def __eq__(self, other):
        return self.grid == other.grid
    

    def logRules(self):
        for f in self.rules:
            print(BABAf(f).name, ":", self.rules[f])


    def logEtat(self):
        log = ""
        # for i in range(Etat.w):
        #     log += str(i) + " "
        # log += '\n'
        for k in range(Etat.count):
            log += self.grid[k].textcode() + " "
            if (k+1) % Etat.w == 0:
                log += "  " + str(k//Etat.w) + " | " + str(k) + '\n'
        print(log)


    def getRules(self):
        self.refreshMask &= ~GETf.getRules
        # un bitmask par objet (6 au total). si "BABA IS YOU" est visible dans le niveau, le flag 'YOU' dans le bitmask de 'baba' dans 'self.rules' sera à 1
        # dans le cas d'une transformation, par exemple "BABA IS ROCK", toutes les cases sont parcourues et chaque case où le flag 'baba' est à 1 est mis à 0 et le flag 'rock' est mis à 1
        self.rules = {
            BABAf.PUSH: words_mask,
        }
        for k in range(self.count):
            if BABAf.IS in self.grid[k]:
                pos = i2yxi(k)
                for dir in (Etat.yxi_right, Etat.yxi_down):
                    pos_pref = pos + -dir
                    pos_suff = pos + dir
                    if isInBounds(pos_pref) and isInBounds(pos_suff):
                        prefs = self.grid[pos_pref.i]
                        suffs = self.grid[pos_suff.i]
                        if prefs * suffs != 0 and prefs & words_mask and suffs & words_mask:
                            for _,pref_f in prefs.flags(BABAb.first_word, BABAb.last_word):
                                for _,suff_f in suffs.flags(BABAb.first_word, BABAb.last_word):
                                    if pref_f in word2obj:
                                        pref_obj = word2obj[pref_f]
                                        if suff_f in self.rules:
                                            self.rules[suff_f] |= pref_obj
                                        else:
                                            self.rules[suff_f] = pref_obj
                                        # si suffixe aussi désigne un objet, on applique la transformation
                                        if suff_f in word2obj:
                                            suff_obj = word2obj[suff_f]
                                            for k2 in range(self.count):
                                                if pref_f in self.grid[k2]:
                                                    self.grid[k2] &= ~pref_obj
                                                    self.grid[k2] |= suff_obj


    def checkWinDefeat(self):
        self.refreshMask &= ~(GETf.getYous | GETf.getWins)
        # on gagne si un des flags représentant les objets d'une case, a son correspondant dans 'self.rules' marqué comme 'YOU' et 'WIN'
        # on perd si aucune case n'a d'objet correspondant dans 'self.rules' marqué comme 'YOU'
        self.defeat = True
        self.win = False

        if BABAf.YOU not in self.rules:
            return

        self.yous = []
        self.wins = set()
            
        for cell_i,cell_f in enumerate(self.grid):
            you = False
            win = False

            if cell_f & self.rules[BABAf.YOU]:
                you = True
                self.defeat = False
                self.yous.append(cell_i)
            
            if BABAf.WIN in self.rules and cell_f & self.rules[BABAf.WIN]:
                win = True
                self.wins.add(cell_i)
                
            if you and win:
                self.win = True
                break


    def getYous(self):
        self.yous = []
        if BABAf.YOU in self.rules:
            for cell_i,cell_f in enumerate(self.grid):
                if cell_f & self.rules[BABAf.YOU]:
                    self.yous.append(cell_i)


def i2yxi(i):
    return YXI(i // Etat.w, i % Etat.w, i)

def yx2yxi(y,x):
    return YXI(y, x, y*Etat.w + x)

def isInBounds(yxi):
    return yxi.y>=0 and yxi.x<Etat.w and yxi.y<Etat.h and yxi.x>=0