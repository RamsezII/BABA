from sortedcontainers.sortedlist import SortedList
import time

from CORE.Etat import *
from CORE.Move import move
from IA.EtatIA import EtatIA
from IA.Euristiques import euristique
from IA.SaveIA import saveIA
from UTIL.SysArgs import sysArgs


if __name__ == "__main__":
    args = sysArgs("-fps", "-level")

    if "-level" in args:
        levelname = args["-level"]
    else:
        levelname = input("level: ")

    ouverts = SortedList()
    ouverts.add(EtatIA(levelname))
    fermes = []

    print("A*...")
    t0 = time.time()
    t01 = time.time()
    iterations = 0
    courant: EtatIA = None

    while len(ouverts) != 0:
        courant = ouverts.pop(0)
        fermes.append(courant)

        if courant.win:
            print("WIN!")
            break
        elif courant.defeat:
            print("DEFEAT")
            break
        else:
            for dir in Etat.yxi_dirs:
                etat = courant.clone()
                move(etat, dir)
                if etat.pullChange():
                    if etat.m_get & GETf.getPaths:
                        etat.getDistances()
                    if etat not in ouverts and etat not in fermes:
                        etat.dir = dir
                        etat.eur = euristique(etat)
                        etat.parent = courant
                        ouverts.add(etat)
        iterations += 1
        if iterations % 20 == 0:
            t02 = time.time()
            print("iteration: {} | time: {}".format(iterations, t02-t01))
            t01 = t02

    t1 = time.time()
    print("A* time: " + str(t1-t0))
    print("iterations: " + str(iterations))
    
    if courant:
        saveIA(courant, levelname)
    else:
        print("ERROR")

    print("FIN")