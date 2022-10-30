from genericpath import isfile

import Etat

if __name__ == "__main__":    

    print("  -- BABA IS YOU! --\nmove with ZQSD keys")
    level0_path = "level_0.txt"
    if isfile(level0_path):
        etat = Etat.Etat(level0_path)
        while not etat.checkwin():
            print(etat)
            etat.play()
    else:
        print("no savefile at: " + level0_path)    

    print("FIN")

