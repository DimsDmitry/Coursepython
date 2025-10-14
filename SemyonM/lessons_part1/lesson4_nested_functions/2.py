# Отпускные — это деньги, которые выплачиваются сотруднику во время отпуска вместо зарплаты.
# Сделай программу лаконичнее, чтобы она легко читалась другими сотрудниками и была не длиннее 5 строк.


month_salary = input('Введите зарплату за месяц:')
month_salary = int(month_salary)
vacation = input('Введите количество дней отпуска:')
vacation = int(vacation)
month = 29.5  # среднее количество дней в месяце
daily_salary = month_salary / month
vacation_pay = daily_salary * vacation
print('Примерные отпускные:', vacation_pay)
