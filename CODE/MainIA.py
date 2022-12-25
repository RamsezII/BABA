import os
import sortedcontainers.sortedlist
import time


dirs = ["up", "right", "down", "left"]


class AStar():
    def __init__(self, levelname, ui):
        self.levelname = os.path.join("levels", levelname)
        self.savepath = os.path.join("IA_solutions", levelname)
        file = open(self.levelname, 'r')
        lines = file.readlines()
        file.close()
        self.ouverts = sortedcontainers.sortedlist.SortedList()
        courant = Etat.Etat()
        ReadText(courant, lines)
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
        t0_main = time.time()
        t_next = time.time()+1
        loopcount = 0
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

            loopcount += 1
            t_loop = time.time()
            if t_loop > t_next:
                t_next += 1
                print("iterations: " + str(loopcount))
                loopcount = 0

        t1_main = time.time()
        print("A* time: " + str(t1_main-t0_main) + "\nsaving solution...")
        file = open(self.savepath, 'w')
        self.saveIA(courant, file)
        file.close()
        print("saved solution in: " + self.savepath)


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