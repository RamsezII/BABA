
from UTIL.Util import *
from IA.EtatIA import *


def heuristique(etatIA:EtatIA):
    value = MAX_INT
    
    # si un IS et deux mots
    if BABAf.IS in etatIA.reachables:
        print("enfermement?")
        w1, w2 = BABAf(0), BABAf(0)
        for w in etatIA.reachables:
            if w != BABAf.IS and w in word2obj:
                if w1 == BABAf(0):
                    w1 = w
                elif w2 == BABAf(0):
                    w2 = w
                else:
                    print("enfermement: plus de 2 mots")
                    break
        print("enferemment: w1=", w1, "w2=", w2)
        
    
    return value