# Шаг 2. Создание модели
import pandas as pd

from sklearn.model_selection import train_test_split
# Функция для разбиения исходного набора данных на выборки для обучения и тестирования модели.
from sklearn.preprocessing import StandardScaler
# Класс для стандартизации показателей.
from sklearn.neighbors import KNeighborsClassifier
# Класс для создания и обучения модели.
from sklearn.metrics import confusion_matrix, accuracy_score

# подключаем очищенный датафрейм
df = pd.read_csv('titanic_passengers.csv')
print(df)

# Отделим целевую переменную от остальных данных
X = df.drop('Survived', axis=1)
y = df['Survived']

# train_test_split разбивает данные случайным образом на обучающие и тестовые
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

# создаём StandardScaler для обработки данных в понятный sklearn формат
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.fit_transform(X_test)

# создаём классификатор по методу ближайшего соседа
classifier = KNeighborsClassifier(n_neighbors=5)
classifier.fit(X_train, y_train)  # передаём ему обработанные данные

# Метод fit() подбирает признаки из набора обучающих данных

y_pred = classifier.predict(X_test)  # предсказываем выживаемость людей

# Функции для оценки точности модели