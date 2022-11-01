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
        screen = Screen.Screen()
        running = True

        while running:
            deltatime = screen.deltatime(10)
            dir = [0,0]

            for event in pygame.event.get():
                e = event.type
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        splits = (input(">")).split(' ')
                        command = splits[0]
                        if command == "load":
                            print("load: ", splits[1])
                        elif command == "quit":
                            print("quit!")
                            running = False
                    elif event.key == pygame.K_r:
                        if len(etats) != 0:
                            etat = etats.pop()
                            etat.changed = True
                    elif event.key == pygame.K_z:
                        dir[0] -= 1
                    elif event.key == pygame.K_d:
                        dir[1] += 1
                    elif event.key == pygame.K_s:
                        dir[0] += 1
                    elif event.key == pygame.K_q:
                        dir[1] -= 1

            if dir[0] != dir[1]:
                etats.append(etat)
                etat = etat.clone()
                etat.move(dir)
                if not etat.changed:
                    etat = etats.pop()
            
            if etat.changed:
                etat.changed = False
                screen.refresh(etat)
                print("stack:", len(etats))
                print(etat.logRules())
                print(etat.logEtat())
    else:
        print("no savefile at:", level0_path)

    print("FIN")
