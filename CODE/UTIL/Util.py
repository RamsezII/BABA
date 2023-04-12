
MAX_INT = 1 << 32 - 1

def minIndex(values):
    m = values[0]
    x = 0
    for i in range(1, values):
        if values[i] < m:
            m = values[i]
            x = i
    return x,m
