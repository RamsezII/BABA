from genericpath import isfile

import Etat

if __name__ == "__main__":    

    print("  -- BABA IS YOU! --\nmove with ZQSD keys")
    level0_path = "./levels/level_0.txt"
    if isfile(level0_path):
        etat = Etat.Etat(level0_path)
        while not etat.checkwin():
            print(etat)

            inp = input("move: ").lower()

            if inp == 'r':
                print("rewind")
            else:
                dir = [0,0]

                if inp == 'z': dir[0]-=1
                if inp == 'd': dir[1]+=1
                if inp == 's': dir[0]+=1
                if inp == 'q': dir[1]-=1    

                if dir != [0,0]:
                    etat = etat.move(dir)
    else:
        print("no savefile at: " + level0_path)    

    print("FIN")
