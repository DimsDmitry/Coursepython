list2 = ['text', 'hello', 4, 2, 10, 15]
print(list2[0])  # первый элемент
print(list2[:3])  # от 0 до 3
print(list2[3:])  # от 3 до конца
print(list2[1:5:2])  # от 1 до 5 с шагом 2

# вложенные индексы:
list1 = ['text', 4, 2, 10, [1, 2, 3]]
print(list1[4][0])

