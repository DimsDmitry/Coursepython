from datetime import datetime  # для фиксирования времени событий
import logging
import random


import telebot
from telebot import types

# Убедитесь, что файлы лежат в одной папке с этим скриптом
from key import KEY
from help_functions import give_advice, number_of_luck

# инициализация бота
bot = telebot.TeleBot(KEY)

# ЛОГГИРОВАНИЕ
def log_action(user_id, user_name, text):
    """функция для записи действий пользователя в текстовом файле
    with open - открыть файл и автоматически закрыть
    a - режим добавление
    utf-8 кодировка"""

    try:
        with open('bot_log.txt', 'a', encoding='utf-8') as f:
            # получаем время в текущем времени
            current_time = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
            """%d - день, %m - месяц, %Y - полный год,
            %H:%M:%S - час, минута, секунда (24ч формат)"""
            log_entry = f'[{current_time}] ID: [{user_id}] Name: [{user_name}] Text: [{text}]\n'
            f.write(log_entry)  # записываем действие в файл
            print(f'Лог записан: {log_entry.strip()}')  # strip - удалить лишние пробелы в начале и конце строки
    except Exception as e:
        # если возникла ошибка - помещаем её в переменную "e" и выводим в консоль
        print(f"Ошибка записи лога: {e}")


# обработчик команды /start
@bot.message_handler(commands=['start'])
def start_message(message):
    # создаём клавиатуру, которая всплывает при команде start
    log_action(message.from_user.id, message.from_user.username, '/start')  # фиксируем действие
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    # создаём кнопки, добавляем их
    item1 = types.KeyboardButton('Получить совет')
    item2 = types.KeyboardButton('Число удачи')
    item3 = types.KeyboardButton('Помощь')

    markup.add(item1, item2, item3)

    # Отправляем сообщение с прикреплённой клавиатурой
    text = f"Привет, {message.from_user.first_name}! Я твой бот-помощник. Выбери действие ниже:"
    bot.send_message(message.chat.id, text, reply_markup=markup)
    # крайний параметр отвечает за то, чтобы клавиатуру привязать к сообщению

# Обработка текстовых сообщений (нажатий на кнопки ReplyKeyboard)
@bot.message_handler(content_types=['text'])
def handle_text(message):
    # фиксируем каждое входящее текстовое сообщение:
    log_action(message.from_user.id, message.from_user.username, message.text)
    # обработка текста
    if message.text == 'Получить совет':
        # give_advice() генерирует рандомный совет, помещает его в переменную result
        result = give_advice()
        # result отправляется пользователю:
        bot.send_message(message.chat.id, result)

    elif message.text == 'Число удачи':
        # number_of_luck() генерирует рандомное число, далее отправка пользователю
        bot.send_message(message.chat.id, number_of_luck())

    elif message.text == 'Помощь':
        # создаём inline-клавиатуру (пульт управления внутри сообщения)
        # row_width = 1 - кнопки будут одна под другой
        help_markup = types.InlineKeyboardMarkup(row_width=1)
        # кнопка с документацией по TeleBot
        url_button = types.InlineKeyboardButton(
            text='Документация TeleBot',
            url='https://pypi.org/project/pyTelegramBotAPI/'
        )
        # кнопка с документацией по BotFather
        bot_father_button = types.InlineKeyboardButton(
            text='Как создать своего Бота',
            url='https://help.botman.pro/article/23763'
        )
        # добавляем всё в один ряд
        help_markup.add(url_button, bot_father_button)
        # отправляем сообщение с этим меню
        bot.send_message(
            message.chat.id,
            text='Добро пожаловать в раздел "Помощь"! Выберите нужный раздел',
            reply_markup=help_markup
        )
    else:
        # если пользователь написал что-то другое (не нажал на кнопки)
        bot.send_message(message.chat.id, 'Я пока не знаю, что на это ответить')

# запускаем бесконечный цикл опроса сервером Telegram
# none_stop=True - бот будет пытаться перезагрузиться даже при сбоях сети
print(f'Бот успешно запущен в {datetime.now().strftime("%d.%m.%Y %H:%M:%S")}')
bot.polling(none_stop=True)