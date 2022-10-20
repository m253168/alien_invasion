import pygame
import time

class character:

    def __init__(self,screen):
        self.screen = screen
        self.image = pygame.image.load('images/grumpy_cat.bmp')
        self.rect = self.image.get_rect()
        self.rect.center = screen.get_rect().center


    def draw(self):
        self.screen.blit(self.image, self.rect)


pygame.init()
screen = pygame.display.set_mode((600, 400))
screen.fill((245, 236, 206))
cat = character(screen)
cat.draw()
pygame.display.flip()
time.sleep(5)


