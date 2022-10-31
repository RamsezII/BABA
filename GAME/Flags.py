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
    empty = 1 << Objs.empty   # 0b1
    baba_obj = 1 << Objs.baba_obj   # 0b10
    wall_obj = 1 << Objs.wall_obj   # 0b100
    rock_obj = 1 << Objs.rock_obj   # 0b1000
    flag_obj = 1 << Objs.flag_obj   # 0b10000
    lava_obj = 1 << Objs.lava_obj   # 0b100000
    water_obj = 1 << Objs.water_obj   # 0b1000000
    baba_word = 1 << Objs.baba_word   # 0b10000000
    wall_word = 1 << Objs.wall_word   # 0b100000000
    rock_word = 1 << Objs.rock_word   # 0b1000000000
    flag_word = 1 << Objs.flag_word   # 0b10000000000
    lava_word = 1 << Objs.lava_word   # 0b100000000000
    water_word = 1 << Objs.water_word   # 0b1000000000000       
    is_word = 1 << Objs.is_word   # 0b10000000000000
    you_word = 1 << Objs.you_word   # 0b100000000000000
    sink_word = 1 << Objs.sink_word   # 0b1000000000000000      
    defeat_word = 1 << Objs.defeat_word   # 0b10000000000000000 

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