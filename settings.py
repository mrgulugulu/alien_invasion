class Settings():
    #存储所有设置的类
    def __init__(self):
        #初始化游戏的设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        #飞船的设置
        self.ship_speed_factor = 1.5

        #子弹的设置
        self.bullet_speed_factor = 1 #子弹速度系数
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60 #子弹颜色
        self.bullets_allowed = 3 #子弹数量
