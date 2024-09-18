'''напиши программу, которая выведет текущее время, увеличенное на 2 часа 15 минут'''

from datetime import *

now = datetime.now() + timedelta(hours=2, minutes=15)
print(now)