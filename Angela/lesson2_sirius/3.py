A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

area_hole = D * E

# площади сторон кирпича
area1 = A * B
area2 = B * C
area3 = C * D

if area1 <= area_hole or area2 <= area_hole or area3 <= area_hole:
    print('YES')
else:
    print('NO')