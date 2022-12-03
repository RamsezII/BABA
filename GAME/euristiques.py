def euristique(etat):
    return manhattan(etat)

def manhattan(self):
    wins = set()
    yous = set()
    for you in self.yous:
        yous.add((you[0]//self.width, you[0]%self.width))
    for win in self.wins:
        wins.add((win//self.width, win%self.width))

    man = self.height+self.width
    for win in wins:
        for you in yous:
            h = abs(win[0]-you[0])
            w = abs(win[1]-you[1])
            dist = pow(h*h + w*w, 0.5)
            if dist < man:
                man = dist
    return man