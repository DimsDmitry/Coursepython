test_list = []
test_list = list()

test_list = [5, 3, 2, 4, 2, 5]
print(len(test_list))  # длина списка
test_list.append(10)  # добавить элемент в список
test_list.sort()
test_list.insert(2, 9)
while 5 in test_list:
    test_list.remove(5)
    # удаление всех значений 5
list2 = ['text', 'hello', 4, 2, 10, 15]
print(list2[:3])  # от 0 до 3
print(list2[3:])  # от 3 до конца
print(list2[1:5:2])  # от 1 до 5 с шагом 2
print(list2[2])

for elem in list2:
    print(elem)