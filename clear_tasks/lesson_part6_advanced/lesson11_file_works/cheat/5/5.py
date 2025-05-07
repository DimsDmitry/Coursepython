# Напишите программу, которая проанализирует стихотворение Лермонтова "Приходит осень, золотит…",
# выведет количество гласных букв в нём и согласных, а также отдельно количество букв "о".
# Первая строка (заголовок) не учитывается!!
# Не забудьте обработать исключение FileNotFoundError

def count_letters(filename):
    vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"  # Гласные буквы (русские)
    consonants = "бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ"  # Согласные буквы (русские)
    count_vowels = 0
    count_consonants = 0
    count_o = 0

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            # Пропускаем первую строку (заголовок)
            next(file)

            for line in file:
                for char in line:
                    if char in vowels:
                        count_vowels += 1
                    elif char in consonants:
                        count_consonants += 1
                    if char.lower() == 'о':
                        count_o += 1

        print(f"Количество гласных букв: {count_vowels}")
        print(f"Количество согласных букв: {count_consonants}")
        print(f"Количество букв 'о': {count_o}")

    except FileNotFoundError:
        print("Файл не найден. Пожалуйста, проверьте имя файла.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


# Укажите имя файла, который нужно обработать
filename = 'text.txt'
count_letters(filename)