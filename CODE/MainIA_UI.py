import os.path
from sortedcontainers.sortedlist import SortedList
import time

from CORE.Etat import Etat
from CORE.Move import move
from IA.Euristiques import euristique
from IA.EtatIA import EtatIA
import ReadIA
from UI.UI_pygame import *


def RunIA_UI(levelname):
    etat = EtatIA(levelname)
    screen = Screen(etat)
    fps = 5

    ouverts = SortedList()
    ouverts.add(etat)
    fermes = []

    print("A*...")
    t0 = time.time()
    iterations = 0
    courant = None

    while len(ouverts) != 0:
        screen.deltatime(fps)
        courant = ouverts.pop(0)
        iterations += 1

        screen.refresh(courant)
        if getQuit():
            print("interrupt")
            return

        if courant.win:
            print("WIN!")
            break
        elif courant.defeat:
            print("DEFEAT")
            break
        else:
            for i,dir in enumerate(Etat.yxi_dirs):
                etat = courant.clone()
                move(etat, dir)
                if etat.pullChange():
                    if etat.needPaths:
                        etat.getDistances()
                    if etat not in ouverts and etat not in fermes:
                        etat.dir_i = i
                        etat.eur = euristique(etat)
                        etat.parent = courant
                        ouverts.add(etat)
        fermes.append(courant)

    t1 = time.time()
    print("A* time: " + str(t1-t0))
    print("iterations: " + str(iterations))
    
    if courant:
        print("saving solution...")
        savelines = []
        while courant.parent:
            savelines.append(EtatIA.dirs[courant.dir_i])
            courant = courant.parent
        savepath = os.path.join("IA_solutions", levelname)
        file = open(savepath, 'w')
        file.writelines(savelines)        
        file.close()
        print("saved solution in: " + savepath)
    else:
        print("ERROR")
    



if __name__ == "__main__":
    # argv = sys.argv
    # args = len(argv)
    # if args <= 1:
    #     levelname = input("level name: ")
    # else:
    #     levelname = argv[1]
    levelname = "level_IA_03.txt"
    RunIA_UI(levelname)    
    # ReadIA.run(levelname)
    print("FIN")