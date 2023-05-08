
import CORE.Etat
from CORE.Data import *
from IA.EtatIA import *
import IA.Distances as Distances
from UTIL.Util import *


def heuristique(etatIA:EtatIA)->int:

    if BABAf.WIN in etatIA.reachables and BABAf.IS in etatIA.reachables:
        for win_i in etatIA.reachables[BABAf.WIN]:
            for IS_i in etatIA.reachables[BABAf.IS]:
                dirf = DIRf.none
                for i in range(4):
                    yxi = i2yxi(IS_i) + Etat.yxi_dirs[i]
                    if CORE.Etat.isInBounds(yxi) and not etatIA.grid[yxi.i]:
                        dirf |= DIRf(1 << i)

                if DIRf.up_down in dirf or DIRf.left_right in dirf:
                    for wordf in word2obj:
                        objf = word2obj[wordf]

                        if objf not in etatIA.rules[BABAf.YOU] and wordf in etatIA.reachables and objf in etatIA.reachables:
                            
                            if win_i == IS_i + Etat.yxi_down.i:
                                dir_i = Etat.yxi_down.i
                            elif win_i == IS_i + Etat.yxi_right.i:
                                dir_i = Etat.yxi_right.i
                            elif DIRf.up_down in dirf:
                                dir_i = Etat.yxi_down.i
                            else:
                                dir_i = Etat.yxi_right.i

                            pref_i = IS_i - dir_i
                            suff_i = IS_i + dir_i
                            pref_dists = Distances.getDistances(etatIA, pref_i)
                            suff_dists = Distances.getDistances(etatIA, suff_i)

                            word_i = etatIA.reachables[wordf][0]

                            # distance de WIN->SUFF
                            win2suff_dist = suff_dists[win_i]
                            heur = win2suff_dist

                            # si WIN est déjà en suffixe
                            if heur == 0:
                                # YOU->MOT
                                mot_dists = Distances.getDistances(etatIA, word_i)
                                you2mot_dist = MAX_INT
                                for you_i in etatIA.yous:
                                    you2mot_dist = min(you2mot_dist, mot_dists[you_i])
                                heur += you2mot_dist

                                # MOT->PREF
                                mot2pref_dist = pref_dists[word_i]
                                heur += mot2pref_dist

                            else:
                                # YOU->WIN
                                win_dists = Distances.getDistances(etatIA, win_i)
                                you2win_dist = MAX_INT
                                for you_i in etatIA.yous:
                                    you2win_dist = min(you2win_dist, win_dists[you_i])
                                heur += you2win_dist

                                # WIN->SUFF
                                win2suff_dist = suff_dists[win_i]
                                heur += win2suff_dist

                                # SUFF->MOT
                                suff2word_dist = suff_dists[word_i]
                                heur += suff2word_dist

                                # MOT->PREF
                                word2pref_dist = pref_dists[word_i]
                                heur += word2pref_dist

                            # aller vers le WIN CLAIR
                            WC_dists = Distances.getDistances(etatIA, etatIA.reachables[objf])
                            you2WC_dist = WC_dists[pref_i]
                            heur += you2WC_dist
                                
                            return heur
        
    return MAX_INT

