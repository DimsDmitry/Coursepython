import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='helper2_bot.log',
    filemode='a',
    encoding='utf-8'
)

"""
level=logging.INFO - значит записываём всё, что важнее или равно уровню INFO
DEBUG, INFO, WARNING, ERROR, CRITICAL

format - внешний вид строки, время-имя-уровень-сообщение

asctime (ASCII) - сюда Python автоматически подставит дату и время события.
Теперь не нужна библиотека datetime
name - имя пользователя
levelname - уровень важности сообщения. Это может быть один из указанных выше уровней, 
что помогает быстро найти ошибки, просто пролистав до слова ERROR

message - сам текст сообщения

filemode='a' - режим ДОзаписи, т.е. добавляем текст к имеющемуся

encoding='utf-8' - кодировка текста в русский
"""