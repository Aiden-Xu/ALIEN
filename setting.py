class Settings():
    '''存储游戏的所有设置'''

    def __init__(self):
        '''初始化游戏的设置'''
        # 屏幕设置
        self.screen_width = 601
        self.screen_height = 400
        self.bg_color = (230, 230, 230)

        #飞船的设置
        self.ship_speed_factor = 1
        self.ship_limit = 2
        #子弹设置
        self.bullet_speed_factor = 2
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allow = 1

        #1为向右，-1为左
        self.fleet_direction = 1

    def addspeed_x(self):
        self.alien_speed_factor *= 1.1
       # print(self.alien_speed_factor)
        return self.alien_speed_factor
    def addspeed_y(self):
        self.fleet_drop_speed *=1.1
      #  print(self.fleet_drop_speed)
        return self.fleet_drop_speed

    def addailen_point(self):
        self.alien_point += 10
        #  print(self.fleet_drop_speed)
        return self.alien_point
    def reset_speed(self):
        # 外星人设置
        self.alien_speed_factor = 0.1
        # 向下的速度
        self.fleet_drop_speed = 1
        #分数
        self.alien_point = 50