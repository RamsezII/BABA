import pygame

from UTIL.SysArgs import sysArgs
from CORE.Etat import Etat
from CORE.Move import move
from IA.EtatIA import EtatIA
from UI.UI_pygame import Screen
from UTIL.YXI import YXI


if __name__ == "__main__":
    args = sysArgs("-fps", "-level")

    if "-fps" in args:
        fps = int(args["-fps"])
    else:
        fps = 0
    
    if "-level" in args:
        levelname = args["-level"]
    else:
        # levelname = input("level: ")
        # levelname = "small.txt"
        # levelname = "level_WPC1.txt"
        levelname = "level_ENF.txt"

    etat = EtatIA(levelname)
    screen = Screen(etat)
    fps = 30
    running = True

    while running:
        dir_yxi: YXI = YXI(0,0,0)
        dirflag = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    if etat.parent:
                        etat = etat.parent
                        etat.changed = True
                elif not (dirflag or etat.win or etat.defeat):
                    dirflag = True
                    if event.key == pygame.K_z:
                        dir_yxi += Etat.yxi_up
                    if event.key == pygame.K_d:
                        dir_yxi += Etat.yxi_right
                    if event.key == pygame.K_s:
                        dir_yxi += Etat.yxi_down
                    if event.key == pygame.K_q:
                        dir_yxi += Etat.yxi_left
        
        if running:
            if not (etat.win or etat.defeat or dir_yxi.iszero()):
                clone = etat.copy()
                move(clone, dir_yxi)
                if clone.changed:
                    clone.parent = etat
                    etat = clone
            
            if etat.pullChange():
                # etat.logRules()
                # etat.logEtat()
                screen.refresh(etat)
                # etat.getDistances()
                # etat.logYousDistances()

                if etat.win:
                    print("WIN!")
                elif etat.defeat:
                    print("DEFEAT")
        
        deltatime = screen.deltatime(fps)
    print("FIN")
