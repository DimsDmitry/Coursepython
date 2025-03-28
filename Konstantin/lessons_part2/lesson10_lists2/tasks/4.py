'''Программа должна запрашивать ввод предмета, пока не введён 0 (сигнал конца ввода).
1. Если такой предмет уже есть в списке, то должно печататься: «Этот предмет уже записан».
2. Если такого предмета ещё нет, то выводится сообщение «Предмет не записан. Добавить его?»
В зависимости от ответа, он добавляется либо нет.

Пример:
Введи предмет (0 - остановить ввод):>? русский
Предмет не записан. Добавить его?>? да
Введи предмет (0 - остановить ввод):>? русский
Этот предмет уже записан
Введи предмет (0 - остановить ввод):>? математика
Предмет не записан. Добавить его?>? да
Введи предмет (0 - остановить ввод):>? ин яз
Предмет не записан. Добавить его?>? нет
Введи предмет (0 - остановить ввод):>? ин яз
Предмет не записан. Добавить его?>? да
Введи предмет (0 - остановить ввод):>? 0
Список предметов: ['русский', 'математика', 'ин яз']
'''