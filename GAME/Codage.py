from enum import IntFlag

flags_count = 19

class Flags(IntFlag):
    empty = 0
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
    baba = 1 << 13
    wall = 1 << 14
    rock = 1 << 15
    flag = 1 << 16
    lava = 1 << 17
    water = 1 << 18

    def hasflags(self, flag): # OR
        return self & flag

    def hasmask(self, mask): # AND
        return self & mask == mask
    
    def flags(self):
        if self >= 0:
            for i in range(19):
                flag = Flags(1 << i)
                if self & flag:
                    yield flag,i
    
    # def flags(self):
    #     if self >= 0:
    #         for flag in Flags:
    #             if self.hasflags(flag):
    #                 yield flag
    
    def textcode(self):
        if self == 0:
            return ".."
        else:
            for i in range(17):
                flag = Flags(1 << i)
                if self.hasflags(flag):
                    return f"{i:02d}"
        return "??"


words = Flags.BABA | Flags.WALL | Flags.ROCK | Flags.FLAG | Flags.LAVA | Flags.WATER | Flags.IS | Flags.YOU | Flags.SINK | Flags.WIN | Flags.DEFEAT | Flags.PUSH | Flags.SOLID
objects = Flags.baba | Flags.wall | Flags.rock | Flags.flag | Flags.lava | Flags.water
first_obj = 13

word2obj = {
    Flags.BABA: 0,
    Flags.WALL: 1,
    Flags.ROCK: 2,
    Flags.FLAG: 3,
    Flags.LAVA: 4,
    Flags.WATER: 5,
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

    print()
    print("FIN")