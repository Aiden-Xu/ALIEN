import pygame.font


class Scoreboard():
    # 显示的分信息的类
    def __init__(self, ai_settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # 显示得分信息的字体
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None,48)
        #准备初始得分图像
    def prer_score(self):
        '''把得分弄成图像'''
        rounded_score = int(round(self.stats.score,-1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str,True,self.text_color,self.ai_settings.bg_color)
        #得分放到右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
    def prer_score1(self):
        '''最高分'''
        rounded_score = int(round(self.stats.h_score,-1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str,True,(80, 225, 30),self.ai_settings.bg_color)
        #得分放到左上
        self.score_rect = self.score_image.get_rect()
        self.score_rect.left = self.screen_rect.left + 20
        self.score_rect.bottom =  self.screen_rect.bottom
    def show_score(self):
        self.screen.blit(self.score_image,self.score_rect)
