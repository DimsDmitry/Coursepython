users = ['oleg123', 'girl22', 'f_Ivan', 'crazy.dog']
amount_users = len(users)
users.sort()
i = 1
print('Список пользователей:')
for user in users:
      print(i, '-', user)
      i += 1
print('Всего пользователей:', amount_users)