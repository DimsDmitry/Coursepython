import telebot
from telebot import types  # Для работы с кнопками
import random

# 1. Инициализация бота с помощью токена
TOKEN = 'ВАШ_ТОКЕН_ЗДЕСЬ'
bot = telebot.TeleBot(TOKEN)


# 2. Обработчик команды /start
@bot.message_handler(commands=['start'])
def start_message(message):
    # Создаем клавиатуру, которая появится вместо обычной раскладки
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    # Добавляем кнопки
    item1 = types.KeyboardButton("💡 Получить совет")
    item2 = types.KeyboardButton("🎲 Число удачи")
    item3 = types.KeyboardButton("❓ Помощь")

    markup.add(item1, item2, item3)

    # Отправляем сообщение с прикрепленной клавиатурой
    bot.send_message(
        message.chat.id,
        f"Привет, {message.from_user.first_name}! Я твой бот-помощник. Выбери действие в меню ниже:",
        reply_markup=markup
    )


# 3. Обработка текстовых сообщений (нажатий на кнопки ReplyKeyboard)
@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == "💡 Получить совет":
        advices = [
            "Пей больше воды сегодня!",
            "Сделай перерыв на 5 минут и потянись.",
            "Прочитай 10 страниц любой книги.",
            "Напиши план задач на завтра прямо сейчас."
        ]
        bot.send_message(message.chat.id, random.choice(advices))

    elif message.text == "🎲 Число удачи":
        number = random.randint(1, 100)
        # Пример использования Inline-кнопки (под сообщением)
        inline_markup = types.InlineKeyboardMarkup()
        btn = types.InlineKeyboardButton("Попробовать еще раз", callback_data='reroll')
        inline_markup.add(btn)

        bot.send_message(message.chat.id, f"Твое число удачи сегодня: {number}", reply_markup=inline_markup)

    elif message.text == "❓ Помощь":
        bot.send_message(message.chat.id, "Я помогаю тебе быть продуктивным. Нажимай на кнопки внизу!")

    else:
        bot.send_message(message.chat.id, "Я пока не знаю, как на это ответить. Попробуй кнопки меню.")


# 4. Обработка нажатий на Inline-кнопки (callback_data)
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == "reroll":
        # Генерируем новое число при нажатии на кнопку под сообщением
        new_number = random.randint(1, 100)
        # Редактируем старое сообщение, чтобы не спамить в чате
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text=f"Новое число удачи: {new_number}"
        )
        # Отправляем уведомление в верхней части экрана (всплывашка)
        bot.answer_callback_query(call.id, "Обновлено!")


# 5. Запуск бота (бесконечный цикл)
print("Бот запущен...")
bot.polling(none_stop=True)