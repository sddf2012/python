# from alien_invasion import AlienInvasion
from setting import Settings
import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, settings: Settings, midbottom: tuple) -> None:
        super().__init__()

        self.image = pygame.Surface((settings.bullet_width, settings.bullet_height))
        self.image.fill(settings.bullet_color)
        self.settings = settings
        self.rect = self.image.get_rect()
        self.rect.midbottom = midbottom

    # def blitme(self):
    #     pygame.draw.rect(self.ai_game.screen, self.settings.bullet_color, self.rect)

    def update(self):
        self.rect.y -= self.settings.bullet_speed
