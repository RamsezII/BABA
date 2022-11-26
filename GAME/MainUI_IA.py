import math
import pygame

import Main
import Screen


if __name__ == "__main__":    
    # fps = int(input("fps: "))
    # fps = 15
    main = Main.Main("./levels/level_IA_01.txt")
    screen = Screen.Screen(main)
    
    while main.running:
        # deltatime = screen.deltatime(fps)

        for event in pygame.event.get():
            e = event.type

            if event.type == pygame.QUIT:
                main.running = False
                break

            elif event.type == pygame.KEYDOWN:
                # utiliser terminal
                if event.key == pygame.K_p:
                    splits = (input(">")).split(' ')
                    command = splits[0]
                    if command == "load":
                        print("load: ", splits[1])
                    elif command == "quit":
                        print("quit!")
                        running = False                        
        
        if main.running and not main.etat.win:
            succs = main.successeurs()
            count = len(succs)
            if count == 0:
                print("NO SUCCS")
                break
            elif count == 1:
                main.etat = succs[0]
            else:
                eur_min = math.inf
                next = None
                for x in succs:
                    eur = x.manhattan()
                    if eur < eur_min:
                        eur_min = eur
                        next = x
                main.apply(next)
            
            if main.etat.changed:
                main.etat.changed = False
                screen.refresh(main.etat)
                print("stack:", len(main.etats))
                # print(main.etat.logRules())
                # print(etat.logEtat())

                if main.etat.win:
                    print("WIN!")
                elif main.etat.defeat:
                    print("DEFEAT")

    print("FIN")
