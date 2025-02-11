#example pygame Видео 3 - Взаимодействие объектов

import pygame
pygame.init()  #эта ф-я авт-ки иниц-т все необходимые модули pygame. Без нее ничего раб не б.
import time  # импортируем библ-ку time для задержки

window_size = (800, 600)  #перем. c размерfvb окна: ширина, высота
screen = pygame.display.set_mode(window_size) #создаём окно
pygame.display.set_caption("Тестовый проект") #название окна

image1 = pygame.image.load("picPython.png") #загружаем наше изображение
image_rect1 = image1.get_rect()  # загружаем нашу рамку в отдельную переменную

image2 = pygame.image.load("cat.png")
image_rect2 = image2.get_rect()

run = True
while run:  #НАЧАЛО БЕСКОНЕЧ.ИГРОВОГО ЦИКЛА. пОКА RUN = истина
    for event in pygame.event.get(): #проходим. по всем событиям
        if event.type == pygame.QUIT: #если событие = крестик (чтобы прг не зависала при наж на крестик, а сразу завершалась)
            run = False #то run = ложь - конец игр цикла
        if event.type == pygame.MOUSEMOTION: #отслеживаем движение мыши
            mouseX, mouseY = pygame.mouse.get_pos() #в две перем-е сохранили коорд х и у нашей мышки
            image_rect1.x = mouseX - 30 # передаем тек знач-е коорд Х мышки рамке изображения
            image_rect1.y = mouseY - 30 # -30 - чт курсор был по центру, смещаем само изобр на -30 относит курсора мыши
    if image_rect1.colliderect(image_rect2):
        print("Произошло столкновение")
        time.sleep(1)


    screen.fill((0,0,0)) #заливает фон окна черным цветом. Двойные скобки - тк передаем кортеж
    screen.blit(image1, image_rect1)  #эта ф-я отрисовывает и изобр., и его рамку
    screen.blit(image2, image_rect2)

    pygame.display.flip()  #обновл.содержимое экрана. М исп и update() - весь экран или часть его.

pygame.quit()
