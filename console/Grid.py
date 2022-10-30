from enum import Flag, auto

class Flags(Flag):
    empty = 0
    baba = auto()
    wall = auto()
    rock = auto()
    flag = auto()
    lava = auto()
    water = auto()

    def hasflag(self, flag): # OR
        return self & flag

    def hasflags(self, flags): # AND
        return self & flags == flags

code2flag = {
    '.': Flags.empty,
    'b': Flags.baba,
    'w': Flags.wall,
    'r': Flags.rock,
    'f': Flags.flag,
    'l': Flags.lava,
    'a': Flags.water,
}

flag2code = {
    Flags.empty: '.',
    Flags.baba: 'b', 
    Flags.wall: 'w', 
    Flags.rock: 'r', 
    Flags.flag: 'f', 
    Flags.lava: 'l', 
    Flags.water: 'a',
}

if __name__ == "__main__":
    for x in code2flag:
        print(str(code2flag[x]) + ": \'" + x + "\',")