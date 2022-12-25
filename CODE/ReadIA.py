import os.path

from CORE.Etat import Etat
from CORE.Move import move
from IA.EtatIA import EtatIA
from UI.UI_pygame import *


def run(levelname):
    rootdir = os.path.abspath(__file__)
    rootdir = os.path.dirname(rootdir)
    rootdir = os.path.dirname(rootdir)
    rootdir = os.path.dirname(rootdir)
    print("rootdir:", rootdir)
    file = open(os.path.join("levels", levelname), 'r')
    lines = file.readlines()
    file.close()

    etat = Etat(levelname)
    screen = Screen(etat)
    screen.refresh(etat)
    screen.deltatime(1)

    fps = 5

    for line in lines:
        if getQuit():
            break
        else:
            for i in range(0, 4):
                if line.startswith(EtatIA.dirs[i]):
                    move(etat, Etat.yxi_dirs[i])
                    break
        screen.refresh(etat)
        screen.deltatime(fps)
    
    while not getQuit():
        screen.deltatime(10)

if __name__ == "__main__":
    # argv = sys.argv
    # args = len(argv)

    # if args <= 1:
    #     filename = input("level name : ")
    # else:
    #     filename = argv[1]
    filename = "level_IA_03.txt"
    run(filename)
    
    print("FIN")
