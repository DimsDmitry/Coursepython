N = int(input())
M = int(input())
x = int(input())
y = int(input())

# определим расстояния до бортика
n = N - x
m = M - y

# определим минимальное расстояние до края бассейна
if n <= x and n <= y and n <= m:
    print(n)

if x <= n and x <= y and x <= m:
    print(x)

if m <= n and m <= y and m <= x:
    print(m)

if y <= n and y <= m and y <= x:
    print(y)