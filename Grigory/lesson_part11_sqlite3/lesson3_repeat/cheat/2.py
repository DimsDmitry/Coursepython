# Задание - система учёта студентов
# Создать класс Student со свойствами - имя, возраст, факультет, группа
# Список оценок (пуст по умолчанию) и средний балл - два встроенных свойства
# Функция say_hello здоровается и выводит краткую сводку о студенте
# Функция average_marks проверяет есть ли у ученика оценки. Если нет - запрашивает их
# и считает средний балл


class Student:
    """класс описывающий студента"""
    def __init__(self, name, age, faculty, group):
        """метод присваивает экземпляру класса указанные свойства"""
        # присвоим переданные свойства ПРЯМО в экземпляр класса
        self.name = name
        self.age = age
        self.faculty = faculty
        self.group = group
        self.marks = []  # список оценок хранится внутри класса по умолчанию
        self.average_mark = 0

    def say_hello(self):
        """функция позволяет студенту поздороваться и рассказать о себе"""
        print(f'\nПривет! Меня зовут {self.name}, мне {self.age} лет.')
        print(f'Номер группы: {self.group}, факультет: {self.faculty}\n')

    def average_marks(self):
        """функция проверяет наличие оценок, считает средний балл"""
        if len(self.marks) == 0:
            print(f'У студента {self.name} нет оценок! Введите их через пробел:')
            marks_list = input('Введите оценки через пробел:').split()
            self.marks = list(map(int, marks_list))
            print(f'Оценки ученика {self.name}: {self.marks}')
        summ = 0
        for mark in self.marks:
            summ += mark
        self.average_mark = summ / len(self.marks)
        print(f'Студент {self.name} имеет средний балл: {self.average_mark}')


# создание объекта (экземпляра) класса
st1 = Student('Иван', 19, 'Информационные технологии', '2526')
st2 = Student('Марина', 20, 'Компьютерная безопасность', '1225')
print(st1.name)  # свойство объекта класса
st1.say_hello()  # метод объекта класса
st1.marks = [2, 3, 4, 5, 5]
st1.average_marks()