import sys
import pygame
import datetime
from setting import Settings
from ship import Ship


class AlienInvasion:
    """管理游戏资源和⾏为的类"""

    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)


    def run_game(self):
        """开始游戏的主循环"""
        while True:
            # 侦听键盘和⿏标事件
            # print(datetime.datetime.now(), "开始检查事件")
            self._check_events()
            self.ship.update()
            # 让最近绘制的屏幕可⻅
            self._update_screen()

            self.clock.tick(60)

    def _check_events(self):
        for event in pygame.event.get():
            # print("事件循环", event.type)
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # print("key down right")
                    self.ship.move_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.move_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.move_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.move_left = False

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()

if __name__ == "__main__":
    # 创建游戏实例并运⾏游戏
    ai = AlienInvasion()
    ai.run_game()