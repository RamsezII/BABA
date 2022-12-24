import os
import sortedcontainers.sortedlist
import time

import CORE.Move
import CORE.ReadText
import IA.Euristiques
import IA.EtatIA
import UI.UI_pygame
import ReadIA


def RunIA_UI(levelname):
    dir_name = os.path.dirname(os.path.abspath(__file__))
    file = open(os.path.join(os.path.dirname(dir_name), "levels", levelname), 'r')
    lines = file.readlines()
    file.close()

    etat = IA.EtatIA.EtatIA()
    CORE.ReadText.readtext(etat, lines)

    ouverts = sortedcontainers.sortedlist.SortedList()
    ouverts.add(etat)

    fermes = []

    screen = UI.UI_pygame.Screen(ouverts[0])

    print("A*...")
    t0 = time.time()
    iterations = 0
    courant = None

    while len(ouverts) != 0:
        courant = ouverts.pop(0)
        iterations += 1

        screen.refresh(courant)
        if UI.UI_pygame.getQuit():
            print("interrupt")
            return

        if courant.win:
            print("WIN!")
            break
        elif courant.defeat:
            print("DEFEAT")
            break
        else:
            for dir in range(1, 5):
                etat = courant.clone()
                CORE.Move.move(etat, dir)
                if etat.pullChange() and etat not in ouverts and etat not in fermes:
                    etat.eur = IA.Euristiques.euristique(etat)
                    etat.parent = courant
                    ouverts.add(etat)
        fermes.append(courant)

    t1 = time.time()
    print("A* time: " + str(t1-t0))
    print("iterations: " + str(iterations))
    
    if courant:
        print("saving solution...")
        dirs = ("up", "right", "down", "left")
        savepath = os.path.join(os.path.dirname(dir_name), "IA_solutions", levelname)

        file = open(savepath, 'w')        

        def saveIA(etat):
            if etat.parent:
                saveIA(etat.parent)
            if etat.dir != 0:
                file.write(dirs[etat.dir-1] + '\n')
        saveIA(courant)
        
        file.close()

        print("saved solution in: " + savepath)
        ReadIA.run(levelname)
    else:
        print("ERROR")
    



if __name__ == "__main__":
    # argv = sys.argv
    # args = len(argv)
    # if args <= 1:
    #     filename = input("level name: ")
    # else:
    #     filename = argv[1]
    filename = "level_IA_03.txt"
    RunIA_UI(filename)
    print("FIN")