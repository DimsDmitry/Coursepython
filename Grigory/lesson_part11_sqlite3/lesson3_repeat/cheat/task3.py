class Book:
    """Класс, описывающий книгу в библиотеке"""

    def __init__(self, title, author, year, genre):
        """Метод инициализации: присваивает экземпляру класса указанные свойства"""
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.ratings = []
        self.average_rating = 0.0

    def book_info(self):
        """Метод выводит краткую информацию о книге"""
        print(f"\nПривет, я книга! Меня зовут {self.title}. "
              f"Мой автор — {self.author}, {self.year} год. "
              f"Жанр: {self.genre}.")

    def calculate_average_rating(self):
        """Метод проверяет наличие оценок, при необходимости запрашивает их,
        и вычисляет средний рейтинг книги"""

        # Проверяем, есть ли оценки
        if not self.ratings:  # более питоновский способ проверки пустого списка
            print(f"\nУ книги '{self.title}' пока нет оценок. "
                  f"Введите оценки читателей через пробел:")
            ratings_input = input("> ").split()
            self.ratings = [int(r) for r in ratings_input]  # list comprehension
            print(f"Оценки книги '{self.title}': {self.ratings}")

        # Вычисляем среднее с помощью встроенных функций
        self.average_rating = sum(self.ratings) / len(self.ratings)

        # Выводим результат (округляем до 2 знаков)
        print(f"Средний рейтинг книги '{self.title}': "
              f"{self.average_rating:.2f}")


# Создаем объекты
book1 = Book("Мастер и Маргарита", "Михаил Булгаков", 1967, "Роман")
book2 = Book("1984", "Джордж Оруэлл", 1949, "Антиутопия")

# Проверяем работу
print(book2.title)
book1.book_info()
book1.ratings = [5, 4, 5, 5, 4]
book1.calculate_average_rating()
book2.calculate_average_rating()