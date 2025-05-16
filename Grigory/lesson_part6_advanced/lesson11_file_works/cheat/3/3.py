# 1. Модифицируйте программу так, чтобы она подсчитывала количество строк в файле
# и выводила это количество на экран. Файл создайте вручную и вставьте в него несколько строк текста
# на своё усмотрение
# 2. Также выведите все уникальные слова (строки) из файла.

unique_words = set()
line_count = 0


with open('data.txt', 'r', encoding='UTF-8') as file:
    for line in file:
        line_count += 1
        unique_words.add(line.strip())

print(f'Количество строк: {line_count}')
print('Уникальные слова:', unique_words)