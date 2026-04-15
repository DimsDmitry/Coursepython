import sqlite3


# стандартный модуль для работы с БД

def run_university_db():
    """создаёт базу данных для университета"""
    # 1) Установка связи - пытаемся открыть файл university_pro.db
    # Если его нет - создаём с нуля
    conn = sqlite3.connect('university_pro.db')
    # Создаём объект "курсор" - это инструмент который позволит нам отправлять
    # SQL-запросы в саму базу данных. Без него запросы не будут восприниматься
    cursor = conn.cursor()

    # 2) Настройка поведения базы
    # По умолчанию СУБД sqlite позволяет нарушать связи между объектами,
    # например привязать студента к номеру группы которого не существует
    # Команда PRAGMA заставляет базу строго проверять внешние ключи foreign_keys
    cursor.execute('PRAGMA foreign_keys=ON')

    # 3) Создание таблиц
    # 1. Таблица факультетов.
    # CREATE TABLE IF NOT EXISTS - создать таблицу, если её не существует,
    # id INTEGER PRIMARY KEY AUTOINCREMENT - айди будет числовым типом данных,
    # PRIMARY KEY AUTOINCREMENT - выдавать первичный ключ (уникальный номер)
    # автоматически каждой строке (1, 2, 3)
    # name TEXT NOT NULL UNIQUE - названия факультетов будут иметь текстовый формат,
    # и не должны повторяться (уникальные)

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS faculties(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE
    )''')

    # 2. Таблица Групп
    # faculty_id INTEGER - колонка-ссылка, в которой будет лежать число (ID факультета)
    # FOREIGN KEY ... REFERENCES - это нить, связывающая группу с факультетом
    # ON UPDATE CASCADE ON DELETE CASCADE - если мы обновим факультет, в его группах айди факультета
    # тоже обновится; если мы УДАЛИМ факультет, база САМА удалит все его группы

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS groups(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            faculty_id INTEGER,
            FOREIGN KEY (faculty_id) REFERENCES faculties(id) ON UPDATE CASCADE ON DELETE CASCADE
        )''')

    # 3. Таблица Студентов.
    # age - возраст, численный тип данных; ON DELETE SET NULL - если группу удалят, то сам студент НЕ УДАЛИТСЯ,
    # но его поле group_id станет пустым (NULL)

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS students(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                full_name TEXT NOT NULL,
                age INTEGER NOT NULL,
                group_id INTEGER,
                FOREIGN KEY (group_id) REFERENCES groups (id) ON UPDATE CASCADE ON DELETE SET NULL
            )''')

    # 4) Создание VIEW - виртуального окна, содержимое которое мы определим запросом
    cursor.execute('DROP VIEW IF EXISTS faculty_stats')
    # каждый раз при открытии окна база будет пересчитывать студентов

    # SELECT ... COUNT(s.id) - выбрать имя факультета и посчитать  кол-во студентов
    cursor.execute("""
    CREATE VIEW faculty_stats AS
        SELECT 
            f.id AS faculty_id,
            f.name AS faculty_name,
            COUNT(s.id) AS student_count,
            AVG(s.age) AS average_age  -- Средний возраст студента по факультету
        FROM faculties f
        LEFT JOIN groups g ON f.id = g.faculty_id
        LEFT JOIN students s ON g.id = s.group_id
        GROUP BY f.id
        """)

    # GROUP BY - сгруппировать по - взять все данные так чтобы расчёт шёл
    # для каждого факультета отдельно - GROUP BY f.id
    # 5) Заполняем данными таблицы (INSERT)
    # 5.1) INSERT OR IGNORE - добавь значение, но если оно уже есть, не добавляй (чтобы не плодить дубликаты)
    cursor.execute("INSERT OR IGNORE INTO faculties(id, name) VALUES (1, 'Программирование'), (2, 'Дизайн')")
    # 5.2) добавили факультеты и их номера, теперь добавим связи
    cursor.execute("INSERT OR IGNORE INTO groups(id, name, faculty_id) VALUES (1, 'ПРОГ-101', 1), (2, 'АРТ-202', 2)")

    # 5.3) Добавляем студентов, будем хранить их как список кортежей
    students_list = [
        ('Иван Иванов', 19, 1),
        ('Мария Сидорова', 21, 1),
        ('Анна Сергеева', 20, 2),
        ('Пётр Волков', 22, 2)
    ]
    # executemany - подставляет сразу много данных из списка в шаблоны с вопросиками (?)
    # эти вопросики называются - ПЛЕЙСХОЛДЕРЫ (place holder - держатель места)
    # это поможет подставить сразу много данных и защищает нас от поломки таблицы в случае опечатки
    cursor.executemany('''
        INSERT OR IGNORE INTO students (full_name, age, group_id)
        VALUES (?, ?, ?)
        ''', students_list)
    # пока мы не сохранили изменения, они все находятся в подвешенном состоянии
    # commit() записывает все изменения на файл .db навсегда
    conn.commit()

    # 6) Проверка данных и их вывод
    print('\n  ОТЧЁТ ИЗ БАЗЫ ДАННЫХ  \n')
    # запросим ВСЕ (*) данные из нашего виртуального отчёта - view - faculty_stats
    cursor.execute('SELECT * FROM faculty_stats')
    for row in cursor.fetchall():
        # циклом for проходимся по каждой строке таблицы
        print(f'Факультет: {row[1]}\nСтудентов: {row[2]}\nСредний возраст: {row[3]}\n')

    conn.close() # закрываем соединение

# Точка входа. Сработает только если открыть файл напрямую
if __name__ == '__main__':
    run_university_db()