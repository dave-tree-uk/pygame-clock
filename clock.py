# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 11:23:50 2023

@author: davet
"""



import pygame
import time
import sys

pygame.init()
print('hello')
screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))
    current_time = time.strftime('%H:%M:%S')