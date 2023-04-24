# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 11:23:50 2023

@author: davet

Simple clock in pygame

"""
import pygame
import os
import sys
from datetime import datetime

pygame.init()

# Get screen resolution
info = pygame.display.Info()
screen_width = info.current_w
screen_height = info.current_h

# Set window position
window_width = 100
window_height = 50
buffer_x = 50
buffer_y = 50
pos_x = screen_width - window_width - buffer_x
pos_y = buffer_y
os.environ['SDL_VIDEO_WINDOW_POS'] = '%d,%d' % (pos_x, pos_y)

screen = pygame.display.set_mode((window_width, window_height), pygame.NOFRAME)
clock = pygame.time.Clock()

font = pygame.font.Font(None, 42)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get current time and update text surface
    now = datetime.now()
    time_string = now.strftime('%H:%M')
    text = font.render(time_string, True, (255, 255, 255))
    text_rect = text.get_rect(center=(50, 25))

    screen.fill((0, 0, 0))
    screen.blit(text, text_rect)
    pygame.display.flip()
    clock.tick(60)
