import time
import pygame

import Main
import UI


if __name__ == "__main__":    
    main = Main.Main("level_1.txt")
    screen = UI.Screen(main)

    while main.running:
        dir = 0
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
                    if event.key == pygame.K_z:
                        dir = -main.etat.width
                    elif event.key == pygame.K_d:
                        dir = 1
                    elif event.key == pygame.K_s:
                        dir = main.etat.width
                    elif event.key == pygame.K_q:
                        dir = -1
        
        if main.running:
            if dir != 0:
                print("move...")
                t0_move = time.time()
                main.move(dir)
                t1_move = time.time()
                print("move time: " + str(t1_move-t0_move) + '\n')
            
            if main.changed:
                main.changed = False
                screen.refresh(main.etat)
                # print("stack:", len(main.etats))
                # print(main.etat.logRules())
                # print(etat.logEtat())

                if main.etat.win:
                    print("WIN!")
                elif main.etat.defeat:
                    print("DEFEAT")
        
        deltatime = screen.deltatime(30)

    print("FIN")
