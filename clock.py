# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 11:23:50 2023

@author: davet

Simple clock in pygame

"""


import pygame
import os
import sys

pygame.init()

# Get screen resolution
info = pygame.display.Info()
screen_width = info.current_w
screen_height = info.current_h

# Set window position
window_width = 200
window_height = 100
buffer_x = 50
buffer_y = 50
pos_x = screen_width - window_width - buffer_x
pos_y = buffer_y
os.environ['SDL_VIDEO_WINDOW_POS'] = '%d,%d' % (pos_x, pos_y)

screen = pygame.display.set_mode((window_width, window_height), pygame.NOFRAME)
clock = pygame.time.Clock()

font = pygame.font.Font(None, 36)
text = font.render('12:34', True, (255, 255, 255))
text_rect = text.get_rect(center=(100, 50))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))
    screen.blit(text, text_rect)
    pygame.display.flip()
    clock.tick(60)
