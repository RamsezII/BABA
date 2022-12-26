import os

def rootpath():
    path = os.path.abspath(__file__)
    path = os.path.dirname(path)
    path = os.path.dirname(path)
    path = os.path.dirname(path)
    return path


def getlines(filepath):
    file = open(filepath, 'r')
    lines = file.readlines()
    file.close()
    return lines