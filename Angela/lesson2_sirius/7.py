a = int(input())
b = int(input())

if a == 0:
    if b == 0:
        print('INF')  # бесконечно много решений
    else:
        print('NO')  # решений нет
elif b % a == 0:
    print(-b//a)  # целочисленное решение
else:
    print('NO')  # целочисленных решений нет