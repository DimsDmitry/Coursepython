import pandas as pd


# Загрузка данных
df = pd.read_csv("StudentsPerformance .csv")

# Преобразование колонок с оценками в числовой формат (если не числовой) и вычисление среднего балла
score_cols = ['math score', 'reading score', 'writing score']


# Удаление строк с пропущенными значениями после преобразования
df.dropna(inplace=True)

# Вычисление среднего балла
df['average_score'] = df[score_cols].mean(axis=1)

print(df['average_score'])
print(df["parental level of education"].value_counts())
print('\n', '=' * 100, '\n')
# Начинаем анализ:
print(df[['parental level of education', 'test preparation course', 'average_score']])
print("-" * 50)

# Группировка по посещению подготовительных курсов и расчет среднего балла
prep_course_impact = df.groupby('test preparation course')['average_score'].mean().sort_values()

print("Средний балл в зависимости от посещения подготовительных курсов:")
print(prep_course_impact)
print('\n', '#' * 100, '\n')