import os

def getpath(relativepath):
    path = os.path.abspath(__file__)
    path = os.path.dirname(path)
    path = os.path.dirname(path)
    path = os.path.dirname(path)
    return os.path.join(path, relativepath)


def getlines(filepath):
    file = open(getpath(filepath), 'r')
    lines = file.readlines()
    file.close()
    return lines