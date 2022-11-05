import genericpath
import os

import Etat

WDIR = os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":    
    level0_path = "./levels/level_2.txt"

    if not genericpath.isfile(level0_path):
        print("no savefile at:", level0_path)
    else:
        etat = Etat.Etat()
        etat.init(level0_path)
        etats = []
        running = True

        print(etat.logRules())
        print(etat.logEtat())

        while running:
            dir = [0,0]
            join = input(">")
            splits = join.split(' ')
            command = splits[0].lower()

            if command == 'r':
                if len(etats) != 0:
                    etat = etats.pop()
                    etat.changed = True
            elif command in "zqsd":
                dir = [0,0]

                if command == 'z': dir[0]-=1
                if command == 'd': dir[1]+=1
                if command == 's': dir[0]+=1
                if command == 'q': dir[1]-=1    

                if dir != [0,0]:
                    etat = etat.clone()
                    etat.move(dir)
            elif command == "load":
                print("load: ", splits[1])
            elif command == "quit":
                print("quit!")
                running = False
            
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
                    print("stack:", len(etats))
                    print(etat.logRules())
                    print(etat.logEtat())
                    if etat.win:
                        print("WIN!")
                    elif etat.defeat:
                        print("DEFEAT")

    print("FIN")