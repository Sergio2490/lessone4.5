#Игра Арканоид
import pygame
import sys
pygame.init()  #Иниуиализация Pygame

#Параметры окна
screen_width, screen_height = 600, 400
screen = pygame.display.set_mode((screen_width, screen_height))  #создаем окно с размерами
pygame.display.set_caption("Арканоид")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# ФПС
clock = pygame.time.Clock() # счетчик времени
FPS = 60   #кол-во кадров в секунду

# Параметры платформы
paddle_width, paddle_height = 100, 10
paddle_x = (screen_width - paddle_width) // 2  # коорд х - ставим платформу по центру окна игры
paddle_y = screen_height - paddle_height - 20 # по оси у - ставим пратформу чуть выше нижнего края окна
paddle_speed = 6 #скорость платформы

# Параметры мяча
ball_radius = 8
ball_x = screen_width //2  # по оси х - ставим мяч по центру окна
ball_y = paddle_y - ball_radius # по у - мяч лежит на платформе
ball_speed_x = 4
ball_speed_y = -4

#Запуск основного цикла игры
running = True   # если переменная станет False, то цикл остановится
while running:
    #Обработка событий
    for event in pygame.event.get():   # перебираем события в игре
        if event.type == pygame.QUIT:  # если произошло событие выхода - крестик справа вверху окна
            running = False            # то завершаем цикл и выходим из программы
