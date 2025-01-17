marks = '5 3 4 2 1 4 5'.split()
summ = 0
print(marks)
for m in marks:
    summ += int(m)

average = round(summ/len(marks), 2)
print(average)
