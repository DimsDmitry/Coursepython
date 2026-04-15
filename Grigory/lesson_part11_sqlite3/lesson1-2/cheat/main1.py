import sqlite3

# 1. Создаем файл базы и подключаемся к нему
conn = sqlite3.connect('my_quiz.db')
# 2. Создаем "курсор" — наш инструмент для выполнения команд
cursor = conn.cursor()

# 3. Пишем команду на языке SQL для создания таблицы
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    score INTEGER
)
''')

# 4. Сохраняем изменения и закрываем
conn.commit()
conn.close()