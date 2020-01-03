import sys
import pygame

from settings import Settings
from ship import Ship

def run_game():
    pygame.init()

    #初始化pygame,设置和屏幕对象
    ai_settings = Settings()


    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    #创建一艘飞船
    ship = Ship(screen)




    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(ai_settings.bg_color)
        ship.blitme()

        pygame.display.flip()

run_game()
