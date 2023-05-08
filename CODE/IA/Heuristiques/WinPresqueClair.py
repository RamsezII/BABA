
import CORE.Etat
from CORE.Data import *
from IA.EtatIA import *
import IA.Distances as Distances
from UTIL.Util import *


def heuristique(etatIA:EtatIA)->int:

    if BABAf.WIN in etatIA.reachables and BABAf.IS in etatIA.reachables:
        for win_yxi in etatIA.reachables[BABAf.WIN]:
            for IS_yxi in etatIA.reachables[BABAf.IS]:
                dirf = DIRf.none
                for i in range(4):
                    yxi = IS_yxi + Etat.yxi_dirs[i]
                    # if CORE.Etat.isInBounds(pos) and etatIA.distYous[pos.i] < MAX_INT:
                    if CORE.Etat.isInBounds(yxi) and not etatIA.grid[yxi.i]:
                        dirf |= DIRf(1 << i)

                if DIRf.up_down in dirf or DIRf.left_right in dirf:
                    for wordf in word2obj:
                        objf = word2obj[wordf]

                        if objf not in etatIA.rules[BABAf.YOU] and wordf in etatIA.reachables and objf in etatIA.reachables:
                            
                            # d'abord WIN vers suffixe de IS, puis mot vers prefixe de IS
                            
                            # if WIN suffixe de IS
                            #    heur = dist(mot,you) + dist(suf,mot) + dist(WC,you)
                            # else
                            #    heur = dist(WIN,you) + dist(pref,WIN) + dist(pref,mot) + dist(suf,mot) + dist(WC,you)

                            if win_yxi == IS_yxi + Etat.yxi_down:
                                dir = Etat.yxi_down
                            elif win_yxi == IS_yxi + Etat.yxi_right:
                                dir = Etat.yxi_right
                            elif DIRf.up_down in dirf:
                                dir = Etat.yxi_down
                            else:
                                dir = Etat.yxi_right

                            pref_yxi = IS_yxi - dir
                            suff_yxi = IS_yxi + dir
                            pref_dists = Distances.getDistances(etatIA, pref_yxi.i)
                            suff_dists = Distances.getDistances(etatIA, suff_yxi.i)

                            word_yxi = etatIA.reachables[wordf][0]

                            # distance de WIN->SUFF
                            win2suff_dist = suff_dists[win_yxi.i]
                            heur = win2suff_dist

                            # si WIN est déjà en suffixe
                            if heur == 0:
                                # YOU->MOT
                                mot_dists = Distances.getDistances(etatIA, word_yxi.i)
                                you2mot_dist = MAX_INT
                                for you_i in etatIA.yous:
                                    you2mot_dist = min(you2mot_dist, mot_dists[you_i])
                                heur += you2mot_dist

                                # MOT->PREF
                                mot2pref_dist = pref_dists[word_yxi.i]
                                heur += mot2pref_dist

                            else:
                                # YOU->WIN
                                win_dists = Distances.getDistances(etatIA, win_yxi.i)
                                you2win_dist = MAX_INT
                                for you_i in etatIA.yous:
                                    you2win_dist = min(you2win_dist, win_dists[you_i])
                                heur += you2win_dist

                                # WIN->SUFF
                                win2suff_dist = suff_dists[win_yxi.i]
                                heur += win2suff_dist

                                # SUFF->MOT
                                suff2word_dist = suff_dists[word_yxi.i]
                                heur += suff2word_dist

                                # MOT->PREF
                                word2pref_dist = pref_dists[word_yxi.i]
                                heur += word2pref_dist

                            # aller vers le WIN CLAIR
                            WC_dists = Distances.getDistances(etatIA, (pos.i for pos in etatIA.reachables[objf]))
                            you2WC_dist = WC_dists[pref_yxi.i]
                            heur += you2WC_dist
                                
                            return heur
        
    return MAX_INT

