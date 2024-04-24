import pygame
import random
from setting import Settings


class Alien(pygame.sprite.Sprite):
    def __init__(self, settings: Settings, topleft: tuple):
        super().__init__()

        self.settings = settings

        originalImage = pygame.image.load("alien/images/alien.bmp")
        self.image = pygame.transform.scale(
            originalImage, (settings.alien_width, settings.alien_height)
        )
        self.rect = self.image.get_rect()
        self.rect.topleft = topleft
        self.frame_count = 0
        self.reach_bottom = False

    def update(self):
        if self.reach_bottom:
            return
        self.frame_count += 1
        if self.frame_count % self.settings.frame != 0:
            return
        speed_x = random.randint(
            -self.settings.alien_max_speed_x, self.settings.alien_max_speed_x
        )
        speed_y = random.randint(0, self.settings.alien_max_speed_y)
        x = self.rect.x + speed_x
        y = self.rect.y + speed_y
        width = self.rect.width
        height = self.rect.height
        if x + width > self.settings.screen_width or x < 0:
            x = self.rect.x
        if y + height >= self.settings.screen_height:
            y = self.settings.screen_height - height
            self.reach_bottom=True

        self.rect.x = x
        self.rect.y = y
