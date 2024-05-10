from random import *

list1 = ['Иванов', 'Петров', 'Сидоров', 'Пупкина', 'Губкина', 'Олегова']
# shuffle(list1)
# print(list1[0])

rand_ind = randint(0, len(list1)-1)
print(list1[rand_ind])