# Напиши программу, которая будет открывать файл для чтения (перед этим создав его если он не существует),
# а затем построчно записывать в него текст, который запрашивается у пользователя через input


# Указываем имя файла
filename = 'data.txt'

# Открываем файл для записи
with open(filename, 'w') as file:
    print("Введите строки для записи в файл (введите пустую строку для завершения):")

    while True:
        # Запрашиваем ввод строки у пользователя
        user_input = input()

        # Проверяем, является ли введенная строка пустой
        if user_input == "":
            break  # Выходим из цикла, если строка пустая

        # Записываем введенную строку в файл с переводом строки
        file.write(user_input + '\n')

print(f"Данные успешно записаны в файл {filename}.")