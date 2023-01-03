import os.path
from sortedcontainers.sortedlist import SortedList
import time

from CORE.Etat import *
from CORE.Move import move
from IA.Heuristiques import heuristique
from IA.EtatIA import EtatIA
from ReadIA import readIA
from IA.SaveIA import saveIA
from UI.UI_pygame import *
from UTIL.Path import *
from UTIL.SysArgs import sysArgs


if __name__ == "__main__":
    args = sysArgs("-fps", "-level")

    if "-fps" in args:
        fps = int(args["-fps"])
    else:
        fps = 0
    
    if "-level" in args:
        levelname = args["-level"]
    else:
        levelname = input("level: ")

    etat = EtatIA(levelname)
    screen = Screen(etat)

    ouverts = SortedList()
    ouverts.add(etat)
    fermes = []

    print("A*...")
    t0 = time.time()
    iterations = 0
    courant: EtatIA = None

    while len(ouverts) != 0:
        if fps != 0:
            screen.deltatime(fps)
        
        courant = ouverts.pop(0)
        fermes.append(courant)
        iterations += 1
        screen.refresh(courant)

        if getQuit():
            print("interrupt")
            break
        elif courant.win:
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
                        etat.eur = heuristique(etat)
                        etat.parent = courant
                        ouverts.add(etat)

    t1 = time.time()
    print("A* time: " + str(t1-t0))
    print("iterations: " + str(iterations))
    
    if courant:
        saveIA(courant, levelname)
    else:
        print("ERROR")

    print("FIN")