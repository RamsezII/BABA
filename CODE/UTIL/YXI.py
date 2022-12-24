

class yxi():
    def __init__(self, y, x, i):
        self.y = y
        self.x = x
        self.i = i
    
    def __repr__(self) -> str:
        return "(y: " + str(self.y) + ", x: " + str(self.x) + ", i: " + str(self.i) + ")"
        
    def __add__(self, o):
        return yxi(self.y+o.y, self.x+o.x, self.i+o.i)
    
    def __sub__(self, o):
        return yxi(self.y-o.y, self.x-o.x, self.i-o.i)

    def __neg__(self):
        return yxi(-self.y,-self.x,-self.i)

    def iszero(self):
        return self.y == self.x == self.i == 0



if __name__ == "__main__":

    a = yxi(2,5,4)
    b = yxi(8,4,1)
    c = -a
    print(a+b)
    print(a-b)
    print(c)

    print("FIN")