import time


print("run...")
t0 = time.time()

for i in range(10000000):
    waw = 1

t1 = time.time()
print("time: " + str(t1-t0))