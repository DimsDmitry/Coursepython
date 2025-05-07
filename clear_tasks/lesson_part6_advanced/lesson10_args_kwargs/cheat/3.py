# Создание профиля пользователя
#
# Вы разрабатываете систему профилей пользователей и хотите создать функцию,
# которая принимает обязательные данные: имя и электронная почта,
# и произвольное количество дополнительных параметров: хобби (*args) и доп. информация (**kwargs).

# Пример использования
# user_profile = create_user_profile("Alice", "alice@example.com", "чтение", "путешествия", возраст=30, город="Москва")
# print(user_profile)
# Вывод:
# {'username': 'Alice', 'email': 'alice@example.com', 'hobbies': ('чтение', 'путешествия'), 'additional_info': {'возраст': 30, 'город': 'Москва'}}

def create_user_profile(username, email, *args, **kwargs):
    profile = {
        "username": username,
        "email": email,
        "hobbies": args,
        "additional_info": kwargs
    }
    return profile

# Пример использования
user_profile = create_user_profile("Alice", "alice@example.com", "чтение", "путешествия", возраст=30, город="Москва")
print(user_profile)
# Вывод:
# {'username': 'Alice', 'email': 'alice@example.com', 'hobbies': ('чтение', 'путешествия'), 'additional_info': {'возраст': 30, 'город': 'Москва'}}
