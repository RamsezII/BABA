import genericpath
import pygame

import Screen
import Etat

if __name__ == "__main__":    
    level0_path = "./levels/level_0.txt"

    if genericpath.isfile(level0_path):
        etat = Etat.Etat()
        etat.init(level0_path)
        etats = []
        screen = Screen.Screen(etat.w, etat.h)
        running = True

        while running:
            deltatime = screen.deltatime(10)
            dir = [0,0]

            for event in pygame.event.get():
                e = event.type

                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.KEYDOWN:
                    # passer en mode terminal
                    if event.key == pygame.K_p:
                        splits = (input(">")).split(' ')
                        command = splits[0]
                        if command == "load":
                            print("load: ", splits[1])
                        elif command == "quit":
                            print("quit!")
                            running = False

                    # rewind
                    elif event.key == pygame.K_r:
                        if len(etats) != 0:
                            etat = etats.pop()
                            etat.changed = True
                    
                    # quand l'execution est lente (debug), l'appui de touche répétée a le temps de créer une accumulation
                    elif not etat.win:
                        if event.key == pygame.K_z:
                            dir[0] = max(-1, dir[0]-1)
                        elif event.key == pygame.K_d:
                            dir[1] = min(1, dir[1]+1)
                        elif event.key == pygame.K_s:
                            dir[0] = min(1, dir[0]+1)
                        elif event.key == pygame.K_q:
                            dir[1] = max(-1, dir[1]-1)
            
            if not etat.win:
                if dir[0] != dir[1]:
                    etats.append(etat)
                    etat = etat.clone()
                    etat.move(dir)
                    if etat.changed:
                        if etat.win:
                            print("WIN!")
                    else:
                        etat = etats.pop()
                if etat.changed:
                    etat.changed = False
                    screen.refresh(etat)
                    print("stack:", len(etats))
                    print(etat.logRules())
                    # print(etat.logEtat())
                    if etat.defeat:
                        print("DEFEAT")
    else:
        print("no savefile at:", level0_path)

    print("FIN")
