"""Напишите программу, в которой будет предлагаться опробовать новые блюда в меню. Если пользователь желает начать, ему
необходимо ввести “да”. Затем он выбирает продукт, который хотел бы попробовать: мясо или молочные продукты. После
выбора продукта, нужно уточнить его вкус.

Структура:
Желаете попробовать наше новое меню?
Если введено "да", предлагаем вкус:

    1) Если введено "мясо", а затем:
    говядина - предлагается говяжий стейк
    курица - куриное филе в сырном соусе
    во всех остальных случаях - мясо по-французски

    2) Если введено "молочный", а затем:
    творог - финский творожный пирог
    молоко - молочный коктейль
    во всех остальных случаях - сырники

    3) Во всех остальных случаях - вишнёвый пирог

Если введено "нет", выводим сообщение "До свидания!"
"""

print("Желаете попробовать наше новое меню?")
answer = input()
if answer == "да":

