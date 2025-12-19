import json # java script object notation

from telebot import *
import requests
from currency_converter import CurrencyConverter

from key import SECRET_KEY

bot = telebot.TeleBot(SECRET_KEY)  # создаём объект класса TeleBot - это бот
# API = '135b46a59fd34bb8f2b485d430aa50d7'
currency = CurrencyConverter()  # создаём объект класса CurrencyConverter - конвертер валют
amount = 0  # сумма, которую ввёл пользователь на обмен
bot.delete_webhook()  # очистить старые соединения, чтобы бот запустился корректно


@bot.message_handler(commands=['start'])
# если пришла команда start - запусти функцию ниже (start())
def start(message):
    """Отправляет пользователю приветствие, получает объект message (сообщение) от пользователя"""
    bot.send_message(message.chat.id, 'Привет, введите сумму')
    # бот получает команду - передать то что ввёл пользователь (message), в функцию summa:
    bot.register_next_step_handler(message, summa)


def summa(message):
    """обрабатывает число, введённое пользователем, затем переводит его на кнопки выбора валют"""
    # объявляем количество денег глобальной переменной, чтобы она была распознана во всех функциях
    global amount
    try:
        # очищаем текст от пробелов, пробуем перевести его в int
        amount = int(message.text.strip())
    except ValueError:
        # если не получилось перевести в число (например пользователь ввёл буквы)
        bot.send_message(message.chat.id, 'Неверный формат. Впишите сумму')
        # то отправляем ему сообщение об ошибке и переходим на след действие - эта же функция
        bot.register_next_step_handler(message, summa)  # снова просим ввести сумму
        # если возникла ошибка - завершаем работу функции:
        return

    # если преобразование в int прошло успешно, далее проверяем, чтобы оно было больше 0
    if amount > 0:
        # создаём блок для встроенных кнопок, две кнопки в одном ряду
        markup = types.InlineKeyboardMarkup(row_width=2)
        # создаём кнопки. callback_data - это данные, которые получит бот при нажатии кнопки
        btn1 = types.InlineKeyboardButton('USD/EUR', callback_data='usd/eur')
        btn2 = types.InlineKeyboardButton('EUR/USD', callback_data='eur/usd')
        btn3 = types.InlineKeyboardButton('USD/GBP', callback_data='usd/gbp')
        btn4 = types.InlineKeyboardButton('Другое значение:', callback_data='else')
        markup.add(btn1, btn2, btn3, btn4)  # добавляем все кнопки в блок
        # отправляем сообщение с текстом, к которому прикреплены кнопки
        bot.send_message(message.chat.id, 'Выберите пару валют', reply_markup=markup)
    else:
        # если оно не больше 0 - вызываем функцию повторно
        bot.send_message(message.chat.id, 'Число должно быть больше 0.')
        # след действие - эта же функция
        bot.register_next_step_handler(message, summa)


@bot.callback_query_handler(func=lambda call: True)
# "слушатель" кнопок - если кнопка нажата возвращает True (принимает нажатие любой кнопки)
def callback(call):
    """получает объект call, который содержит данные с кнопки callback_data"""
    if call.data != 'else':
        # если выбрана стандартная кнопка, делаем буквы капсом и делим данные на две части через /
        values = call.data.upper().split('/')
        # выполняем конвертацию. amount - сумма денег,
        # values[0] - что меняем (первый элемент), values[1] - НА что меняем (второй элемент)
        res = currency.convert(amount, values[0], values[1])
        # далее бот отправляет ответ в виде полученной суммы денег, округлённой до сотых
        bot.send_message(call.message.chat.id, f'Получается: {round(res, 2)}. Можете заново вписать сумму')
        # далее повторно вызывается функция summa, тем самым предлагая пользователю снова обменять валюту
        bot.register_next_step_handler(call.message, summa)
    else:
        # если пользователь не выбрал пару валют из предложенных, ему предлагается
        # ввести нужные ему валюты для обмена через "/"
        bot.send_message(call.message.chat.id, 'Введите пару значений через слэш')
        # далее переводим пользователя на функцию my_currency
        bot.register_next_step_handler(call.message, my_currency)


def my_currency(message):
    """функция обрабатывает валюты, введённые пользователем вручную.
    например, RUB/CNY"""
    values = message.text.upper().split('/')  # делаем буквы большими, извлекаем валюты из текста сообщения
    res = currency.convert(amount, values[0], values[1])  # производим конвертацию
    # выводим результат, округлённый до сотых
    bot.send_message(message.chat.id, f'Получается: {round(res, 2)}. Можете заново вписать сумму')
    # далее повторно вызывается функция summa
    bot.register_next_step_handler(message, summa)

# команда, запускающая бота и заставляющая его работать постоянно (как цикл),
# чтобы она постоянно проверял наличие новых сообщений
# none_stop=True - указывает боту, что он должен работать даже если возникла ошибка
bot.polling(none_stop=True)
