'''напиши программу, которая выведет текущее время, увеличенное на 2 часа 15 минут'''

from datetime import datetime, timedelta
clock_in_half_hour = datetime.now() + timedelta()

print(clock_in_half_hour)