import pygame
import time

pygame.init()
rocket_speed = 1
moving_right = False
moving_left = False


class character:

    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('images/grumpy_cat.bmp')
        self.rect = self.image.get_rect()
        self.rect.center = screen.get_rect().center
        self.x = float(self.rect.x)

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if moving_left:
            self.x -= rocket_speed
        if moving_right:
            self.x += rocket_speed


class rocket:
    def moving(self):
        for event in pygame.event.get():
            if event.type == pygame.quit():
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    moving_right = True
            elif event.key == pygame.K_LEFT:
                moving_right = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    moving_right = False
                elif event.key == pygame.K_LEFT:
                    moving_left = False


screen = pygame.display.set_mode((600, 400))
screen.fill((245, 236, 206))
cat = character(screen)
cat.draw()
pygame.display.flip()
time.sleep(30)

if __name__ == '__main__':
    game = rocket()
    game.run_game()
