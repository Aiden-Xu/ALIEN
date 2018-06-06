import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, ai_settings, screen):
        '''初始化设置和位置'''
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载外星人图像图像并获取外接矩形
        self.image = pygame.image.load('image/b.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 每个外星人最初在屏幕左上角
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的准确位置
        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)
    def check_edges(self):
        '''如果到达边缘就TRUE'''
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
    def update(self):
        '''向左或右移动'''
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x
