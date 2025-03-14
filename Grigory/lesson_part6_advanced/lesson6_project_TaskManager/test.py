tasks = [('купить билеты', 'отпуск'), ('провести урок', 'Григорий'), ('ремонт', 'икеа')]

delete = input('Какую задачу удалить?').lower()
for t in tasks:
    if delete in t:
        tasks.remove(t)
        print(tasks)