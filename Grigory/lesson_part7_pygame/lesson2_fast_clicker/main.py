import pygame
import time
from random import randint


pygame.init()  # запуск pygame

# Создаём окно программы:
back = (200, 255, 255)  # цвет
WIDTH, HEIGHT = 510, 400  # размер
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(back)  # заливка цветом
clock = pygame.time.Clock()  # игровой таймер

class Label:
    """Класс прямоугольник"""
    def __init__(self, x, y, width, height, color):
        # создаём прямоугольник:
        self.rect = pygame.Rect(x, y, width, height)
        self.main_color = color

    def color(self, new_color):
        """красит в указанный цвет"""
        self.main_color = new_color

    def fill(self):
        # заливка прямоугольника цветом
        pygame.draw.rect(screen, self.main_color, self.rect)

    def set_text(self, text, fsize, text_color=(0, 0, 0)):
        # создаём объект шрифта
        self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)

    def outline(self, frame_color, thickness):
        """рамка для прямоугольника с текстом"""
        pygame.draw.rect(screen, frame_color, self.rect, thickness)

    def draw(self, shift_x, shift_y):
        """рисуем прямоугольник с текстом и сдвигаем текст"""
        self.fill()
        if self.image:
            screen.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))

    def collidepoint(self, x, y):
        """проверяет клик в конкретной точке, возвращает
        True или False, в зависимости от того в ту ли точку был клик"""
        return self.rect.collidepoint(x, y)



YELLOW = (255, 255, 0)  # жёлтый - для рамки
DARK_BLUE = (0, 0, 114)  # темно-голубой - для текста
BLUE = (73, 74, 255)  # голубой - для обводки рамки

RED = (255, 0, 0)  # клик не туда
GREEN = (1, 217, 71)  # клик туда

LIGHT_GREEN = (214, 255, 179)  # окошко "вы победили"
LIGHT_RED = (255, 137, 144)  # окошко "вы проиграли"


cards = []  # список карточек
num_cards = 4
x = 70

start_time = time.time()  # стартовое время
current_time = start_time  # текущее время

"""музыка"""
pygame.mixer.init()  # подключить музыку
# pygame.mixer.music.load('jungles.ogg')
# pygame.mixer.music.play()

click_right = pygame.mixer.Sound('click_right.ogg')
click_wrong = pygame.mixer.Sound('click_wrong.ogg')
# click_right.set_volume(0.1)

"""надписи игры"""
# время
time_text = Label(0, 0, 50, 50, back)
time_text.set_text('Время:', 20, DARK_BLUE)
time_text.draw(20, 20)

timer = Label(50, 55, 50, 40, back)
timer.set_text('0', 20, DARK_BLUE)
timer.draw(0, 0)

# счёт
score_text = Label(380, 0, 50, 50, back)
score_text.set_text('Счёт:', 20, DARK_BLUE)
score_text.draw(20, 20)

score = Label(430, 55, 50, 40, back)
score.set_text('0', 20, DARK_BLUE)
score.draw(0, 0)


for i in range(num_cards):
    # создаём каждую карточку отдельно
    new_card = Label(x, 170, 70, 100, YELLOW)
    new_card.fill()
    new_card.outline(BLUE, 3)
    new_card.set_text('ТАП', 14)
    cards.append(new_card)  # затем добавляем её в список
    x += 100

wait = 0  # частота смены надписи click
points = 0  # счёт очков

while True:
    """игровой цикл - это бесконечный цикл, на каждом шаге которого
    происходит отрисовка объектов игры, обработка событий извне, обновление фона"""
    if wait == 0:
        # если счётчик кадров опустился до 0, обновляем надпись "клик" и сбрасывает счётчик кадров
        wait = 20  # столько кадров надпись будет на одном месте
        click = randint(1, num_cards)  # рандомим номер карточки
        for i in range(num_cards):
            # находим нужную карточку, оставляем на ней надпись клик
            cards[i].color(YELLOW)
            if i+1 == click:
                cards[i].draw(19, 40)
            else:
                # остальные карточки просто закрашиваем
                cards[i].fill()
    else:
        wait -= 1

    for card in cards:
        card.outline(BLUE, 3)

    """Обработка кликов по карточке"""
    for event in pygame.event.get():
        # проверяем тип события
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # если нажата левая кнопка мыши - проверяем куда именно она попала
            # (x, y) - кортеж с координатами клика. Распакуем его в две разные переменные
            x, y = event.pos
            for i in range(num_cards):  # проверяем индексы 0 1 2 3
                # ищем, в какую ИМЕННО карточку попал клик
                if cards[i].collidepoint(x, y):
                    if i + 1 == click:
                        # попали куда нужно - красим карточку в зелёный
                        click_right.play()  # звук клика
                        cards[i].color(GREEN)
                        points += 1  # увеличиваем счёт очков
                    else:
                        click_wrong.play()  # звук клика
                        # мимо - красным
                        cards[i].color(RED)
                        points -= 1  # уменьшаем счёт очков
                    # не забываем обновить карточки
                    cards[i].fill()
                    score.set_text(str(points), 20, DARK_BLUE)
                    score.draw(0, 0)
                    # и отрисовать изменившийся счёт

    new_time = time.time()  # на каждом шаге цикла заново отмеряется время
    if int(new_time) - int(current_time) == 1:
        # проверяем, есть ли разница в 1 секунду между старым и новым временем
        # если да - устанавливаем новый счёт таймера
        timer.set_text(str(int(new_time - start_time)) , 20, DARK_BLUE)
        timer.draw(0, 0)
        current_time = new_time

    # ВЫИГРЫШ И ПРОИГРЫШ
    if new_time - start_time >= 11:
        # если время достигло 11 секунд - мы проиграли
        win = Label(0, 0, 510, 400, LIGHT_RED)
        win.set_text('Время вышло!', 40, DARK_BLUE)
        win.draw(115, 170)
        break

    if points >= 10:
        # если мы набрали 10 очков - победа
        win = Label(0, 0, 510, 400, LIGHT_GREEN)
        win.set_text('Победа!', 40, DARK_BLUE)
        win.draw(175, 150)
        resul_time = Label(90, 220, 250, 250, LIGHT_GREEN)
        final_time = round(float(new_time - start_time), 2)  # считаем время, за которое игра пройдена
        resul_time.set_text(f'Время прохождения: {str(final_time)} сек.', 20, DARK_BLUE)
        resul_time.draw(0, 0)
        break

    pygame.display.update()  # обновление экрана
    clock.tick(40)  # установка FPS

pygame.display.update()


