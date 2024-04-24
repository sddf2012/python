import pygame
from setting import Settings

BLUE = (66, 193, 240)


class Score:
    def __init__(self, settings: Settings):
        self.rect = pygame.Rect(settings.screen_width-settings.score_width, 0, settings.score_width, settings.score_height)
        self.font = pygame.font.SysFont('simsun', 20)
        self.settings = settings

    def draw(self, screen, sum, score):
        self.text = f"外星人:{sum};总分:{score}"
        pygame.draw.rect(screen, self.settings.bg_color, self.rect)
        text_surface = self.font.render(self.text, True, BLUE)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)
