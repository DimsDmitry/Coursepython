# Напишите программу, которая должна считать текст  строки, затем вывести полученный текст по одному символу на каждой
# строке.Пример работы программы:
#
# Введите текст бегущей строки:>? Привет!
# П
# р
# и
# в
# е
# т
# !

# Подсказка - вспомните функцию len(), а также срезы строки
text = input('Введите текст бегущей строки:')
while len(text) > 0:
    print(text[0])
    text = text[1:]


