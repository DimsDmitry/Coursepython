from time import *


test1 = time()

for i in range(3000):
    print(i)

test2 = time()
print('Время работы программы, сек: ', test2-test1)