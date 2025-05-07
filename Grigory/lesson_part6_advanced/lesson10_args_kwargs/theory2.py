user = {
    'имя': 'лупа',
    'фамилия': 'пупа',
    'пароль': 123
}


for a, b in user.items():
    print(a, b)

for key in user:
    print(key)
    print(user[key])