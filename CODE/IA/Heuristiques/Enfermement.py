
from UTIL.Util import *
from IA.EtatIA import *
from IA.Distances import *


def heuristique(etatIA:EtatIA)->int:
    # si un IS et deux mots
    if BABAf.IS in etatIA.reachables:
        w1, w2 = BABAf(0), BABAf(0)
        for w in etatIA.reachables:
            if w != BABAf.IS and w in words_mask:
                if w1 == BABAf(0):
                    w1 = w
                elif w2 == BABAf(0):
                    w2 = w
                else:
                    print("enfermement: plus de 2 mots")
                    break
        if w1 != 0 and w2 != 0:
            # trois situations :
            #  - loi non formée
            #  - formée dans un sens
            #  - et dans l'autre sens
            
            cell_IS = etatIA.reachables[BABAf.IS][0]
            cell_pref = etatIA.reachables[w1][0]
            cell_suf = etatIA.reachables[w2][0]

            if cell_suf - cell_IS == cell_IS - cell_pref:
                # loi formée
                dists = getDistances(etatIA, (cell_pref.i, cell_suf.i))
                heur = getMinDistance(dists, etatIA.yous)
                heur += int(MAX_INT/2)
                return heur
            else:
                print("error enfermement: loi non formée")
                pass
    
    return MAX_INT