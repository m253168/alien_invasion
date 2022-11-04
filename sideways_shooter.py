import pygame
import sys
from pygame.sprite import Sprite


class Character:

    def __init__(self, screen):
        # screen = pygame.display.set_mode((600, 400))
        self.screen = screen
        self.image = pygame.image.load('images/ship_rotate.bmp').convert()
        self.rect = self.image.get_rect()
        self.rect.left = self.screen.get_rect().left
        self.y = float(self.rect.y)
        self.screen_rect = screen.get_rect()
        self.moving_up = False
        self.moving_down = False
        self.bullets = pygame.sprite.Group()

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
        # if event.key == pygame.K_RIGHT:
        #     self.moving_right = True
        # elif event.key == pygame.K_LEFT:
        #     self.moving_left = True
        if event.key == pygame.K_UP:
            self.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()


    def _check_keyup_events(self, event):
        """responds to key releases"""
        # if event.key == pygame.K_RIGHT:
        #     self.moving_right = False
        # elif event.key == pygame.K_LEFT:
        #     self.moving_left = False
        if event.key == pygame.K_UP:
            self.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.moving_down = False


    def _fire_bullet(self):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)


    def update(self):
        # if self.moving_right and self.rect.right < self.screen_rect.right:
        #     self.x += rocket_speed
        # if self.moving_left and self.rect.left > 0:
        #     self.x -= rocket_speed
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= rocket_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += rocket_speed
        # update rect object from self.x
        # self.rect.x = self.x
        self.rect.y = self.y

    def draw(self):
        screen.fill((245, 236, 206))
        self.screen.blit(self.image, self.rect)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()

    def run_game(self):
        while True:
            self._check_events()
            self.update()
            self.draw()
            self.bullets.update()

            for bullet in self.bullets.copy():
                if bullet.rect.right >= self.screen_rect.right:
                    self.bullets.remove(bullet)

class Bullet(Sprite):

    def __init__(self,rocket_game):
        super().__init__()
        self.bullet_speed = 1.0
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3
        self.screen = rocket_game.screen
        self.color = self.bullet_color

        self.rect = pygame.Rect(0,0,self.bullet_width,self.bullet_height)
        self.rect.midright = rocket_game.rect.midright
        self.x = float(self.rect.x)

    def update(self):
        self.x += self.bullet_speed
        self.rect.x = self.x

    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)


pygame.init()
rocket_speed = .5
screen = pygame.display.set_mode((600, 400))
cat = Character(screen)
cat.run_game()
