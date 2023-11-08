num1 = input('Введите 1-е число')
num1 = int(num1)
num2 = input('Введите 2-е число')
num2 = int(num2)
result = max(num1, num2)
print('Наибольшее число:', result)

num1 = int(input('Введите 1-е число'))
num2 = int(input('Введите 2-е число'))
result = max(num1, num2)
print('Наибольшее число:', result)

good = input('Что вам понравилось в отеле?')
bad = input('Что вам НЕ понравилось в отеле?')
l1 = len(good)
l2 = len(bad)
length = l1 + l2
print('Всего символов:', length)

good = len(input('Что вам понравилось в отеле?'))
bad = len(input('Что вам НЕ понравилось в отеле?'))
length = good + bad
print('Всего символов:', length)

print('Всего символов:', len(input('Что вам понравилось в отеле?')) + len(input('Что вам НЕ понравилось в отеле?')))

