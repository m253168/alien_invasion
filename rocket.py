import pygame
import sys


class Character:

    def __init__(self, screen):
        # screen = pygame.display.set_mode((600, 400))
        self.screen = screen
        self.image = pygame.image.load('images/grumpy_cat.bmp')
        self.rect = self.image.get_rect()
        self.rect.center = self.screen.get_rect().center
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.screen_rect = screen.get_rect()
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def _check_events(self):
        """respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """responds to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.moving_left = True
        elif event.key == pygame.K_UP:
            self.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()


    def _check_keyup_events(self, event):
        """responds to key releases"""
        if event.key == pygame.K_RIGHT:
            self.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.moving_left = False
        elif event.key == pygame.K_UP:
            self.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.moving_down = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += rocket_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= rocket_speed
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= rocket_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += rocket_speed
        # update rect object from self.x
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self):
        screen.fill((245, 236, 206))
        self.screen.blit(self.image, self.rect)
        pygame.display.flip()

    def run_game(self):
        while True:
            self._check_events()
            self.update()
            self.draw()


pygame.init()
rocket_speed = .5
screen = pygame.display.set_mode((600, 400))
cat = Character(screen)
cat.run_game()
