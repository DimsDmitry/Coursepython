"""напишите программу, которая будет запрашивать количество секунд и засекать обратный отсчёт, с интервалом 1 сек
Пример:

Введите количество секунд:>? 5
5
4
3
2
1
"""

from time import sleep


max_count = int(input('Введите количество секунд:'))
counter = max_count
while counter > 0:
    print(counter)
    counter -= 1
    sleep(1)