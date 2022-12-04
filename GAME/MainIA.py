import os
import sys
import sortedcontainers.sortedlist
import time

import Etat
import euristiques


dir_name = os.path.dirname(os.path.abspath(__file__))
dirs = ["up", "right", "down", "left"]


class AStar():
    def __init__(self, levelname, ui):
        self.levelname = os.path.join(os.path.dirname(dir_name), "levels", levelname)
        self.savepath = os.path.join(os.path.dirname(dir_name), "IA_solutions", levelname)
        file = open(self.levelname, 'r')
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
        print("A*...")
        t0 = time.time()
        while len(self.ouverts) != 0:
            courant = self.ouverts.pop(0)
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
                        etat.eur = courant.eur + euristiques.euristique(etat)
                        etat.parent = courant
                        self.ouverts.add(etat)
            self.fermes.append(courant)
        t1 = time.time()
        print("A* time: " + str(t1-t0) + "\nsaving solution...")
        file = open(self.savepath, 'w')
        self.saveIA(courant, file)
        file.close()
        print("saved solution in: " + self.savepath)


if __name__ == "__main__":
    argv = sys.argv
    args = len(argv)
    if args <= 1:
        filename = input("level name: ")
    else:
        filename = argv[1]
    AStar(filename, True).mainLoop()
    print("FIN")