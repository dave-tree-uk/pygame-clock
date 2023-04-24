# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 11:23:50 2023

@author: davet

Simple clock in pygame

"""


import pygame
import time
import sys
import os

# Set window position
os.environ['SDL_VIDEO_WINDOW_POS'] = '%d,%d' % (50, 50)


pygame.init()
screen = pygame.display.set_mode((200, 100), pygame.NOFRAME)
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))
    current_time = time.strftime('%H:%M:%S')
    text = font.render(current_time, True, (255, 255, 255))
    screen.blit(text, (50, 50))
    pygame.display.update()
    clock.tick(1)
