marks = '5 2 3 4 5'.split()
# Способ 1
marks = list(map(int, marks))
print(marks)
summ = 0
for m in marks:
    summ += m

# Способ 2
marks = '5 2 3 4 5'.split()
summ = 0
for m in marks:
    summ += int(m)