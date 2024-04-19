import pygame


class Ship:
    """管理⻜船的类"""

    def __init__(self, ai_game):
        """初始化⻜船并设置其初始位置"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        # 加载⻜船图像并获取其外接矩形
        originalImage = pygame.image.load("alien/images/ship.bmp")
        self.image = pygame.transform.scale(originalImage, (50, 50))
        self.rect = self.image.get_rect()
        # 每艘新⻜船都放在屏幕底部的中央
        self.rect.midbottom = self.screen_rect.midbottom

        self.settings = ai_game.settings
        self.pos_max = self.settings.screen_width - self.rect.width
        self.pos_min = 0
        self.speed = 5.5
        self.move_right = False
        self.move_left = False

    def blitme(self):
        """在指定位置绘制⻜船"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.move_right:
            pos = self.rect.x + self.speed
            if pos >= self.pos_max:
                pos = self.pos_max
            self.rect.x = pos
        elif self.move_left:
            pos = self.rect.x - self.speed
            if pos <= self.pos_min:
                pos = self.pos_min
            self.rect.x = pos
