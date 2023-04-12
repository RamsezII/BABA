
import CORE.Etat
from CORE.Data import *
from IA.EtatIA import *
import IA.Distances as Distances
from UTIL.Util import *


def heuristique(etatIA:EtatIA):    

    value = MAX_INT

    if BABAf.WIN in etatIA.reachables and BABAf.IS in etatIA.reachables:
        pos_win = etatIA.reachables[BABAf.WIN][0]

        for IS_pos in etatIA.reachables[BABAf.IS]:
            dirf = DIRf.none
            for i in range(4):
                pos = IS_pos + Etat.yxi_dirs[i]
                if CORE.Etat.isInBounds(pos) and etatIA.distYous[pos.i] < MAX_INT:
                    dirf |= DIRf(1 << i)

            if DIRf.up_down in dirf or DIRf.left_right in dirf:
                for wordf in word2obj:
                    objf = word2obj[wordf]

                    if wordf in etatIA.reachables and objf in etatIA.reachables:
                        
                        # d'abord WIN vers suffixe de IS, puis mot vers prefixe de IS
                        
                        # if WIN suffixe de IS
                        #    heur = dist(mot,you) + dist(suf,mot) + dist(WC,you)
                        # else
                        #    heur = dist(WIN,you) + dist(pref,WIN) + dist(pref,mot) + dist(suf,mot) + dist(WC,you)

                        if DIRf.up_down in dirf:
                            dir = Etat.yxi_down.i
                        else:
                            dir = Etat.yxi_right.i

                        dists_pref = Distances.getDistances(etatIA, IS_pos.i - dir)
                        dists_suf = Distances.getDistances(etatIA, IS_pos.i + dir)

                        pos_word = etatIA.reachables[wordf][0]
                        
                        heur = 0

                        # si WIN n'est pas encore en suffixe
                        if Distances.getDistance(dists_suf, pos_win) != 0:
                            # distance de you à WIN
                            dists_win = Distances.getDistances(etatIA, pos_win.i)
                            dist_youWin = MAX_INT
                            for you in etatIA.yous:
                                dist_youWin = min(dist_youWin, Distances.getDistance(dists_win, you))
                            heur += dist_youWin

                            # distance de WIN à IS
                            heur += Distances.getDistance(dists_suf, pos_win)

                            # distances restantes, donc you(partant de IS) au mot, puis le mot à IS, donc 2*dist(IS, mot)
                            heur += 2 * Distances.getDistance(dists_suf, pos_word)

                        else:
                            # aller vers le mot
                            dists_mot = Distances.getDistances(etatIA, pos_word.i)
                            dist_youMot = MAX_INT
                            for you in etatIA.yous:
                                dist_youMot = min(dist_youMot, Distances.getDistance(dists_mot, you))
                            heur += dist_youMot

                            # pousser le mot en IS
                            heur += Distances.getDistance(dists_pref, pos_word)

                        # aller vers le WIN CLAIR
                        dists_winClair = Distances.getDistances(etatIA, (pos.i for pos in etatIA.reachables[objf]))
                        heur += Distances.getDistance(dists_winClair, IS_pos)
                            
                        return heur
                        value = min(value, heur)
        
    return value

