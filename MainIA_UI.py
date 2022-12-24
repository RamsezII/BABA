import os
import sys
import sortedcontainers.sortedlist
import time

import CORE.Etat
import CORE.Move
import CORE.ReadText
import IA.Euristiques
import UI.UI_pygame
import ReadIA


dir_name = os.path.dirname(os.path.abspath(__file__))
dirs = ["up", "right", "down", "left"]


class AStar():
    def __init__(self, levelname, ui):
        self.levelname = levelname
        file = open(os.path.join(os.path.dirname(dir_name), "levels", levelname), 'r')
        lines = file.readlines()
        file.close()
        self.ouverts = sortedcontainers.sortedlist.SortedList()
        courant = CORE.Etat.Etat()
        CORE.ReadText.readtext(courant, lines)
        self.ouverts.add(courant)
        self.fermes = []
        self.ui = ui
    

    def saveIA(self, etat, file):
        if etat.parent:
            self.saveIA(etat.parent, file)
        if etat.dir != 0:
            file.write(dirs[etat.dir-1] + '\n')
    

    def showSolution(self, etat, fps):
        if etat.parent:
            self.showSolution(etat.parent, fps)
            self.deltatime(fps)
        self.refresh(etat)
    

    def mainLoop(self):
        screen = UI.UI_pygame.Screen(self.ouverts[0])

        print("A*...")
        t0 = time.time()
        iterations = 0

        while len(self.ouverts) != 0:
            courant = self.ouverts.pop(0)
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
                    if etat.pullChange() and etat not in self.ouverts and etat not in self.fermes:
                        etat.eur = IA.Euristiques.euristique(etat)
                        etat.parent = courant
                        self.ouverts.add(etat)
            self.fermes.append(courant)

        t1 = time.time()
        print("A* time: " + str(t1-t0))
        print("iterations: " + str(iterations))
        print("saving solution...")
        savepath = os.path.join(os.path.dirname(dir_name), "IA_solutions", self.levelname)
        file = open(savepath, 'w')
        self.saveIA(courant, file)
        file.close()
        print("saved solution in: " + savepath)
        ReadIA.run(self.levelname)


if __name__ == "__main__":
    # argv = sys.argv
    # args = len(argv)
    # if args <= 1:
    #     filename = input("level name: ")
    # else:
    #     filename = argv[1]
    filename = "level_IA_03.txt"
    AStar(filename, True).mainLoop()
    print("FIN")