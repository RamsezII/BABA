import pygame

from CORE.Etat import Etat
from CORE.Move import move
from UI.UI_pygame import Screen
from UTIL.YXI import yxi


if __name__ == "__main__":
    etat = Etat("level_3.txt")
    etat.logEtat()
    screen = Screen(etat)
    fps = 30
    running = True

    while running:
        dir_yxi: yxi = yxi(0,0,0)
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
                clone = etat.clone()
                move(clone, dir_yxi)
                if clone.changed:
                    clone.parent = etat
                    etat = clone
            
            if etat.pullChange():
                etat.logRules()
                etat.logEtat()
                screen.refresh(etat)

                if etat.win:
                    print("WIN!")
                elif etat.defeat:
                    print("DEFEAT")
        
        deltatime = screen.deltatime(fps)

    print("FIN")
