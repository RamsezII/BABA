from CORE.Data import *
from CORE.Etat import Etat
from UTIL.Path import *


def textToEtat(etat, levelpath):
    lines = getlines(levelpath)
    Etat.h = len(lines)
    etat.grid = []
    for j in range(Etat.h):
        splits = lines[j].split(' ')
        Etat.w = len(splits)
        for i in range(Etat.w):
            if splits[i].startswith(".."):
                etat.grid.append(BABAf.none)
            else:
                etat.grid.append(BABAf(1 << int(splits[i])))