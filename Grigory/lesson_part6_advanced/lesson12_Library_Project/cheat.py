class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year})\n"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        if not self.books:
            print("Библиотека пуста.\n")
        else:
            for book in self.books:
                print(book)

    def save_to_file(self, filename):
        with open(filename, 'w', encoding='UTF-8') as file:  # Открываем файл для записи
            for book in self.books:
                file.write(f"{book.title},{book.author},{book.year}\n")  # Записываем каждую книгу

    def load_from_file(self, filename):
        try:
            with open(filename, 'r', encoding='UTF-8') as file:  # Открываем файл для чтения
                for line in file:
                    title, author, year = line.strip().split(',')  # Читаем и разбиваем строки
                    self.add_book(Book(title, author, int(year)))  # Добавляем книгу в библиотеку
        except FileNotFoundError:
            print("Файл не найден.\n")


def main():
    library = Library()
    library.load_from_file('library.txt')  # Загружаем книги из файла

    while True:
        print("1. Добавить книгу")
        print("2. Показать все книги")
        print("3. Сохранить книги в файл")
        print("4. Выход\n")
        choice = input("Выберите действие:\n")

        if choice == '1':
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = input("Введите год издания: ")
            library.add_book(Book(title, author, year))
        elif choice == '2':
            library.display_books()
        elif choice == '3':
            library.save_to_file('library.txt')  # Сохраняем книги в файл
            print("Книги сохранены в файл.\n")
        elif choice == '4':
            print('\nРабота завершена.')
            break
        else:
            print("Неверный выбор. Попробуйте снова.\n")


if __name__ == "__main__":
    a = Book('title', 'author', 'year')