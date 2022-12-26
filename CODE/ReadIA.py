import os.path

from CORE.Etat import Etat
from CORE.Move import move
from IA.EtatIA import EtatIA
from UI.UI_pygame import *
from UTIL.Path import *
from UTIL.SysArgs import sysArgs


def readIA(levelname, fps):
    etat = Etat(levelname)
    screen = Screen(etat)
    screen.refresh(etat)
    screen.deltatime(1)

    lines_sol = getlines(os.path.join(rootpath(), "IA_solutions", levelname))

    for line in lines_sol:
        if getQuit():
            break
        else:
            for dir in Etat.yxi_dirs:
                if line.startswith(str(dir)):
                    move(etat, dir)
                    break
        screen.refresh(etat)
        if fps != 0:
            screen.deltatime(fps)
    
    while not getQuit():
        screen.deltatime(10)


if __name__ == "__main__":
    args = sysArgs("-fps", "-level")

    if "-fps" in args:
        fps = int(args["-fps"])
    else:
        fps = 0
    
    if "-level" in args:
        levelname = args["-level"]
    else:
        levelname = input("level: ")
        
    readIA(levelname, fps)    
    print("FIN")