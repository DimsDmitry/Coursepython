class AgeException(Exception):
    def __init__(self, age, minage, maxage):
        self.age = age
        self.minage = minage
        self.maxage = maxage

    def __str__(self):
        # возвращает строчный аргумент
        text = f'Недопустимое значение: {self.age} '\
                f'Возраст должен быть в диапазоне от {self.minage} до {self.maxage}'
        return text


class Person:
    def __init__(self, name, age):
        self.name = name  # устанавливаем имя
        minage = 1
        maxage = 100
        if minage <= age <= maxage:  # установим возраст
            self.age = age
        else:
            raise AgeException(age, minage, maxage)

    def print_info(self):
        print(f'Человек {self.name}, возраст - {self.age}')


human1 = Person('Олег', -2)
human1.print_info()


