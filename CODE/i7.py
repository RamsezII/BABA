import time

if __name__ == "__main__":
    t0 = time.time()
    i = 0
    for a in range(10):
        t02 = time.time()
        for b in range(1 << 28):
            pass
        t12 = time.time()
        print("a: ", a, "|", t12-t02)
    t1 = time.time()
    print(t1-t0)
    print("FIN")