import os
import sys
import sortedcontainers.sortedlist
import time

import Etat
import euristiques
import UI
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
        courant = Etat.Etat()
        courant.readtext(lines)
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
        screen = UI.Screen(self.ouverts[0])

        print("A*...")
        t0 = time.time()
        t_next = time.time()+1
        loopcount = 0

        while len(self.ouverts) != 0:
            courant = self.ouverts.pop(0)

            screen.refresh(courant)
            if UI.getQuit():
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
                    etat.move(dir)
                    if etat.pullChange() and etat not in self.ouverts and etat not in self.fermes:
                        etat.eur = euristiques.euristique(etat)
                        etat.parent = courant
                        self.ouverts.add(etat)
            self.fermes.append(courant)

            loopcount += 1
            t_loop = time.time()
            if t_loop > t_next:
                t_next += 1
                print("operations: " + str(loopcount))
                loopcount = 0

        t1 = time.time()
        print("A* time: " + str(t1-t0) + "\nsaving solution...")
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