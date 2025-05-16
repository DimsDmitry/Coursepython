# Напишите программу, которая открывает файл tasks.txt и выводит все задачи на экран.
# Если задач нету, выводится сообщение "список задач пуст"
# Обработайте исключение FileNotFoundError
# Файл tasks.txt создайте и заполните вручную


def view_tasks():
    try:
        with open('tasks.txt', 'r') as file:
            tasks = file.readlines()
            if not tasks:
                print("Список задач пуст.")
            else:
                print("Список задач:")
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task.strip()}")
    except FileNotFoundError:
        print("Файл tasks.txt не найден.")

view_tasks()