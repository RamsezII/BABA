

from enum import IntFlag


class Flags(IntFlag):
    A = 1 << 0
    B = 1 << 1
    C = 1 << 2

f = Flags.B | Flags.C

for x in f:
    print(x.name)