# Кортежи неизменяемы, но вы можете создать новый кортеж на основе существующего.
# Напишите код, который добавляет элемент 60 к кортежу numbers из предыдущего задания.

numbers = (10, 20, 30, 40, 50)
numbers += (60,)
print(numbers)
