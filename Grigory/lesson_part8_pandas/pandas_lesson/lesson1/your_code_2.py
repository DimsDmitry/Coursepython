import pandas as pd


df = pd.read_csv('GoogleApps.csv')

# Сколько стоит (Price) самое дешёвое платное приложение (Type == 'Paid)? 0.99
res = df[df['Type'] == 'Paid']['Price'].min()

# res = df[df['Price'] > 100]['App'].max()   # самое дорогое приложение
print(res)

# Чему равно медианное (median) количество установок (Installs)
# приложений из категории (Category) "ART_AND_DESIGN"?
res = df['Category'].value_counts()
res = df[df['Category'] == 'ART_AND_DESIGN']['Installs'].median()
print(res)

# На сколько максимальное количество отзывов (Reviews) для бесплатных приложений (Type == 'Free')
# больше максимального количества отзывов для платных приложений (Type == 'Paid')?
print(df['Type'].value_counts())
free = df[df['Type'] == 'Free']['Reviews'].max()
paid = df[df['Type'] == 'Paid']['Reviews'].max()
print('Макс кол-во отзывов для бесплатных приложений:', free)
print('Для платных:', paid)
print('Их разница:', free - paid)
print('\n', '#' * 100, '\n')

# Каков минимальный размер (Size) приложения для тинейджеров (Content Rating == 'Teen')?
print(df['Content Rating'].value_counts())
result = df[df['Content Rating'] == 'Teen']['Size'].min()
print('Минимальный размер приложения для подростков:', result)
name_app = df[df['Size'] == result]['App']
print('Его имя:', name_app)
print('\n', '#' * 100, '\n')
# *К какой категории (Category) относится приложение с самым большим количеством отзывов (Reviews)?
result = df[df['Reviews'] == df['Reviews'].max()]['Category']
print(result)  # GAME

# *Каков средний (mean) рейтинг (Rating) приложений стоимостью (Price) более 20 долларов и 
# с количеством установок (Installs) более 10000?
res = df[(df['Price'] > 20) & (df['Installs'] > 10000)]['Rating'].mean()
print(res)