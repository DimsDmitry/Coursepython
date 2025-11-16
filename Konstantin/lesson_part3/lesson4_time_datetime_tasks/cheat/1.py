'''Напиши программу, которая выведет в консоль по отдельности, сколько секунд, минут, дней и лет прошло с 01.01.1970'''
import time


# Получаем текущее время в секундах с 01.01.1970
current_time = time.time()

# Вычисляем количество лет, дней, минут и секунд
seconds = int(current_time)
minutes = seconds // 60
hours = minutes // 60
days = hours // 24
years = days // 365

# Выводим результаты
print(f"Прошло {seconds} секунд")
print(f"Прошло {minutes} минут")
print(f"Прошло {days} дней")
print(f"Прошло {years} лет")