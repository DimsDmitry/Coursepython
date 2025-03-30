while True:
    try:
        children_amount = int(input('Введите число детей'))
        sweets_amount = int(input('Введите количество конфет'))
        break
    except:
        print('Ошибка! Количество должно быть целым числом')
#допиши вычисление порции с обработкой деления на 0

try:
   portion = sweets_amount/children_amount
   print('Каждый ребёнок получит', portion, 'конфет(-ы)')
except:
   print('Ошибка деления! Возможно, пришло 0 детей?')