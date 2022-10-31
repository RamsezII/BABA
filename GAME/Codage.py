from enum import IntFlag


class Flags(IntFlag):
    empty = 0
    BABA = 1 << 0,
    WALL = 1 << 1,
    ROCK = 1 << 2,
    FLAG = 1 << 3,
    LAVA = 1 << 4,
    WATER = 1 << 5,
    IS = 1 << 6,
    YOU = 1 << 7,
    SINK = 1 << 8,
    WIN = 1 << 9,
    DEFEAT = 1 << 10,
    baba = 1 << 11,
    wall = 1 << 12,
    rock = 1 << 13,
    flag = 1 << 14,
    lava = 1 << 15,
    water = 1 << 16,

    def hasflags(self, flag): # OR
        return self & flag

    def hasmask(self, mask): # AND
        return self & mask == mask
    
    def textcode(self):
        if self == 0:
            return ".."
        else:
            for i in range(17):
                flag = Flags(1 << i)
                if self.hasflags(flag):
                    return f"{i:02d}"
        return "??"


ruleFlags = Flags.BABA | Flags.WALL | Flags.ROCK | Flags.FLAG | Flags.LAVA | Flags.WATER | Flags.YOU | Flags.SINK | Flags.WIN | Flags.DEFEAT

obj2rule = {
    Flags.baba: Flags.BABA,
    Flags.wall: Flags.WALL,
    Flags.rock: Flags.ROCK,
    Flags.flag: Flags.FLAG,
    Flags.lava: Flags.LAVA,
    Flags.water: Flags.WATER,
}


if __name__ == "__main__":

    # logflags
    print()
    i = 0
    for x in Flags:
        if x != Flags.empty:
            print(x.name+" = 1 << " + str(i))
            i += 1

    # log ruleFlags
    # print()
    # log = ""
    # for x in Flags:
    #     log += "Flags." + x.name + " | "
    # print(log)

    print()
    print("FIN")