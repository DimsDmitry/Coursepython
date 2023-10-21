greeting = 'Добро пожаловать!'

symbol1 = greeting[8]  # один элемент
symbol2 = greeting[2:8]  # все элементы от 2 до 8, не включая 8
symbol3 = greeting[2:]  # все элементы от 2 и до конца
symbol4 = greeting[:8]  # все элементы от начала и до 8, не включая 8

print(symbol1)
print(symbol2)
print(symbol3)
print(symbol4)
print(100*'#')

symbol1 = greeting[-1]  # первый элемент с конца
symbol2 = greeting[-5:-2]  # все элементы от -5 до -2, не включая -2
symbol3 = greeting[-2:]  # все элементы от -2 и до конца
symbol4 = greeting[:-8]  # все элементы от начала и до -8, не включая -8
symbol5 = greeting[3:-8]  # все элементы от 3 и до -8, не включая -8

print(symbol1)
print(symbol2)
print(symbol3)
print(symbol4)
print(symbol5)




