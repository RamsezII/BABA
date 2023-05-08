from sortedcontainers.sortedlist import SortedList
import time

from CORE.Etat import *
from CORE.Move import move
from IA.EtatIA import EtatIA
from IA.Heuristiques import Heuristique
from IA.SaveIA import saveIA
from UI.UI_pygame import *
from UTIL.Path import *
from UTIL.SysArgs import sysArgs
from UTIL.Util import MAX_INT


if __name__ == "__main__":
    args = sysArgs("-fps", "-level")

    if "-fps" in args:
        fps = int(args["-fps"])
    else:
        fps = 0
    
    if "-level" in args:
        levelname = args["-level"]
    else:
        # levelname = input("level: ")
        # levelname = "level_IA_01.txt"
        # levelname = "level_2.txt"
        # levelname = "level_WPC1.txt"
        levelname = "level_ENF.txt"
        # levelname = "mithian_test.txt"

    etat = EtatIA(levelname)
    screen = Screen(etat)

    ouverts = SortedList()
    ouverts.add(etat)
    fermes = []

    print("start...")
    t0 = time.time()
    iterations = 0
    courant: EtatIA
    cout = 10

    while len(ouverts) != 0:
        if fps != 0:
            screen.deltatime(fps)
        
        courant = ouverts.pop(0)
        courant.cout = cout = cout + 1
                
        fermes.append(courant)
        iterations += 1
        screen.refresh(courant)

        if getQuit():
            print("interrupt")
            break
        elif courant.win:
            print("WIN!")
            break
        else:
            for push_dir in Etat.yxi_dirs:
                etat = courant.copy()
                move(etat, push_dir)
                if etat.pullChange():
                    if etat not in fermes and etat not in ouverts:
                        # etat.heur = int(courant.cout/4) + 4*Heuristique.heuristique(etat)
                        # screen.refresh(etat)
                        etat.heur = Heuristique.heuristique(etat)
                        if etat.heur < MAX_INT:
                            etat.parent = courant
                            ouverts.add(etat)

    t1 = time.time()
    print("finish time: " + str(t1-t0))
    print("iterations: " + str(iterations))
    
    if courant:
        saveIA(courant, levelname)
    else:
        print("ERROR")

    print("FIN")