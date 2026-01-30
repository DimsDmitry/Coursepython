import random
import logging  # для логов

import telebot
from telebot import types

# Убедитесь, что файлы лежат в одной папке с этим скриптом
from key import KEY
from help_functions import give_advice, number_of_luck

# запускаем логгирование:
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='helper2_bot.log',
    filemode='a',
    encoding='utf-8'
)

# инициализация бота
bot = telebot.TeleBot(KEY)


# обработчик команды /start
@bot.message_handler(commands=['start'])
def start_message(message):
    # фиксируем действие
    logging.info(f"Пользователь {message.from_user.first_name}, ID {message.chat.id} запустил бота")
    # создаём клавиатуру, которая всплывает при команде start
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
    # фиксируем действие
    logging.info(f"Пользователь {message.from_user.first_name} отправил сообщение: {message.text}")
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
try:
    print(f'Бот успешно запущен. Логи пишутся в helper2_bot.log')
    bot.polling(none_stop=True)
except Exception as e:
    logging.error(f'Критическая ошибка: {e}')