import pandas as pd


# Шаг 1. Загрузка и очистка данных
df = pd.read_csv('titanic.csv')



# Шаг 2. Создание модели
from sklearn.model_selection import train_test_split
# Функция для разбиения исходного набора данных на выборки для обучения и тестирования модели.
from sklearn.preprocessing import StandardScaler
# Класс для стандартизации показателей.
from sklearn.neighbors import KNeighborsClassifier
# Класс для создания и обучения модели.
from sklearn.metrics import confusion_matrix, accuracy_score
# Функции для оценки точности модели

# Отделим целевую переменную от остальных данных

# train_test_split разбивает данные случайным образом на обучающие и тестовые



# Метод fit() подбирает признаки из набора обучающих данных

