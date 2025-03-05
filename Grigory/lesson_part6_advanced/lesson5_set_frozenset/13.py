# Сравнение frozenset: Создайте два frozenset, содержащих одни и те же элементы, но в разном порядке.
# Проверьте, равны ли они.

set1 = frozenset([1, 2, 3])
set2 = frozenset([3, 2, 1])

print(set1 == set2)
