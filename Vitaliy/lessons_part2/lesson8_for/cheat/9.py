# Факториалы: Напишите программу, которая использует цикл for
# для вычисления факториалов чисел от 1 до 10 и выводит результаты.
# Пример:
#
# Число: >? 5
# 120

n = int(input('Число: '))

factorial = 1

for i in range(2, n+1):
    factorial *= i

print(factorial)