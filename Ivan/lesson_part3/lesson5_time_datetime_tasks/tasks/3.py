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


seconds = int(input('Введите количество секунд:'))
for i in range(seconds, -1, -1):
    print(i)
    sleep(1)
