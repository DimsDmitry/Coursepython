def sum_multiply(a, b):
    return a + b, a * b


result = sum_multiply(5, 10)
print(result)

# переменная result будет КОРТЕЖЕМ (кортеж - неизменяемые список)
# если функция возвращает 2 и более значений, можно их поместить
# в разные переменные - это называется распаковкой кортежа
num1, num2 = sum_multiply(4, 10)
print(num1)
print(num2)