import sys, pygame
from pygame.sprite import Group
from alienwork.setting import *
from alienwork.ship import Ship
import alienwork.game_functions as gf
from alienwork.game_stats import GameStats
from alienwork.button import Button
from alienwork.scoreboard import Scoreboard

def run_game():
    # 初始化屏幕
    pygame.init()
    ai_settings = Settings()
    ai_settings.reset_speed()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # 开始按钮
    play_button = Button(ai_settings, screen, 'Play')
    # 一艘飞船
    ship = Ship(ai_settings, screen)
    # 存子弹的编组
    bullets = Group()
    # 外星人
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)
    # 用于统计当局信息的实类和记分牌
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings,screen,stats)
    sb1 = Scoreboard(ai_settings,screen,stats)
    sb1.prer_score1()
    # 主循环
    while True:
        sb.prer_score()
        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, aliens, ship, bullets,sb,stats,sb1)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button,sb,sb1)


run_game()
