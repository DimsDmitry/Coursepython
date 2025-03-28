digit = int(input('Введите число (0 - остановить)'))
even = 0
while digit != 0:
    if digit % 2 == 0:
        print('Число чётное!')
        even += 1
        digit = int(input('Введите число (0 - остановить)'))
    else:
        print('Число нечётное!')
        digit = int(input('Введите число (0 - остановить)'))

print('Введено чётных чисел:', even)

