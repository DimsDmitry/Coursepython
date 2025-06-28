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
        self.outline(BLUE, 5)  # Рисуем обводку при отрисовке
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

cards = []  # список карточек
num_cards = 4
x = 70
wait = 20  # частота смены надписи click


for i in range(num_cards):
    # создаём каждую карточку отдельно
    new_card = Label(x, 170, 70, 100, YELLOW)
    new_card.outline(BLUE, 100)
    new_card.set_text('ТАП', 14)
    cards.append(new_card)  # затем добавляем её в список
    x += 100

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
        card.draw(19, 40)


    pygame.display.update()  # обновление экрана
    clock.tick(40)  # установка FPS