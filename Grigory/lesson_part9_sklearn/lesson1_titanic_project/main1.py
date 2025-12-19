import pandas as pd


# Шаг 1. Загрузка и очистка данных
df = pd.read_csv('titanic.csv')
df.info()
print(df.groupby('Sex')['Survived'].mean())
print(df.pivot_table(index = 'Survived', columns = 'Pclass', values = 'Age', aggfunc = 'mean'))
df.drop(['PassengerId', 'Name', 'Ticket', 'Cabin', 'Embarked', 'Fare'], axis=1, inplace=True)

# вычислим медианный возраст пассажира для каждого класса кают
age1 = df[df['Pclass'] == 1]['Age'].median()
age2 = df[df['Pclass'] == 2]['Age'].median()
age3 = df[df['Pclass'] == 3]['Age'].median()
print(age1, age2, age3)

def fill_age(row):
    if pd.isnull(row['Age']):
        if row['Pclass'] == 1:
            return age1
        if row['Pclass'] == 2:
            return age2
        return age3
    return row['Age']

df['Age'] = df.apply(fill_age, axis=1)

def fill_gender(gender):
    if gender == 'male':
        return 1
    return 0

df['Sex'] = df['Sex'].apply(fill_gender)

def is_alone(row):
    if row['SibSp'] + row['Parch'] == 0:
        return 0
    return 1

df['Alone'] = df.apply(is_alone, axis=1)
df.info() # проверим датафрейм - теперь возраст есть у всех людей, пол заменён со строки на число
# а также создан столбец alone - если 0 - человек путешествовал один, если 1 - с кем-то
print('\n', '#' * 100, '\n')

alone_tab = df.pivot_table(values='Age', columns='Alone', index='Survived', aggfunc='count')
print(alone_tab)
"""Вывод - среди пассажиров, которые были с попутчиками, соотношение выживших и погибших  примерно 1:1,
а среди пассажиров, которые путешествовали в одиночку, количество погибших в 2.3 раз больше выживших"""

df.to_csv('titanic_passengers.csv')



