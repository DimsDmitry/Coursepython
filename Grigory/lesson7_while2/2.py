# Напишите программу, которая будет запрашивать числа, пока не введено 0, и считать количество ТОЛЬКО НЕчётных чисел
count = 0
num = int(input("Введите число: "))
while num != 0:
    if num % 2 != 0:
        count += 1
    num = int(input("Введите число: "))
print("Количество нечётных чисел:", count)
