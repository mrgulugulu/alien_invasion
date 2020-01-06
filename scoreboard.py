import pygame.font
from pygame.sprite import Group

from ship import Ship

class Scoreboard():
    '''显示得分信息的类'''
    def __init__(self, ai_settings, screen, stats):
        '''初始化显示得分涉及的属性'''
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        #显示得分信息时使用的字体设置
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        #准备初始得分图像和最高得分
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        '''将得分转换为一幅渲染的图像'''
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)#字符串格式设置指令
        self.score_image = self.font.render(score_str, True, self.text_color,
            self.ai_settings.bg_color)#创建图像的render()

        #将得分放在屏幕右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        #右边缘与屏幕右边缘相距20像素
        self.score_rect.top = 20#上边缘与屏幕上边缘相距20像素

    def show_score(self):
        '''在屏幕上显示得分'''
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        #绘制飞船
        self.ships.draw(self.screen)

    def prep_high_score(self):
        '''将最高得分转换为渲染的图像'''
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "Score {:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True,
                self.text_color, self.ai_settings.bg_color)

        #将最高得分放在屏幕中央
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx#居中
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        '''将等级转换为渲染的图像'''
        self.level_image = self.font.render('Level' + str(self.stats.level), True,
                self.text_color, self.ai_settings.bg_color)

        #将等级放在得分之下
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right#等级与得分右对齐
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        '''显示还剩下多少艘飞船'''
        self.ships = Group()#存储飞船实例
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width #贴近屏幕左边
            ship.rect.y = 10
            self.ships.add(ship)
