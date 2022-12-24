import os
import sys

import CORE.Etat
import MainIA
import UI

dir_name = os.path.dirname(os.path.abspath(__file__))

def run(filename):
    file = open(os.path.join(os.path.dirname(dir_name), "levels", filename), 'r')
    lines = file.readlines()
    file.close()

    etat = Etat.Etat()
    etat.readtext(lines)
       
    file = open(os.path.join(os.path.dirname(dir_name), "IA_solutions", filename), 'r')
    lines = file.readlines()
    file.close()

    screen = UI.Screen(etat)
    screen.refresh(etat)
    screen.deltatime(1)

    fps = 5

    for line in lines:
        if UI.getQuit():
            break
        for i in range(0, 4):
            if line.startswith(MainIA.dirs[i]):
                etat.move(i+1)
                break
        screen.refresh(etat)
        screen.deltatime(fps)
    
    while not UI.getQuit():
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
