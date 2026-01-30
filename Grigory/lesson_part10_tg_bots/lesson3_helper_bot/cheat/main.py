import random
from datetime import datetime  # Импортируем datetime для фиксации времени событий

import telebot
from telebot import types

# Импортируем ваши данные (убедитесь, что файлы лежат в одной папке с этим скриптом)
from key import KEY
from help_functions import give_advice, number_of_luck

# Инициализация бота с использованием вашего ключа
bot = telebot.TeleBot(KEY)


# --- НОВАЯ ФУНКЦИЯ: ЛОГИРОВАНИЕ ---
def log_action(user_id, user_name, text):
    """
    Функция для записи действий пользователя в текстовый файл.
    'with open' автоматически закрывает файл после записи.
    'a' (append) — режим добавления новых данных в конец файла.
    'utf-8' — кодировка для поддержки русского языка.
    """
    try:
        with open("bot_log.txt", "a", encoding="utf-8") as f:
            # Получаем время в удобном формате: День.Месяц.Год Часы:Минуты
            current_time = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
            log_entry = f"[{current_time}] ID: {user_id} | Name: {user_name} | Message: {text}\n"
            f.write(log_entry)
            print(f"Лог записан: {log_entry.strip()}")  # Дублируем в консоль для контроля
    except Exception as e:
        print(f"Ошибка записи лога: {e}")


# ОБРАБОТЧИК КОМАНДЫ /start
@bot.message_handler(commands=['start'])
def start_message(message):
    # Логируем запуск бота конкретным пользователем
    log_action(message.chat.id, message.from_user.first_name, "/start")

    # Создаём клавиатуру, которая всплывает при команде start
    # resize_keyboard=True делает кнопки компактными по высоте
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    # Создаём кнопки (KeyboardButton — это кнопки-шаблоны для отправки текста)
    item1 = types.KeyboardButton('Получить совет')
    item2 = types.KeyboardButton('Число удачи')
    item3 = types.KeyboardButton('Помощь')

    # Добавляем все кнопки в объект клавиатуры
    markup.add(item1, item2, item3)

    # Отправляем сообщение с прикреплённой клавиатурой
    text = f"Привет, {message.from_user.first_name}! Я твой бот-помощник. Выбери действие ниже:"
    bot.send_message(message.chat.id, text, reply_markup=markup)
    # Параметр reply_markup отвечает за то, чтобы привязать кнопки к этому сообщению


# ОБРАБОТКА ТЕКСТОВЫХ СООБЩЕНИЙ (нажатий на кнопки ReplyKeyboard или ручного ввода)
@bot.message_handler(content_types=['text'])
def handle_text(message):
    # Логируем каждое входящее текстовое сообщение
    log_action(message.chat.id, message.from_user.first_name, message.text)

    # Обработка текста "Получить совет"
    if message.text == 'Получить совет':
        # give_advice() генерирует рандомный совет из help_functions.py
        result = give_advice()
        bot.send_message(message.chat.id, result)

    # Обработка текста "Число удачи"
    elif message.text == 'Число удачи':
        # number_of_luck() генерирует рандомное число
        bot.send_message(message.chat.id, number_of_luck())

    # Обработка текста "Помощь" (Переход к Inline-кнопкам)
    elif message.text == 'Помощь':
        # Создаём inline-клавиатуру (кнопки-"пульт" прямо под сообщением)
        # row_width = 1 - кнопки будут располагаться строго одна под другой
        help_markup = types.InlineKeyboardMarkup(row_width=1)

        # InlineKeyboardButton не отправляет текст в чат, а работает как ссылка или сигнал
        url_button = types.InlineKeyboardButton(
            text='Документация TeleBot',
            url='https://pypi.org/project/pyTelegramBotAPI/'
        )
        bot_father_button = types.InlineKeyboardButton(
            text='Как создать своего Бота',
            url='https://help.botman.pro/article/23763'
        )

        # Добавляем кнопки в меню помощи
        help_markup.add(url_button, bot_father_button)

        # Отправляем сообщение с Inline-кнопками
        bot.send_message(
            message.chat.id,
            text='Добро пожаловать в раздел "Помощь"! Выберите нужный раздел:',
            reply_markup=help_markup
        )

    # Если пользователь написал что-то другое (не предусмотренное кнопками)
    else:
        bot.send_message(message.chat.id, 'Я пока не знаю, что на это ответить. Попробуй кнопки меню!')


# ЗАПУСК БОТА
# polling — метод постоянного опроса серверов Telegram на наличие новых сообщений
# none_stop=True — бот будет пытаться перезапуститься даже при временных сбоях сети
print(f"Бот успешно запущен в {datetime.now().strftime('%H:%M:%S')}")
bot.polling(none_stop=True)