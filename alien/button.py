import pygame
from setting import Settings

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)


class Button:
    def __init__(self, settings: Settings, text: str):

        self.color = WHITE
        self.rect = pygame.Rect(0, 0, settings.button_width, settings.button_height)
        self.text = text
        self.font = pygame.font.SysFont(None, 30)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        if self.text:
            text_surface = self.font.render(self.text, True, RED)
            text_rect = text_surface.get_rect(center=self.rect.center)
            screen.blit(text_surface, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)
