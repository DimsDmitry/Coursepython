# вычислите разницу между двумя указанными датами
from datetime import *


first_date = date(2020, 10, 2)
second_date = date(2020, 10, 30)
# Тогда для получения разницы можно использовать следующий код:

delta = second_date - first_date
print(delta)