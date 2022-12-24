class yxi():
    def __init__(self, y=0, x=0, i=0):
        self.y = y
        self.x = x
        self.i = i
    
    def __repr__(self) -> str:
        return "(y: " + str(self.y) + ", y: " + str(self.x) + ", i: " + str(self.i) + ")"
        
    def __add__(self, o):
        return yxi(self.y+o.y, self.x+o.x, self.i+o.i)

    def iszero(self):
        return self.y == self.x == self.i == 0
