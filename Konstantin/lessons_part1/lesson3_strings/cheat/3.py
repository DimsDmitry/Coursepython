# Хозяина ресторана интересует, понравились ли клиенту фирменные блюда: фондю и жульен.
#
# Напиши программу, которая запрашивает у пользователя понравившиеся блюда
# и печатает результат как в примере:

# Введите любимые блюда ресторана "Алевтина":>? фондю, берёзовый сок, салат
# фондю 0
# жульен -1

dishes = input('Введите любимые блюда ресторана "Алевтина":')
searching1 = 'фондю'
searching2 = 'жульен'

result1 = dishes.find(searching1)
result2 = dishes.find(searching2)
print(searching1, result1)
print(searching2, result2)