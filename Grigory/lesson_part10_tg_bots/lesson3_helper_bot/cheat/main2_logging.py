import random
import logging  # Импортируем профессиональную библиотеку для логов
from datetime import datetime

import telebot
from telebot import types

from key import KEY
from help_functions import give_advice, number_of_luck

# --- НАСТРОЙКА ЛОГГИРОВАНИЯ ---
# level=logging.INFO — значит записываем всё, что важнее или равно уровню INFO
# format — задаем внешний вид строки: Время - Уровень - Сообщение
# filename='bot_pro.log' — имя файла, куда пишем
#
# level = logging.INFO,
# format = '%(asctime)s - %(levelname)s - %(message)s',
#
# Эти две строки — «сердце» настройки логгера. Они объясняют Python, как именно должна выглядеть запись в журнале и куда её сохранять.
#
# Давай разберем каждую из них максимально подробно.
#
# 1. format='%(asctime)s - %(levelname)s - %(message)s'
# Это шаблон (маска) строки. Библиотека logging видит знаки % и понимает, что на эти места нужно автоматически подставить данные.
#
# %(asctime)s (ASCII Time): Сюда Python автоматически подставит дату и время события. Тебе не нужно вручную вызывать datetime.now(),
# библиотека сама возьмет системное время.
#
# %(levelname)s: Сюда подставится уровень важности сообщения. Это может быть INFO, WARNING, ERROR или CRITICAL.
# Это помогает быстро найти ошибки в длинном файле, просто пролистав его до слов "ERROR".
#
# %(message)s: Это сам текст сообщения, который ты пишешь внутри скобок, например: logging.info("Бот запущен").
#
# Как это будет выглядеть в файле: 2024-05-20 12:30:01,123 - INFO - Бот запущен

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='bot_pro.log',
    filemode='a',  # Добавлять в конец файла
    encoding='utf-8'
)

# Инициализация бота
bot = telebot.TeleBot(KEY)


# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start_message(message):
    # Вместо своей функции используем метод из библиотеки logging
    logging.info(f"User {message.from_user.first_name} (ID: {message.chat.id}) started the bot")

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Получить совет')
    item2 = types.KeyboardButton('Число удачи')
    item3 = types.KeyboardButton('Помощь')
    markup.add(item1, item2, item3)

    text = f"Привет, {message.from_user.first_name}! Я твой бот-помощник."
    bot.send_message(message.chat.id, text, reply_markup=markup)


# Обработка текстовых сообщений
@bot.message_handler(content_types=['text'])
def handle_text(message):
    # Логируем текст сообщения
    logging.info(f"User {message.from_user.first_name} sent: {message.text}")

    if message.text == 'Получить совет':
        result = give_advice()
        bot.send_message(message.chat.id, result)

    elif message.text == 'Число удачи':
        bot.send_message(message.chat.id, number_of_luck())

    elif message.text == 'Помощь':
        help_markup = types.InlineKeyboardMarkup(row_width=1)
        url_button = types.InlineKeyboardButton(text='Документация TeleBot',
                                                url='https://pypi.org/project/pyTelegramBotAPI/')
        bot_father_button = types.InlineKeyboardButton(text='Как создать своего Бота',
                                                       url='https://help.botman.pro/article/23763')
        help_markup.add(url_button, bot_father_button)

        bot.send_message(message.chat.id, text='Выберите раздел:', reply_markup=help_markup)
    else:
        # Логируем, если бот чего-то не понял (уровень WARNING)
        logging.warning(f"Unknown command from {message.from_user.first_name}: {message.text}")
        bot.send_message(message.chat.id, 'Я пока не знаю, что на это ответить')


# Запуск бота
# Добавим логирование критической ошибки при выключении
try:
    print("Бот запущен. Логи пишутся в bot_pro.log")
    bot.polling(none_stop=True)
except Exception as e:
    logging.error(f"CRITICAL ERROR: {e}")