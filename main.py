#example pygame

import pygame
pygame.init()  #эта ф-я авт-ки иниц-т все необходимые модули pygame. Без нее ничего раб не б.

window_size = (800, 600)  #перем. c размерfvb окна: ширина, высота
screen = pygame.display.set_mode(window_size) #создаём окно
pygame.display.set_caption("Тестовый проект") #название окна

