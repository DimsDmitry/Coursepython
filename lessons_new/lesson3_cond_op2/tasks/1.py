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
    print("Выберите продукт: мясо или молочные продукты?")
    product = input()
    if product == "мясо":
        print("Какой вкус мяса вам бы хотелось попробовать? (говядина/курица)")
        taste = input()
        if taste == "говядина":
            print("Предлагаем говяжий стейк")
        elif taste == "курица":
            print("Предлагаем куриное филе в сырном соусе")
        else:
            print("Предлагаем мясо по-французски")
    elif product == "молочный":
        print("Какой вкус молочных продуктов вам бы хотелось попробовать? (творог/молоко)")
        taste = input()

        if taste == "творог":
            print("Предлагаем финский творожный пирог")
        elif taste == "молоко":
            print("Предлагаем молочный коктейль")
        else:
            print("Предлагаем сырники")
    else:
        print("Предлагаем вишнёвый пирог")
elif answer == "нет":
    print("До свидания!")