s = 'PythonPython'
string = 'Python'

print(s.find(string))  # Возвращает индекс первого совпавшего значения подстроки
print(s.rfind(string))  # Возвращает индекс последнего совпавшего значения подстроки

text = 'Приветствую вас!'
result1 = text.find('в')  # Буква 'в' есть в строке
print(result1)
result2 = text.find('о')  # Буквы 'о' нет в строке
print(result2)

