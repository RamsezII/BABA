from enum import IntEnum, IntFlag

class BABAb(IntEnum):
    BABA = first_all = first_word = 0
    WALL = 1
    ROCK = 2
    FLAG = 3
    LAVA = 4
    WATER = 5
    IS = 6
    YOU = 7
    SINK = 8
    WIN = 9
    DEFEAT = 10
    PUSH = 11
    SOLID = 12
    wall = last_word = first_obj = 13
    lava = 14
    water = 15
    rock = 16
    flag = 17
    baba = 18
    last_all = last_obj = 19

class BABAf(IntFlag):
    none = 0
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
    
    def flags(self, mini, maxi):
        if self >= 0:
            for i in range(mini, maxi):
                flag = BABAf(1 << i)
                if self & flag:
                    yield i,flag
    
    def textcode(self):
        if self == 0:
            return ".."
        else:
            for i,_ in self.flags(0, BABAb.last_all):
                return f"{i:02d}"
        return "??"

class DIRf(IntFlag):
    none = 0
    up = 1 << 0
    down = 1 << 1
    left = 1 << 2
    right = 1 << 3
    up_down = up | down
    left_right = left | right
    all = up_down | left_right


words_mask = BABAf((1<<BABAb.last_word)-1)
objects_mask = words_mask ^ BABAf((1<<BABAb.last_all)-1)

word2obj = {
    BABAf.BABA : BABAf.baba,
    BABAf.WALL : BABAf.wall,
    BABAf.ROCK : BABAf.rock,
    BABAf.FLAG : BABAf.flag,
}


if __name__ == "__main__":

    # log BABAf from BABAb
    # for i in range(BABAb.last_all):
        # print((str(BABAb(i))+" = 1 << "+str(i))[6:])

    print()
    print("FIN")