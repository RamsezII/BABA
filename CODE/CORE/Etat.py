import copy
from os.path import join as joinpath

from CORE.Data import *
from UTIL.Path import getlines
from UTIL.YXI import yxi

class Etat():
    dirs_yxi = [yxi()]
    h = w = count = 0
    def __init__(self, levelname):
        self.changed = True
        self.win = False
        self.defeat = False
        self.parent: Etat
        self.m_cols = BABAf.none
        self.grid = [BABAf.none]

        levelpath = joinpath("levels", levelname)
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
        Etat.dirs_yxi = [yxi(-1,0,-Etat.h), yxi(0,1,1), yxi(1,0,Etat.h), yxi(-1,0,-1)]

        self.rules = 6*[BABAf.none]    
        self.getRules()
        
        self.yous = []
        self.wins = set()
        self.checkWinDefeat()
    

    def pullChange(self):
        if self.changed:
            self.changed = False
            return True
        else:
            return False


    def clone(self):
        parent = self.parent
        self.parent: Etat
        clone = copy.deepcopy(self)
        clone.parent = self.parent = parent
        return clone
    

    def __eq__(self, other):
        return self.grid == other.grid


    def logEtat(self):
        log = ""
        for k in range(Etat.count):
            log += self.grid[k].textcode() + " "
            if (k+1) % Etat.w == 0:
                log += '\n'
        return log
    

    def isInBounds(self, yxi):
        return yxi.y>=0 and yxi.y<Etat.h and yxi.x>=0 and yxi.x<Etat.w


    def getRules(self):
        # un bitmask par objet (6 au total). si "BABA IS YOU" est visible dans le niveau, le flag 'YOU' dans le bitmask de 'baba' dans 'self.rules' sera à 1
        # dans le cas d'une transformation, par exemple "BABA IS ROCK", toutes les cases sont parcourues et chaque case où le flag 'baba' est à 1 est mis à 0 et le flag 'rock' est mis à 1
        oldrules = self.rules
        self.rules = 6*[BABAf.none]
        for k in range(self.count):
            if self.grid[k] & BABAf.IS:
                pos_k = i2yxi(k)
                for dir_i in range(0,2):
                    pos_a = pos_k + Etat.dirs_yxi[dir_i]
                    pos_b = pos_k + Etat.dirs_yxi[2+dir_i]
                    if self.isInBounds(pos_a) and self.isInBounds(pos_b):
                        prefs = self.grid[pos_a.i]
                        suffs = self.grid[pos_b.i]
                        if prefs * suffs != 0 and prefs & words_mask and suffs & words_mask:
                            for pref in word2obj:
                                if pref in prefs:
                                    for _,suf in suffs.flags(0, BABAb.last_word):
                                        self.rules[word2obj[pref]] |= suf
                                        # si suffixe désigne un objet, il y a probablement transformation
                                        if suf != pref and suf in word2obj:
                                            pref_obj = BABAf(1 << (word2obj[pref]+BABAb.first_obj))
                                            suf_obj = BABAf(1 << (word2obj[suf]+BABAb.first_obj))
                                            for k2 in range(self.count):
                                                if self.grid[k2] & pref_obj:
                                                    self.grid[k2] &= ~pref_obj
                                                    self.grid[k2] |= suf_obj
        if oldrules != self.rules:
            self.m_cols = BABAf.none
            for i,rule in enumerate(self.rules):
                if rule & BABAf.SOLID:
                    self.m_cols |= BABAf(1 << (BABAb.first_obj + i))


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
            for i,flag in flags.flags(BABAb.first_obj, BABAb.last_all):
                rule = self.rules[i-BABAb.first_obj]
                if BABAf.YOU in rule:
                    you = True
                    self.defeat = False
                    self.yous.append((k,flag))
                if BABAf.WIN in rule:
                    win = True
                    self.wins.add(k)
            if you and win:
                self.win = True
                break


def i2yxi(i):
    return yxi(i // Etat.h, i % Etat.w, i)

def yx2yxi(y,x):
    return yxi(y, x, y*Etat.h + x*Etat.w)

def isInBounds(yxi):
    return yxi.y>=0 and yxi.x<Etat.w and yxi.y<Etat.h and yxi.x>=0