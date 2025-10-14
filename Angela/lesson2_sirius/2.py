M = int(input())
N = int(input())
x = int(input())
y = int(input())

# определим короткий бортик:
short = min(M, N)

# определим минимальное расстояние до края бассейна
min_dist = min(x, y, abs(x - M), abs(y - N))
print(min_dist)