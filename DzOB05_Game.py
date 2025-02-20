# Игра Пинг - Понг
    
import pygame
import sys

# Инициализация Pygame
pygame.init()

# Устанавливаем параметры окна
WIDTH, HEIGHT = 800, 600
WINDOW_SIZE = (WIDTH, HEIGHT)
BACKGROUND_COLOR = (0, 0, 0)
FPS = 60

# Создаем окно
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Пинг-Понг')

# Цвета
WHITE = (255, 255, 255)

# Параметры ракеток
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
PADDLE_SPEED = 7

# Параметры мяча
BALL_SIZE = 20
BALL_SPEED_X, BALL_SPEED_Y = 5, 5

# Создаем ракетки и мяч
left_paddle = pygame.Rect(30, (HEIGHT - PADDLE_HEIGHT) // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = pygame.Rect(WIDTH - 30 - PADDLE_WIDTH, (HEIGHT - PADDLE_HEIGHT) // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect((WIDTH - BALL_SIZE) // 2, (HEIGHT - BALL_SIZE) // 2, BALL_SIZE, BALL_SIZE)

# Основной игровой цикл
def main():
    clock = pygame.time.Clock()

    ball_speed_x = BALL_SPEED_X
    ball_speed_y = BALL_SPEED_Y

    rnn = True

    while rnn:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rnn = False

        # Получаем состояние клавиш
        keys = pygame.key.get_pressed()

        #Управление левой ракеткой
        if keys[pygame.K_w] and left_paddle.top > 0:
            left_paddle.y -= PADDLE_SPEED
        if keys[pygame.K_s] and left_paddle.bottom < HEIGHT:
            left_paddle.y += PADDLE_SPEED

        # Управление правой ракеткой
        if keys[pygame.K_UP] and right_paddle.top > 0:
            right_paddle.y -= PADDLE_SPEED
        if keys[pygame.K_DOWN] and right_paddle.bottom < HEIGHT:
            right_paddle.y += PADDLE_SPEED

        # Движение мяча
        ball.x += ball_speed_x
        ball.y += ball_speed_y

        # Проверка столкновений с верхней и нижней границами
        if ball.top <= 0 or ball.bottom >= HEIGHT:
            ball_speed_y = -ball_speed_y

        # Проверка столкновений с ракетками
        if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
            ball_speed_x = -ball_speed_x

        # Проверка если мяч вышел за левую или правую границу
        if ball.left <= 0 or ball.right >= WIDTH:
            ball.x = (WIDTH - BALL_SIZE) // 2
            ball.y = (HEIGHT - BALL_SIZE) // 2
            ball_speed_x = BALL_SPEED_X * (-1 if ball_speed_x > 0 else 1)
            ball_speed_y = BALL_SPEED_Y * (-1 if ball_speed_y > 0 else 1)

        # Отрисовка
        screen.fill(BACKGROUND_COLOR)
        pygame.draw.rect(screen, WHITE, left_paddle)
        pygame.draw.rect(screen, WHITE, right_paddle)
        pygame.draw.ellipse(screen, WHITE, ball)
        pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()