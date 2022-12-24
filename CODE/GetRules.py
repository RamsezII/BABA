from CODE.Data import *


def getRules(self):
    # un bitmask par objet (6 au total). si "BABA IS YOU" est visible dans le niveau, le flag 'YOU' dans le bitmask de 'baba' dans 'self.rules' sera à 1
    # dans le cas d'une transformation, par exemple "BABA IS ROCK", toutes les cases sont parcourues et chaque case où le flag 'baba' est à 1 est mis à 0 et le flag 'rock' est mis à 1
    self.rules = 6*[BABAf.none]
    for k in range(self.count):
        if BABAf.IS in self.grid[k]:
            for dir in (self.w, 1):  # les 2 sens de lectures: vers le bas et vers la droite
                if self.isInBounds(k-dir) and self.isInBounds(k+dir):
                    prefixes = self.grid[k-dir]
                    suffixes = self.grid[k+dir]
                    if prefixes * suffixes != 0 and prefixes & words_mask and suffixes & words_mask:
                        for pref in word2obj:
                            if pref in prefixes:
                                for _,suf in suffixes.flags(0, BABAb.first_obj):
                                    self.rules[word2obj[pref]] |= suf
                                    # si suffixe désigne aussi un objet, c'est une loi de transformation
                                    if suf in word2obj:
                                        pref_obj = BABAf(1 << (word2obj[pref]+BABAb.first_obj))
                                        suf_obj = BABAf(1 << (word2obj[suf]+BABAb.first_obj))
                                        for k2 in range(self.count):
                                            if self.grid[k2] & pref_obj:
                                                self.grid[k2] &= ~pref_obj
                                                self.grid[k2] |= suf_obj        
    self.m_cols = BABAf.none
    for i,rule in enumerate(self.rules):
        if rule & BABAf.SOLID:
            self.m_cols |= BABAf(1 << (BABAb.first_obj + i))