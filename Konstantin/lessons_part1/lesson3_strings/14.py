# Получение первых n символов:
# Напишите программу, которая принимает строку и число n, а затем возвращает первые n символов строки.

text = input('Введите текст:')
n = int(input('Сколько первых символов показать?'))

print(text[:n])