import sqlite3  # Импортируем встроенную библиотеку для работы с БД SQLite


# --- 1. НАСТРОЙКА БАЗЫ ДАННЫХ ---
def init_db():
    """Функция для создания 'скелета' нашей базы данных"""

    # Устанавливаем связь с файлом. Если его нет — он создастся автоматически.
    conn = sqlite3.connect('university_pro.db')

    # Создаем курсор — это наш 'исполнитель', который будет отправлять SQL-команды в файл.
    cursor = conn.cursor()

    # ВКЛЮЧАЕМ РЕЖИМ СВЯЗЕЙ. По умолчанию SQLite может игнорировать Foreign Keys.
    # Эта строчка гарантирует, что мы не сможем привязать студента к несуществующей группе.
    cursor.execute("PRAGMA foreign_keys = ON")

    # Создаем таблицу Факультетов.
    # id — уникальный номер, который база сама будет увеличивать (AUTOINCREMENT).
    # name — текст, который не может быть пустым (NOT NULL) и должен быть уникальным (UNIQUE).
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS faculties (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE
    )''')

    # Создаем таблицу Групп.
    # faculty_id — это 'внешний ключ' (Foreign Key), который связывает группу с факультетом.
    # ON DELETE CASCADE — если мы удалим факультет, то все его группы удалятся сами собой.
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS groups (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE,
        faculty_id INTEGER,
        FOREIGN KEY (faculty_id) REFERENCES faculties (id) ON DELETE CASCADE
    )''')

    # Создаем таблицу Студентов.
    # group_id INTEGER — здесь будет храниться число (ID группы из таблицы выше).
    # ON DELETE SET NULL — если группу удалят, студент останется в базе, но его группа станет 'пустой' (NULL).
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT NOT NULL,
        age INTEGER,
        group_id INTEGER,
        FOREIGN KEY (group_id) REFERENCES groups (id) ON DELETE SET NULL
    )''')

    # Создаем таблицу Студенческих билетов (Связь 1-к-1: 1 студент = 1 билет).
    # student_id INTEGER UNIQUE — слово UNIQUE гарантирует, что у студента не будет двух билетов.
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS student_cards (
        card_id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER UNIQUE,
        card_number TEXT UNIQUE,
        FOREIGN KEY (student_id) REFERENCES students (id) ON DELETE CASCADE
    )''')

    # Подтверждаем сохранение всех таблиц в файле.
    conn.commit()
    # Закрываем соединение, чтобы освободить файл для других программ.
    conn.close()


# --- 2. ЗАПОЛНЕНИЕ ДАННЫМИ ---
def fill_data():
    """Заполняем базу 'первыми жильцами'"""
    conn = sqlite3.connect('university_pro.db')
    cursor = conn.cursor()

    try:
        # INSERT OR IGNORE — команда 'Добавь, а если уже есть — пропусти'.
        # Это защищает код от ошибок при повторном запуске скрипта.
        cursor.execute("INSERT OR IGNORE INTO faculties (name) VALUES ('Программирование')")
        cursor.execute("INSERT OR IGNORE INTO faculties (name) VALUES ('Дизайн')")

        # Нам нужно узнать ID факультета 'Программирование', чтобы привязать к нему группу.
        cursor.execute("SELECT id FROM faculties WHERE name = 'Программирование'")
        # fetchone() достает одну найденную строку, [0] берет первое значение из неё (id).
        f_id = cursor.fetchone()[0]

        # Добавляем группу ПРОГ-101, указывая ID её факультета.
        cursor.execute("INSERT OR IGNORE INTO groups (name, faculty_id) VALUES (?, ?)", ('ПРОГ-101', f_id))

        # Получаем ID только что созданной группы.
        cursor.execute("SELECT id FROM groups WHERE name = 'ПРОГ-101'")
        g_id = cursor.fetchone()[0]

        # Создаем список кортежей со студентами для массового добавления.
        students = [
            ('Иван Иванов', 19, g_id),
            ('Мария Сидорова', 20, g_id)
        ]

        # executemany — быстрый способ добавить сразу много строк из списка.
        # Вопросики '?' — это защита (плейсхолдеры). Данные подставятся автоматически и безопасно.
        cursor.executemany("INSERT OR IGNORE INTO students (full_name, age, group_id) VALUES (?, ?, ?)", students)
        # INSERT OR IGNORE — команда в SQL, которая позволяет вставлять новые записи в базу данных,
        # игнорируя дубликаты уникальных значений.
        conn.commit()
    except Exception as e:
        print(f"Ой! Произошла ошибка: {e}")
    finally:
        conn.close()


# --- 3. ФУНКЦИИ-ОТЧЕТЫ ---

def show_all_students():
    """Собираем данные из трех таблиц в один красивый отчет"""
    conn = sqlite3.connect('university_pro.db')
    cursor = conn.cursor()

    # JOIN — это 'склеивание'.
    # Мы берем таблицу students (s), приклеиваем к ней groups (g), а затем faculties (f).
    # ON — условие склейки: ID в одной таблице должен совпадать с ID в другой.
    query = '''
    SELECT s.full_name, g.name, f.name
    FROM students s
    JOIN groups g ON s.group_id = g.id
    JOIN faculties f ON g.faculty_id = f.id
    '''

    cursor.execute(query)
    # fetchall() — забирает абсолютно все строки, которые нашел поиск.
    rows = cursor.fetchall()

    print("\n" + "=" * 60)
    # Форматированный вывод текста (:<20 значит выделить 20 символов под колонку).
    print(f"{'ФИО СТУДЕНТА':<20} | {'ГРУППА':<10} | {'ФАКУЛЬТЕТ'}")
    print("-" * 60)
    for row in rows:
        print(f"{row[0]:<20} | {row[1]:<10} | {row[2]}")
    print("=" * 60)

    conn.close()


# --- 4. ТОЧКА ВХОДА ---
if __name__ == "__main__":
    init_db()  # 1. Строим здание (таблицы)
    fill_data()  # 2. Заселяем жителей (данные)

    print("Система управления ВУЗом готова!")
    show_all_students()  # 3. Печатаем ведомость