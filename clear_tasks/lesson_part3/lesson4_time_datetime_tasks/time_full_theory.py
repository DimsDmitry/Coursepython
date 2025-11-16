from time import *


# time - возвращает кол-во секунд с начала эпохи (01.01.1970)
seconds = time()
print(seconds)

# ctime - принимает кол-во секунд с начала эпохи и возвращает текущие дату и время
local_time = ctime(1239180090)
print(local_time)

# sleep(n) - останавливает работу программы на n секунд

# print('Hello!')
# sleep(3)
# print('Hello!')
# for i in range(5):
#     print(i)
#     sleep(1)


# localtime

result = localtime(1000)
print(result)

# asctime - принимает кортеж, содержащий 9 значений struct_time и возвращает строку даты
result = asctime((2020, 11, 15, 13, 35, 55, 0, 364, 0))
print(result)