import genericpath
import pygame

import Screen
import Etat

if __name__ == "__main__":    
    level0_path = "./levels/level_0.txt"

    if genericpath.isfile(level0_path):
        etat = Etat.Etat(level0_path)
        running = True

        while running:
            deltatime = Screen.vsync()
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
                        print("rewind")
                    elif event.key == pygame.K_z:
                        dir[0] -= 1
                    elif event.key == pygame.K_d:
                        dir[1] += 1
                    elif event.key == pygame.K_s:
                        dir[0] += 1
                    elif event.key == pygame.K_q:
                        dir[1] -= 1

            if dir[0] != dir[1]:
                etat = etat.move(dir)
                Screen.setdirty = True
            
            if Screen.setdirty:
                Screen.setdirty = False
                Screen.refresh(etat)
                print(etat)
    else:
        print("no savefile at:", level0_path)

    print("FIN")
