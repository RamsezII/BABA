import sortedcontainers.sortedset


def euristique(etat):
    return distances(etat)


def distances(self):
    self.distances = self.width*self.height*()
    for win in self.wins:
        fifo = list(self.grid[0])
        while len(fifo)
        for i,flags in self.grid:
            if flags & self.collisionMask:
                self.distances = -1
            y,x = i//self.height,i%self.width
            for dir in self.dirs_yxi:
                if self.isInBounds_yx(y+dir[0][0],x+dir[0][1]):
                    flags2 = self.grid[dir[1]]



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
