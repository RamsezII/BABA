from enum import Flag, IntEnum, auto


class Objs(IntEnum):
    empty = -1
    baba_obj = auto()   # 0
    wall_obj = auto()   # 1
    rock_obj = auto()   # 2
    flag_obj = auto()   # 3
    lava_obj = auto()   # 4
    water_obj = auto()   # 5
    baba_word = auto()   # 6
    wall_word = auto()   # 7
    rock_word = auto()   # 8
    flag_word = auto()   # 9
    lava_word = auto()   # 10
    water_word = auto()   # 11
    is_word = auto()   # 12
    you_word = auto()   # 13
    sink_word = auto()   # 14
    defeat_word = auto()   # 15


class Flags(Flag):
    empty = 0   # .. | 0 | 0b0
    baba_obj = auto()   # 00 | 1 | 0b1
    wall_obj = auto()   # 01 | 2 | 0b10
    rock_obj = auto()   # 02 | 4 | 0b100
    flag_obj = auto()   # 03 | 8 | 0b1000
    lava_obj = auto()   # 04 | 16 | 0b10000
    water_obj = auto()   # 05 | 32 | 0b100000
    baba_word = auto()   # 06 | 64 | 0b1000000
    wall_word = auto()   # 07 | 128 | 0b10000000
    rock_word = auto()   # 08 | 256 | 0b100000000
    flag_word = auto()   # 09 | 512 | 0b1000000000
    lava_word = auto()   # 10 | 1024 | 0b10000000000
    water_word = auto()   # 11 | 2048 | 0b100000000000
    is_word = auto()   # 12 | 4096 | 0b1000000000000
    you_word = auto()   # 13 | 8192 | 0b10000000000000
    sink_word = auto()   # 14 | 16384 | 0b100000000000000
    defeat_word = auto()   # 15 | 32768 | 0b1000000000000000

    def hasflags_OR(self, flag): # OR
        return self & flag

    def hasflags_AND(self, flags): # AND
        return self & flags == flags
    
    def toIndex(self):
        for i in range(16):
            if self.hasflags_AND(Flags(1 << i)):
                return f"{i:02d}"


if __name__ == "__main__":
    print()
    for x in Objs:
        print(x.name + " = auto()   #", x.value)
    print()
    for x in Flags:
        print(x.name + " = auto()   #", x.toIndex(), "|", x.value, "| " + bin(x.value))