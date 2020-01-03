
import pygame
from pygame.sprite import Group


from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    pygame.init()

    #初始化pygame,设置和屏幕对象
    ai_settings = Settings()


    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    #创建一艘飞船
    ship = Ship(ai_settings, screen)
    #创建一个用于存储子弹的编组
    bullets = Group()



    #开始游戏主循环
    while True:


        gf.check_events(ai_settings, screen, ship, bullets)#重构代码，让其变得更加简洁
        ship.update()
        bullets.update()
        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()
