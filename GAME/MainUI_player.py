import pygame

import Main
import Screen


if __name__ == "__main__":    
    main = Main.Main("./levels/level_1.txt")
    screen = Screen.Screen(main)

    while main.running:
        deltatime = screen.deltatime(10)
        dir = [0,0]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main.running = False
                break
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
                    main.rewind()                
                elif not main.etat.win:
                    # min et max pour eviter accumulation
                    if event.key == pygame.K_z:
                        dir[0] = max(-1, dir[0]-1)
                    elif event.key == pygame.K_d:
                        dir[1] = min(1, dir[1]+1)
                    elif event.key == pygame.K_s:
                        dir[0] = min(1, dir[0]+1)
                    elif event.key == pygame.K_q:
                        dir[1] = max(-1, dir[1]-1)
        
        if main.running:
            if dir[0] != dir[1]:
                main.move(dir)
            
            if main.changed:
                main.changed = False
                screen.refresh(main.etat)
                print("stack:", len(main.etats))
                print(main.etat.logRules())
                # print(etat.logEtat())

                if main.etat.win:
                    print("WIN!")
                elif main.etat.defeat:
                    print("DEFEAT")

    print("FIN")
