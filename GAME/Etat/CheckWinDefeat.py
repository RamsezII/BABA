from Etat.Codage import *


def checkWinDefeat(self):
    # on gagne si un des flags représentant les objets d'une case, a son correspondant dans 'self.rules' marqué comme 'YOU' et 'WIN'
    # on perd si aucune case n'a d'objet correspondant dans 'self.rules' marqué comme 'YOU'
    self.defeat = True
    self.win = False
    self.yous.clear()
    self.wins.clear()
    for k,flags in enumerate(self.grid):
        you = False
        win = False
        for i,flag in flags.flags(BABAb.first_obj, BABAb.last_all):
            rule = self.rules[i-BABAb.first_obj]
            if BABAf.YOU in rule:
                you = True
                self.defeat = False
                self.yous.append((k,flag))
            if BABAf.WIN in rule:
                win = True
                self.wins.add(k)
        if you and win:
            self.win = True
            break