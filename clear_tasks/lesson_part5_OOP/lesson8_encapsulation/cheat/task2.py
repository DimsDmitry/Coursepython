# Создайте класс User, который хранит информацию о пользователе. Он обладает двумя свойствами: логин и пароль.
# Свойство "пароль" должно быть приватным.
# Напишите метод check_password, который будет принимать пароль, сравнивать его с настоящим и
# по результату проверки возвращать True или False

class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def check_password(self, password):
        return self.__password == password


user1 = User('Дима', 125)
print(user1.check_password(123))
