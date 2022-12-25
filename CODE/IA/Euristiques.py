import sortedcontainers.sortedset


def euristique(etat):
    return distances(etat)


def distances(etat):
    dists = sortedcontainers.sortedset.SortedSet()
    for you in etat.yous:
        dists.add(etat.dists[you.pos.i])
    count = len(dists)    
    man = 0
    for i,dist in enumerate(dists):
        man += dist * (count-i)
    man /= count*(count+1)/2    
    return man


def manhattan2(self):
    wins = set()
    yous = set()

    for you in self.yous:
        yous.add((you[0]//self.width, you[0]%self.width))
    for win in self.wins:
        wins.add((win//self.width, win%self.width))

    dists = sortedcontainers.sortedset.SortedSet()
    for win in wins:
        for you in yous:
            h = abs(win[0]-you[0])
            w = abs(win[1]-you[1])
            dists.add(pow(h*h + w*w, 0.5))
    count = len(dists)
    
    man = 0
    for i,x in enumerate(dists):
        man += x * (count-i)
    man /= count*(count+1)/2
    
    return man


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
