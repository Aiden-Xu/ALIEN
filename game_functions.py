import sys, pygame
import time
from alienwork.bullet import Bullet
from alienwork.alien import Alien
from alienwork.button import Button


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    '''按下去'''
    if event.key == pygame.K_RIGHT:
        # 向右移动
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # 向左移动
        ship.moving_left = True
    elif event.key == pygame.K_DOWN:
        # 向下移动,y轴是反的
        ship.moving_down = True
    elif event.key == pygame.K_UP:
        # 向上移动
        ship.moving_up = True
    elif event.key == pygame.K_q:  # exit game
        sys.exit()
    elif event.key == pygame.K_SPACE:
        ship.fire_flag = True


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        # 向右移动
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        # 向左移动
        ship.moving_left = False
    elif event.key == pygame.K_DOWN:
        # 向下移动,y轴是反的
        ship.moving_down = False
    elif event.key == pygame.K_UP:
        # 向上移动
        ship.moving_up = False
    elif event.key == pygame.K_SPACE:
        ship.fire_flag = False


def check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets):
    '''响应按键和鼠标'''
    # 监视外设
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y)


def check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active = True
        # 清空外星人和子弹
        aliens.empty()
        bullets.empty()
        # 创建新外星人
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        ai_settings.reset_speed()


def update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button, sb, sb1):
    '''更新屏幕上的图像，并切换到新屏幕'''
    screen.fill(ai_settings.bg_color)
    if ship.fire_flag:
        auto_fire(ai_settings, screen, ship, bullets)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitem()
    aliens.draw(screen)
    sb.show_score()
    sb1.show_score()
    # 如果游戏没开始，draw个按钮
    if not stats.game_active:
        play_button.draw_button()
    # 屏幕可见
    pygame.display.flip()


def update_bullets(ai_settings, screen, aliens, ship, bullets, sb, stats, sb1):
    '''更新子弹位置，并删除消失的子弹'''
    bullets.update()
    # 删除消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # 检查子弹和外星人是否碰撞，并删除
    check_bullet_alien_collisions(ai_settings, screen, aliens, ship, bullets, sb, stats, sb1)


def check_bullet_alien_collisions(ai_settings, screen, aliens, ship, bullets, sb, stats, sb1):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_point * len(aliens)
            sb.prer_score()
            if (stats.score > stats.h_score):
                stats.h_score = stats.score
                sb1.prer_score1()
    if len(aliens) == 0:
        bullets.empty()
        ai_settings.addspeed_x()
        ai_settings.addspeed_y()
        ai_settings.addailen_point()
        create_fleet(ai_settings, screen, ship, aliens)


def auto_fire(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allow:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def get_number_aliens_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - (2 * alien_width)
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
    '''计算可容纳多少行'''
    available_space_y = (ai_settings.screen_height - (5 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    '''创建外星人组'''
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    row_numbers = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    # 创建多行
    for row_number in range(row_numbers):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def check_fleet_edges(ai_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    '''下移并改变方向'''
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    if stats.ships_left > 0:
        stats.ships_left -= 1
        # 清空外星人和子弹
        aliens.empty()
        bullets.empty()
        # 重新创建
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        time.sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break


def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    '''更新外星人位置'''
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    # 监测与飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)
