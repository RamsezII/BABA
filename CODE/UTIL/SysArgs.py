import sys


def sysArgs(*keys):
    argv = sys.argv
    args = {}
    argi = 0
    while argi < len(argv):
        arg = argv[argi]
        argi += 1
        for key in keys:
            if arg == key:
                args[key] = argv[argi]
                argi += 1
    return args