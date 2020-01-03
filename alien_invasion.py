
import pygame


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




    while True:


        gf.check_events(ship)#重构代码，让其变得更加简洁
        ship.update()
        gf.update_screen(ai_settings, screen, ship)

run_game()
