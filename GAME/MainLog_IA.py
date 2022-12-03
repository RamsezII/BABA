import math
import time

import Main

if __name__ == "__main__":    
    main = Main.Main("level_IA_01.txt")
    fps = 0

    print(main.etat.logEtat())
    t0_main = time.time()
    
    while main.running:
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
                    eur = x.euristique()
                    if eur < eur_min:
                        eur_min = eur
                        next = x
                main.apply(next)
            
            if main.changed:
                main.changed = False
                # print("stack:", len(main.etats))
                # print(main.etat.logRules())
                # print(main.etat.logEtat())

                if main.etat.win:
                    print("WIN!")
                    break
                elif main.etat.defeat:
                    print("DEFEAT")
                    break
    
    print(main.etat.logEtat())
    t1_main = time.time()
    print("main time " + str(t1_main-t0_main))
    print("FIN")
