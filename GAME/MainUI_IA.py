import pygame

import Main
import Screen

import euristiques


if __name__ == "__main__":    
    main = Main("./levels/level_IA_01.txt")
    screen = Screen.Screen(main)
    fps = int(input("fps: "))
    
    while main.running:
        deltatime = screen.deltatime(10)

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
        
        if main.running:
            succs = main.successeurs()
            succs.sort(key=euristiques.euristique_target)
            
            if len(succs) > 1:
                main.etat = succs[0]
            
            if main.etat.changed:
                main.etat.changed = False
                screen.refresh(main.etat)
                print("stack:", len(main.etats))
                print(main.etat.logRules())
                # print(etat.logEtat())

                if main.etat.win:
                    print("WIN!")
                elif main.etat.defeat:
                    print("DEFEAT")

    print("FIN")
