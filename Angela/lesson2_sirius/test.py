x1 = int(input('X первой точки:'))
y1 = int(input('Y первой точки:'))

x2 = int(input('X второй точки:'))
y2 = int(input('Y второй точки:'))

change_dist = abs((x1 - x2) * (y1 - y2))

if change_dist == 2:
    print('YES')
else:
    print('NO')

