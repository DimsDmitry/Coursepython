list_marks = [2, 5, 3, 5, 4, 2, 3, 2, 5]

for m in list_marks:
    if m == 2:
        list_marks.remove(m)

print(list_marks)

list_marks = [2, 5, 3, 5, 4, 2, 3, 2, 5]

while 2 in list_marks:
    list_marks.remove(2)

print(list_marks)