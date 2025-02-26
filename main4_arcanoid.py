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

    # Движение платформы
    keys = pygame.key.get_pressed()  # Считываем нажатие на клавиши
    if keys[pygame.K_LEFT] and paddle_x >0:  # нажата стрелка влево и положение платформы не выходит за пред. экрана слева
        paddle_x -= paddle_speed   # перемещаем платформу влево
    if keys[pygame.K_RIGHT] and paddle_x < screen_width - paddle_width:
        paddle_x += paddle_speed

    # Движение мяча
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Столкновение с краями экрана
    if ball_x <= 0 or ball_x >= screen_width: # если мяч сталкивается с краями экрана, меняем его скорость
        ball_speed_x = -ball_speed_x   # (а значит, и направление на противоположные
    if ball_y <= 0:
        ball_speed_y = -ball_speed_y
    if ball_y >= screen_height:
        #Сброс мяча, если он столкнулся с нижним краем экрана (упал)
        ball_x, ball_y = screen_width // 2, paddle_y-ball_radius
        ball_speed_y = -ball_speed_y

    # Столкновение мяча с платформой
    if paddle_x <= ball_x <= paddle_x + paddle_width and paddle_y <= ball_y + ball_radius <= paddle_y +paddle_height:
        ball_speed_y = -ball_speed_y

    # Очистка экрана
    screen.fill(BLACK)  # Заливка экрана черным цветом

    # Отрисовка платформы и мяча
    pygame.draw.rect(screen, WHITE, (paddle_x, paddle_y, paddle_width, paddle_height))
    pygame.draw.circle(screen, BLUE, (ball_x, ball_y), ball_radius)

    # Обновление экрана
    pygame.display.flip()

    # Ограничение количества кадров в секунду (Контроль FPS)
    clock.tick(FPS)  #чтобы не было слишком много кадров в сек, иначе слишком много раз в сек цикл сработает и слишком быстро передвинет мяч

pygame.quit()
sys.exit()







