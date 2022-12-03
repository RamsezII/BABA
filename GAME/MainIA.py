import os
import sortedcontainers.sortedlist
import time

import Etat
import euristiques
import UI


class AStar():
    def __init__(self, levelname, ui):
        file = open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "levels", levelname), 'r')
        lines = file.readlines()
        file.close()
        self.ouverts = sortedcontainers.sortedlist.SortedList()
        courant = Etat.Etat()
        courant.readtext(lines)
        self.ouverts.add(courant)
        self.fermes = []
        self.ui = ui
    

    def mainLoop(self):
        print("A*...")
        t0_astar = time.time()
        while len(self.ouverts) != 0:
            courant = self.ouverts.pop(0)
            if courant.win:
                print("WIN!")
                break
            elif courant.defeat:
                print("DEFEAT")
                break
            else:
                for dir in (-courant.width, 1, courant.width, -1):
                    etat = courant.clone()
                    etat.move(dir)
                    if etat.pullChange() and etat not in self.ouverts and etat not in self.fermes:
                        etat.eur = courant.eur + euristiques.euristique(etat)
                        etat.parent = courant
                        self.ouverts.add(etat)
            self.fermes.append(courant)
        t1_astar = time.time()
        print("astar: " + str(t1_astar-t0_astar))

        if self.ui:
            screen = UI.Screen(courant)
            screen.showSolution(courant, 5)
            while not UI.getQuit():
                screen.deltatime(15)
        
        print("FIN AStar")


if __name__ == "__main__":
    AStar("level_IA_01.txt", True).mainLoop()
    print("FIN")