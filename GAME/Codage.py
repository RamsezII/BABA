from enum import IntFlag

flags_count = 19

class Flags(IntFlag):
    empty = 0
    # words
    BABA = 1 << 0
    WALL = 1 << 1
    ROCK = 1 << 2
    FLAG = 1 << 3
    LAVA = 1 << 4
    WATER = 1 << 5
    IS = 1 << 6
    YOU = 1 << 7
    SINK = 1 << 8
    WIN = 1 << 9
    DEFEAT = 1 << 10
    PUSH = 1 << 11
    SOLID = 1 << 12
    # objects in drawing order
    wall = 1 << 13
    lava = 1 << 14
    water = 1 << 15
    rock = 1 << 16
    flag = 1 << 17
    baba = 1 << 18
    
    def hasflags(self, flag): # OR
        return self & flag

    def hasmask(self, mask): # AND
        return self & mask == mask
    
    def flags(self):
        if self >= 0:
            for i in range(19):
                flag = Flags(1 << i)
                if self & flag:
                    yield i,flag
    
    def textcode(self):
        if self == 0:
            return ".."
        else:
            for i,_ in self.flags():
                return f"{i:02d}"
        return "??"


words = Flags.BABA | Flags.WALL | Flags.ROCK | Flags.FLAG | Flags.LAVA | Flags.WATER | Flags.IS | Flags.YOU | Flags.SINK | Flags.WIN | Flags.DEFEAT | Flags.PUSH | Flags.SOLID
objects = Flags.baba | Flags.wall | Flags.rock | Flags.flag | Flags.lava | Flags.water
first_obj = 13

word2obj = {
    Flags.WALL: 0,
    Flags.LAVA: 1,
    Flags.WATER: 2,
    Flags.ROCK: 3,
    Flags.FLAG: 4,
    Flags.BABA: 5,
}


if __name__ == "__main__":

    # # logflags
    # print()
    # i = 0
    # for x in Flags:
    #     if x != Flags.empty:
    #         print(x.name+" = 1 << " + str(i))
    #         i += 1
    
    # # log rule2obj
    # print()
    # for x in Flags:
    #     print("Flags." + x.name + ": Flags." + x.name + ",")

    # # log all|
    # print()
    # log = ""
    # for x in Flags:
    #     log += "Flags." + x.name + " | "
    # print(log)

    # # test iter
    # print()
    # for flag,i in (Flags.LAVA | Flags.PUSH | Flags.baba).flags():
    #     print(i, "|", flag.name)

    # # defaultRules
    # print()
    # for i,flag in enumerate((Flags.baba | Flags.wall | Flags.rock | Flags.flag | Flags.lava | Flags.water).flags(False)):
    #     print("0,  #", i, "|" + flag.name)

    print()
    print("FIN")