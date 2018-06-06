import pygame


class Ship():
    def __init__(self, ai_settings, screen):
        '''初始化飞船并设置初始位置'''
        self.screen = screen
        self.ai_settings = ai_settings
        # 加载飞船图像并获取外接矩形
        self.image = pygame.image.load('image/a.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将新飞船放在屏幕下中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - 50
        # 在飞船的属性中存小数点
        self.center = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
        # 移动标识
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        # fire
        self.fire_flag = False

    def blitem(self):
        '''在制定位置绘制飞船'''
        self.screen.blit(self.image, self.rect)

    def update(self):
        '''移动标识'''
        # 更新飞船的center值，而不是rect
        if self.moving_right:
            if self.center >= self.ai_settings.screen_width:
                self.moving_right = False
            else:
                self.center += self.ai_settings.ship_speed_factor
        if self.moving_left:
            if self.center <= 0:
                self.moving_left = False
            else:
                self.center -= self.ai_settings.ship_speed_factor
        if self.moving_up:
            if self.centery <= 0:
                self.moving_up = False
            else:
                self.centery -= self.ai_settings.ship_speed_factor
        if self.moving_down:
            if self.centery >= self.ai_settings.screen_height:
                self.moving_up = False
            else:
                self.centery += self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center
        self.rect.centery = self.centery

    def center_ship(self):
        self.center = self.screen_rect.centerx
        self.centery = self.screen_rect.bottom
