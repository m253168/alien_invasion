import pygame
import sys
import time

pygame.init()
while True:
    screen = pygame.display.set_mode((600, 400))
    screen.fill((0, 0, 255))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            print(event.key)
