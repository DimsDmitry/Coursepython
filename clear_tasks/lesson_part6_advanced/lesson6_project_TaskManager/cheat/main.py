class TaskManager:
    def __init__(self):
        self.tasks = []  # Список задач
        self.tags = set()  # Множество меток
        self.history = []  # Список для хранения истории изменений

    def add_task(self, task, tag):
        self.tasks.append((task, tag))  # Добавление задачи с меткой
        self.tags.add(tag)  # Добавление метки в множество
        self.history.append(("add", task, tag))  # Запись в историю

    def remove_task(self, task):
        for t in self.tasks:
            if t[0] == task:
                self.tasks.remove(t)  # Удаление задачи
                self.history.append(("remove", task))  # Запись в историю
                break

    def view_tasks(self):
        print("Текущие задачи:")
        for task, tag in self.tasks:
            print(f"- {task} [Метка: {tag}]")

    def view_history(self):
        print("История изменений:")
        for record in self.history:
            if record[0] == "add":
                print(f"Добавлена задача: '{record[1]}' с меткой '{record[2]}'")
            elif record[0] == "remove":
                print(f"Удалена задача: '{record[1]}'")


def main():
    manager = TaskManager()
    while True:
        action = input("Выберите действие (add, remove, view, history, exit): ").strip().lower()
        if action == "add":
            task = input("Введите задачу: ")
            tag = input("Введите метку для задачи: ")
            manager.add_task(task, tag)
        elif action == "remove":
            task = input("Введите задачу для удаления: ")
            manager.remove_task(task)
        elif action == "view":
            manager.view_tasks()
        elif action == "history":
            manager.view_history()
        elif action == "exit":
            break
        else:
            print("Неверное действие. Попробуйте снова.")


if __name__ == "__main__":
    main()
