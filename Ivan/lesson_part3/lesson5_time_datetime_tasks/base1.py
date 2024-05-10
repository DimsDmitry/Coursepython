from time import *

start = time()
for i in range(15):
    print(i)
    sleep(2)

stop = time()
print('Программа работала, сек:', stop-start)