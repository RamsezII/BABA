import math
import time
import pygame

import Main
import UI

if __name__ == "__main__":    
    main = Main.Main("level_IA_01.txt")
    screen = UI.Screen(main)
    
    t0 = time.time()

    while main.running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main.running = False
                break                     
        
        if main.running and not main.etat.win:
            succs = main.successeurs()
            count = len(succs)
            if count == 0:
                print("rewind")
                if len(main.etats) == 0:
                    print("block")
                    main.running = False
                    break
                else:
                    main.rewind()
            elif count == 1:
                main.apply(succs[0])
            else:
                eur_min = math.inf
                next = None
                for x in succs:
                    eur = x.manhattan()
                    if eur < eur_min:
                        eur_min = eur
                        next = x
                main.apply(next)
            
            if main.changed:
                main.changed = False
                screen.refresh(main.etat)
                # print("stack:", len(main.etats))
                # print(main.etat.logRules())
                # print(main.etat.logEtat())

                if main.etat.win:
                    print("WIN!")
                    t1 = time.time()
                    print("time:", t1-t0)
                elif main.etat.defeat:
                    print("DEFEAT")

    print("FIN")
