import sqlite3  # Подключаем стандартный модуль Python для работы с базами данных SQLite.


def run_university_db():
    # --- 1. УСТАНОВКА СВЯЗИ ---
    # Пытаемся открыть файл 'university_pro.db'.
    # Если файла нет в папке с проектом, Python создаст его "с нуля".
    conn = sqlite3.connect('university_pro.db')

    # Создаем объект "курсор" (cursor). Это инструмент, через который мы отправляем
    # текстовые SQL-запросы в саму базу данных. Без него мы не сможем ничего записать.
    cursor = conn.cursor()

    # --- 2. НАСТРОЙКА ПОВЕДЕНИЯ БАЗЫ ---
    # По умолчанию SQLite позволяет нарушать связи (например, привязать студента к группе №999, которой нет).
    # Эта команда (PRAGMA) заставляет базу СТРОГО проверять Foreign Keys (внешние ключи).
    cursor.execute("PRAGMA foreign_keys = ON")

    # --- 3. СОЗДАНИЕ ТАБЛИЦ (АРХИТЕКТУРА) ---

    # Строим таблицу Факультетов.
    # PRIMARY KEY AUTOINCREMENT — говорит базе: "Сама выдавай уникальный номер (1, 2, 3...) каждой строке".
    # UNIQUE — запрещает создавать два факультета с одинаковым названием.
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS faculties (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE
    )''')

    # Строим таблицу Групп.
    # faculty_id INTEGER — это колонка-ссылка. В ней будет лежать число (ID факультета).
    # FOREIGN KEY ... REFERENCES — это "железная нить", связывающая группу с факультетом.
    # ON DELETE CASCADE — если мы удалим факультет, база САМА удалит все его группы. Это удобно.
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS groups (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE,
        faculty_id INTEGER,
        FOREIGN KEY (faculty_id) REFERENCES faculties (id) ON DELETE CASCADE
    )''')

    # Строим таблицу Студентов.
    # age INTEGER — новая колонка для хранения возраста (целое число).
    # ON DELETE SET NULL — если группу удалят, студент НЕ удалится, но его поле group_id станет пустым (NULL).
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT NOT NULL,
        age INTEGER,
        group_id INTEGER,
        FOREIGN KEY (group_id) REFERENCES groups (id) ON DELETE SET NULL
    )''')

    # ВАЖНО: Если ты запускал старый код, в файле базы нет колонки 'age'.
    # Этот блок "допиливает" таблицу, если колонка отсутствует, чтобы не было ошибок SQLITE_ERROR.
    try:
        cursor.execute("ALTER TABLE students ADD COLUMN age INTEGER")
    except sqlite3.OperationalError:
        # Если колонка уже есть (второй запуск программы), мы просто игнорируем ошибку.
        pass

    # --- 4. СОЗДАНИЕ ВИРТУАЛЬНОГО ОКНА (VIEW) ---
    # VIEW — это "живой отчет". Мы не записываем туда данные, мы записываем ТУДА ПРАВИЛО расчета.
    # Каждый раз, когда мы открываем это окно, база мгновенно пересчитывает студентов.
    cursor.execute("DROP VIEW IF EXISTS faculty_stats")

    # SELECT ... COUNT(s.id) — "Выбери имя факультета и посчитай количество ID студентов".
    # LEFT JOIN — "Возьми ВСЕ факультеты, даже если в них ПОКА НЕТ ни одного студента".
    # GROUP BY f.id — "Схлопни данные так, чтобы расчет шел отдельно для каждого факультета".
    cursor.execute('''
    CREATE VIEW faculty_stats AS
    SELECT 
        f.id AS faculty_id,
        f.name AS faculty_name,
        COUNT(s.id) AS student_count,
        AVG(s.age) AS average_age  -- ДОБАВЛЕНО: Считаем еще и средний возраст по факультету!
    FROM faculties f
    LEFT JOIN groups g ON f.id = g.faculty_id
    LEFT JOIN students s ON g.id = s.group_id
    GROUP BY f.id
    ''')

    # --- 5. ЗАПОЛНЕНИЕ ДАННЫМИ (INSERT) ---
    # Используем INSERT OR IGNORE, чтобы при повторном запуске скрипта данные не двоились.

    # 5.1. Добавляем "Верхушку" (Факультеты)
    cursor.execute("INSERT OR IGNORE INTO faculties (id, name) VALUES (1, 'Программирование'), (2, 'Дизайн')")

    # 5.2. Добавляем "Связи" (Группы), указывая ID их факультетов
    cursor.execute("INSERT OR IGNORE INTO groups (id, name, faculty_id) VALUES (1, 'ПРОГ-101', 1), (2, 'АРТ-202', 2)")

    # 5.3. Добавляем "Листья" (Студентов)
    # Используем список кортежей — это самый профессиональный способ массовой вставки данных.
    students_to_add = [
        ('Иван Иванов', 19, 1),
        ('Мария Сидорова', 21, 1),
        ('Анна Сергеева', 20, 2),
        ('Петр Волков', 22, 2)
    ]

    # executemany подставляет данные из списка в шаблон с вопросиками (?).
    # Это защищает нас от ошибок форматирования и взломов.
    cursor.executemany('''
        INSERT OR IGNORE INTO students (full_name, age, group_id) 
        VALUES (?, ?, ?)
    ''', students_to_add)

    # ПОДТВЕРЖДЕНИЕ: Пока мы не вызвали commit(), все изменения висят "в воздухе".
    # Эта команда записывает всё на диск в файл .db навсегда.
    conn.commit()

    # --- 6. ПРОВЕРКА И ВЫВОД ---
    print("=== ОТЧЕТ ИЗ БАЗЫ ДАННЫХ (VIEW) ===")

    # Запрашиваем данные из нашего виртуального отчета faculty_stats.
    cursor.execute("SELECT * FROM faculty_stats")
    for row in cursor.fetchall():
        # row[1] — Название, row[2] — Кол-во студентов, row[3] — Средний возраст.
        # :<18 — это форматирование (выровнять текст по левому краю, выделив 18 символов).
        print(f"🏛 Факультет: {row[1]:<18} | 👥 Студентов: {row[2]} | 🎂 Ср. возраст: {row[3]:.1f}")

    # Закрываем соединение. Это как положить трубку телефона после разговора.
    conn.close()


# ТОЧКА ВХОДА: Этот блок сработает только если мы запустим этот файл напрямую.
if __name__ == "__main__":
    run_university_db()