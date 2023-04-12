
import copy
from CORE.Data import *
from UTIL.Path import *
from UTIL.YXI import YXI


class GETf(IntFlag):
    none = 0
    getWins = 1 << 0
    getYous = 1 << 1
    getRules = 1 << 2


class Etat():
    yxi_left = YXI(0,-1,-1)
    yxi_right = YXI(0,1,1)
    yxi_up: YXI = YXI(0,0,0)
    yxi_down: YXI = YXI(0,0,0)
    yxi_dirs = (YXI(0,0,0))
    h = w = count = 0

    def __init__(self, levelname):
        self.changed = True
        self.win = False
        self.defeat = False
        self.parent: Etat = None
        self.m_cols = self.m_yous = self.m_wins = BABAf.none
        self.refreshMask = GETf.none
        self.grid = [BABAf.none]

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

        self.rules = 6*[BABAf.none]    
        self.getRules()
        
        self.yous = []  # l'ordre est important pour les YOU
        self.wins = set()
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
        for i,rule in enumerate(self.rules):
            print(BABAf(1<<(i+BABAb.first_obj)).name, ":", rule)


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
        rules = 6*[BABAf.none]
        for k in range(self.count):
            if self.grid[k] & BABAf.IS:
                pos_k = i2yxi(k)
                for dir in (Etat.yxi_right, Etat.yxi_down):
                    pos_a = pos_k + -dir
                    pos_b = pos_k + dir
                    if isInBounds(pos_a) and isInBounds(pos_b):
                        prefs = self.grid[pos_a.i]
                        suffs = self.grid[pos_b.i]
                        if prefs * suffs != 0 and prefs & words_mask and suffs & words_mask:
                            for pref in word2rule:
                                if prefs & pref:
                                    for _,suf in suffs.flags(BABAb.first_word, BABAb.last_word):
                                        rules[word2rule[pref]] |= suf
                                        # si suffixe désigne un objet, il y a probablement transformation
                                        if suf != pref and suf in word2rule:
                                            pref_obj = BABAf(1 << (word2rule[pref]+BABAb.first_obj))
                                            suf_obj = BABAf(1 << (word2rule[suf]+BABAb.first_obj))
                                            for k2 in range(self.count):
                                                if self.grid[k2] & pref_obj:
                                                    self.grid[k2] &= ~pref_obj
                                                    self.grid[k2] |= suf_obj
        if self.rules != rules:
            self.rules = rules
            self.m_cols = self.m_yous = BABAf.none
            for i,rule in enumerate(rules):
                if rule & BABAf.SOLID:
                    self.m_cols |= BABAf(1 << (i+BABAb.first_obj))
                if rule & BABAf.YOU:
                    self.m_yous |= (1 << (i+BABAb.first_obj))
                if rule & BABAf.WIN:
                    self.m_wins |= (1 << (i+BABAb.first_obj))


    def checkWinDefeat(self):
        self.refreshMask &= ~(GETf.getYous | GETf.getWins)
        # on gagne si un des flags représentant les objets d'une case, a son correspondant dans 'self.rules' marqué comme 'YOU' et 'WIN'
        # on perd si aucune case n'a d'objet correspondant dans 'self.rules' marqué comme 'YOU'
        self.defeat = True
        self.win = False
        self.yous = []
        self.wins = []
        for k,flags in enumerate(self.grid):
            you = False
            win = False
            pos = i2yxi(k)
            for i,_ in flags.flags(BABAb.first_obj, BABAb.last_obj):
                rule = self.rules[i-BABAb.first_obj]
                if BABAf.YOU in rule:
                    you = True
                    self.defeat = False
                    self.yous.append(pos)
                if BABAf.WIN in rule:
                    win = True
                    self.wins.append(pos)
            if you and win:
                self.win = True
                break


    def getYous(self):
        self.yous.clear()
        for k,flags in enumerate(self.grid):
            if flags in self.m_yous:
                self.yous.append(i2yxi(k))


def i2yxi(i):
    return YXI(i // Etat.w, i % Etat.w, i)

def yx2yxi(y,x):
    return YXI(y, x, y*Etat.w + x)

def isInBounds(yxi):
    return yxi.y>=0 and yxi.x<Etat.w and yxi.y<Etat.h and yxi.x>=0