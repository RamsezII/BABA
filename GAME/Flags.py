from enum import Flag, IntEnum, auto


class Objs(IntEnum):
    empty = 0   # 00
    baba_obj = auto()   # 01
    wall_obj = auto()   # 02
    rock_obj = auto()   # 03
    flag_obj = auto()   # 04
    lava_obj = auto()   # 05
    water_obj = auto()   # 06
    baba_word = auto()   # 07
    wall_word = auto()   # 08
    rock_word = auto()   # 09
    flag_word = auto()   # 10
    lava_word = auto()   # 11
    water_word = auto()   # 12
    is_word = auto()   # 13
    you_word = auto()   # 14
    sink_word = auto()   # 15
    defeat_word = auto()   # 16


class Flags(Flag):
    empty = 0   # 0b0
    baba_obj = auto()   # 0b1
    wall_obj = auto()   # 0b10
    rock_obj = auto()   # 0b100
    flag_obj = auto()   # 0b1000
    lava_obj = auto()   # 0b10000
    water_obj = auto()   # 0b100000
    baba_word = auto()   # 0b1000000
    wall_word = auto()   # 0b10000000
    rock_word = auto()   # 0b100000000
    flag_word = auto()   # 0b1000000000
    lava_word = auto()   # 0b10000000000
    water_word = auto()   # 0b100000000000
    is_word = auto()   # 0b1000000000000
    you_word = auto()   # 0b10000000000000
    sink_word = auto()   # 0b100000000000000
    defeat_word = auto()   # 0b1000000000000000

    def hasflags_OR(self, flag): # OR
        return self & flag

    def hasflags_AND(self, flags): # AND
        return self & flags == flags


if __name__ == "__main__":
    print()
    txt = "{name} = auto()   # {value:02d}"
    for x in Objs:
        print(txt.format(name=x.name,value=x.value))
    print()
    for x in Objs:
        print(x.name + " = 1 << Objs." + x.name + "   # " + bin(1 << x.value))
    print()
    for x in Flags:
        print(x.name + " = auto()   # " + bin(x.value))