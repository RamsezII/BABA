

class YXI():
    def __init__(self, y, x, i):
        self.y = y
        self.x = x
        self.i = i
    
    def __repr__(self) -> str:
        return "{: } {: }".format(self.y, self.x)
        
    def __add__(self, o):
        return YXI(self.y+o.y, self.x+o.x, self.i+o.i)
    
    def __sub__(self, o):
        return YXI(self.y-o.y, self.x-o.x, self.i-o.i)

    def __neg__(self):
        return YXI(-self.y,-self.x,-self.i)

    def iszero(self):
        return self.y == self.x == self.i == 0
    
    def __iter__(self):
        yield self.y
        yield self.x
        yield self.i



if __name__ == "__main__":

    a = YXI(2,5,4)
    b = YXI(8,4,1)
    c = -a
    print(a+b)
    print(a-b)
    print(c)

    print("FIN")