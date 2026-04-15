from datetime import *


# класс date отвечает за работу с датами
new_date = date(2029, 9, 11)
print(new_date)

# получить конкретное свойства - день, месяц или год
print(type(new_date))
print(new_date.year)
print(new_date.month)
print(new_date.day)

# replace позволяет заменить конкретные значения даты
new_date = new_date.replace(year=2020)
print(new_date)

# today - актуальная дата. функция получает данные от системы.
print(date.today())

# weekday() позволяет получить число от 0 до 6, где 0 - ПН, 6 - ВС
somedate = date(2025, 9, 1)
weekday = somedate.weekday()
print(weekday)
print('\n', '#' * 100, '\n')
# isoweekday() позволяет получить число от 1 до 7, где 1 - ПН, 7 - ВС
somedate = date(2025, 9, 1)
weekday = somedate.isoweekday()
print(weekday)
print('\n', '=' * 100, '\n')
# класс time позволяет создать объект времени из параметров: час, минута, секунда, микросекунда
# не принимает обязательные параметры, значит если мы что-то пропустим то значение будет равно 0
sometime = time(15, 12)
print(sometime)

sometime = time(13, 25, 14, 12)
print(sometime)

sometime = sometime.replace(hour=19, second=21)  # replace также работает
print(sometime)

# класс datetime объединяет дату и время в одном объекте класса, чтобы работать сразу со всеми
# единицами времени. принимает до 6 параметров, 3 обязательных - год, месяц, день
somedate = datetime(2025, 9, 1, 12, 35, 51, 14)
print(somedate)
print(datetime(2021, 11, 12))

print('\n', '=' * 100, '\n')

# создать объект datetime отдельно из классов date и time - функция combine
some_date = date(2025, 9, 1)
some_time = time(12, 25)
full_time = datetime.combine(some_date, some_time)
print(full_time)
print(type(full_time))

# now - текущее время из системных часов
print(datetime.now())

# timestamp - кол-во секунд с 01.01.1970, до указанной даты
print(datetime.timestamp(datetime.now()))

print('\n', '=' * 100, '\n')
'''АРИФМЕТИЧЕСКИЕ ОПЕРАЦИИ СО ВРЕМЕНЕМ'''
# разница между датами
date1 = date(2025, 9, 1)
date2 = date(2023, 9, 14)
print(date1 - date2)

# поиск будущей даты
cur_date = date(2025, 3, 25)
change = timedelta(days=30)
future_date = cur_date + change
print(future_date)

# поиск прошлой даты
cur_date = date(2025, 3, 25)
change = timedelta(days=30)
future_date = cur_date - change
print(future_date)

# создание часового пояса
new_zone = timezone(timedelta(hours=2), name='Ural')
print(datetime.now(new_zone))
