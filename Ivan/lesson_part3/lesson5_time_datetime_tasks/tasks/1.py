'''Напиши программу, которая выведет в консоль по отдельности, сколько секунд, минут, дней и лет прошло с 01.01.1970'''
from time import *
seconds = time()
mins = seconds/60
days = mins/60/24
years = days/365

print('С 01.01.1970 прошло:')
print(seconds, 'секунд')
print(mins, 'минут')
print(days, 'дней')
print(years, 'лет')