import pandas as pd
df = pd.read_csv('GoogleApps.csv')

# 1 Сколько всего приложений с категорией ('Category') 'BUSINESS'?
print(df['Category'].value_counts())

print('\n', '#' * 100, '\n')
# 2 Чему равно соотношение количества приложений для подростков ('Teen') и для детей старше 10 ('Everyone 10+')?
# Ответ запиши с точностью до сотых.
table = df['Content Rating'].value_counts()
result = round(table['Teen']/table['Everyone 10+'], 2)
print('Соотношение кол-ва приложений для подростков и для детей 10+:', result)  # 2.73
print('\n', '#' * 100, '\n')
# 3.1 Чему равен средний рейтинг ('Rating') платных ('Paid') приложений? 
# Ответ запиши с точностью до сотых.
result = df.groupby(by='Type')['Rating'].mean()
print(round(result['Paid'], 2))  # 4.25

# 3.2 На сколько средний рейтинг ('Rating') бесплатных ('Free') приложений меньше среднего рейтинга платных ('Paid')?
# Ответ запиши с точностью до сотых.
print(round(result['Paid'] - result['Free'], 2))
print('\n', '#' * 100, '\n')
# 4 Чему равен минимальный и максимальный размер ('Size') приложений в категории ('Category') 'COMICS'?
# Запиши ответы с точностью до сотых.
res = df.groupby(by='Category')['Size'].agg(['min', 'max'])
print(res.loc['COMICS']['min'])
print(res.loc['COMICS']['max'])
print('\n', '#' * 100, '\n')
# Бонус 1. Сколько приложений с рейтингом ('Rating') строго больше 4.5 в категории ('Category') ''?
res = df[df['Rating'] > 4.5]['Category'].value_counts()['FINANCE']
print(res)  # 64
print('\n', '#' * 100, '\n')
# Бонус 2. Чему равно соотношение бесплатных ('Free') и платных ('Paidprint('\n', '#' * 100, '\n')') игр с рейтингом ('Rating') больше 4.9?
res = df[(df['Category'] == 'GAME') & (df['Rating'] > 4.9)]['Type'].value_counts()
print('Количество бесплатных игр:', res['Free'])
print('Количество платных игр:', res['Paid'])
print('Их соотношение:', res['Free']/res['Paid'])