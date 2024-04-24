class Settings:
    """存储游戏《外星⼈⼊侵》中所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.frame=60

        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        self.bullet_generate_speed=20

        self.alien_width=50
        self.alien_height=50
        self.alien_max_speed_x=50
        self.alien_max_speed_y=50
        self.alien_generate_speed=4
        
        self.button_width=120
        self.button_height=50
        
        self.score_width=200
        self.score_height=50