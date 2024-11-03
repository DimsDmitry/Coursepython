"""Запрограммируй класс Student:
1) Создай конструктор класса. Он должен создавать студента со свойствами: фамилия, средний балл (по умолчанию равен 0)
 и изучаемое направление (передаются в конструктор. Курс по умолчанию «-»).

2) Создай метод, печатающий информацию о студенте. Он должен выводить данные как в примере.

3) Создай метод, устанавливающий курс по выбору. Название курса должно запрашиваться с клавиатуры и сохраняться как свойство объекта.

4) Создай метод set_average_grade, принимающий все оценки через пробел, разбивающих их на список и считающий средний балл.

Создай экземпляр класса Student с именем и без курса по выбору. Напечатай информацию об объекте.
Затем установи курс по выбору и напечатай обновлённую информацию.

Пример:

Студент(-ка) Иванов
Имеет средний балл: 0
Посещает курс по выбору: -


Введите название курса:>? Физика
Введите оценки через пробел>? 4 5 4 3 2


Студент(-ка) Иванов Валентин
Имеет средний балл: 3.6
Посещает курс по выбору: Физика"""


class Student:
    def __init__(self):
        self.surname = '-'
        self.average_grade = 0
        self.course = '-'

    def print_info(self):
        print('\n')
        print('Студент(-ка)', self.surname)
        print('Имеет средний балл:', self.average_grade)
        print('Посещает курс по выбору:', self.course)
        print('\n')

    def select_surname(self):
        surn = input('Введите фамилию студента:')
        self.surname = surn

    def select_course(self):
        course = input('Введите название курса:')
        self.course = course

    def set_average_grade(self):
        marks = input('Введите оценки через пробел').split()
        summ = 0
        for m in marks:
            summ += int(m)
        av_grade = summ/len(marks)
        av_grade = round(av_grade, 1)
        self.average_grade = av_grade


student = Student()
student.print_info()

student.select_surname()
student.select_course()
student.set_average_grade()

student.print_info()
