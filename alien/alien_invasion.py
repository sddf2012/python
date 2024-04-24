import sys
import pygame
import datetime
import random
from setting import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from time import sleep
from button import Button
from score import Score


class AlienInvasion:
    """管理游戏资源和⾏为的类"""

    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        self.active = False
        self.play_count = 0
        self.alien_count = 0
        self.destory_alien_count = 0
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

        self.bullets = pygame.sprite.Group()
        self.fire = False

        self.aliens = pygame.sprite.Group()
        self.generate_aliens()

        self.button = Button(self.settings, "play game")
        self.button.rect.center = self.screen.get_rect().center

        self.score = Score(self.settings)

        self.frame_count = 1

    def generate_aliens(self):
        count = self.screen.get_width() // self.settings.alien_width
        while count > 0:
            if random.choice([True, False]):
                alien = Alien(
                    self.settings, (self.settings.alien_width * (count - 1), 0)
                )
                self.aliens.add(alien)
                self.alien_count += 1

            count -= 1

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            # 侦听键盘和⿏标事件
            # print(datetime.datetime.now(), "开始检查事件")
            self._check_events()
            self.screen.fill(self.settings.bg_color)

            # 让最近绘制的屏幕可⻅
            self._update_screen()

            self.frame_count += 1
            pygame.display.flip()
            self.clock.tick(self.settings.frame)

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
                # elif event.key == pygame.K_SPACE:
                #     self.bullets.add(Bullet(self.settings, self.ship.rect.midtop))
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.move_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.move_left = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.button.is_clicked(event.pos) and not self.active:
                    self.active = True
                    self.alien_count = 0
                    self.destory_alien_count = 0
                    self.bullets.empty()
                    self.aliens.empty()
                    self.generate_aliens()
                    self.ship.rect.midbottom = self.screen.get_rect().midbottom
                    self.play_count += 1
                    self.fire = True

    def prepare_play_game(self):
        self.button.draw(self.screen)

    def _update_screen(self):
        if self.active:
            self.process_ship()
            self.process_aliens()
            self.process_bullets()
            self.destory_aliens()
            self.determine_gameover()
        else:
            self.prepare_play_game()
        if self.play_count > 0:
            self.ship.blitme()
            self.bullets.draw(self.screen)
            self.aliens.draw(self.screen)
            self.score.draw(self.screen, self.alien_count, self.destory_alien_count)

    def process_ship(self):
        self.ship.update()

    def process_aliens(self):
        if self.aliens:
            self.aliens.update()
        else:
            self.settings.alien_max_speed_y += 10
            self.generate_aliens()
            print(self.settings.alien_max_speed_y)
        # i = self.aliens_frame_count % (
        #     self.settings.frame * self.settings.alien_generate_speed
        # )
        # if i == 0:
        #     self.aliens_frame_count = 1
        #     self.generate_aliens()

        # self.aliens_frame_count += 1

    def process_bullets(self):
        if self.frame_count % self.settings.bullet_generate_speed == 0:
            self.bullets.add(Bullet(self.settings, self.ship.rect.midtop))
        self.bullets.update()

        for bullet in self.bullets:
            if bullet.rect.y <= 0:
                self.bullets.remove(bullet)

    def destory_aliens(self):
        count = len(self.aliens)
        pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        self.destory_alien_count = self.destory_alien_count + count - len(self.aliens)

    def determine_gameover(self):
        collisions = pygame.sprite.spritecollide(self.ship, self.aliens, False)
        is_gameover = bool(collisions)
        if not is_gameover:
            for alien in self.aliens:
                if alien.reach_bottom:
                    print("alien reach bottom", alien.rect.topleft)
                    is_gameover = True
                    break
        if is_gameover:
            self.active = False


if __name__ == "__main__":
    # 创建游戏实例并运⾏游戏
    ai = AlienInvasion()
    ai.run_game()
