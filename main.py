#example pygame

import pygame
pygame.init()  #эта ф-я авт-ки иниц-т все необходимые модули pygame. Без нее ничего раб не б.

window_size = (800, 600)  #перем. c размерfvb окна: ширина, высота
screen = pygame.display.set_mode(window_size) #создаём окно
pygame.display.set_caption("Тестовый проект") #название окна

image = pygame.image.load("picPython.png") #загружаем наше изображение
image_rect = image.get_rect()  # загружаем нашу рамку в отдельную переменную

speed = 5 # скорость перемещ картинки - на сколько она б. перемещ за одно нажатие на клавишу


run = True
while run:  #НАЧАЛО БЕСКОНЕЧ.ИГРОВОГО ЦИКЛА. пОКА RUN = истина
    for event in pygame.event.get(): #проходим. по всем событиям
        if event.type == pygame.QUIT: #если событие = крестик (чтобы прг не зависала при наж на крестик, а сразу завершалась)
            run = False #то run = ложь - конец игр цикла
    screen.fill((0,0,0)) #заливает фон окна черным цветом. Двойные скобки - тк передаем кортеж
    screen.blit(image, image_rect)  #эта ф-я отрисовывает и изобр., и его рамку

    pygame.display.flip()  #обновл.содержимое экрана. М исп и update() - весь экран или часть его.

pygame.quit()

