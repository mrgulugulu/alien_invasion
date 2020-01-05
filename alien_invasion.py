
import pygame
from pygame.sprite import Group
from button import Button
from scoreboard import Scoreboard


from settings import Settings
from ship import Ship
from alien import Alien
from game_stats import GameStats
import game_functions as gf

def run_game():
    pygame.init()

    #初始化pygame,设置和屏幕对象
    ai_settings = Settings()
    #创建一个外星人

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    #创建按钮
    play_button = Button(ai_settings, screen, 'play')

    #创建一个用于存储游戏统计信息的实例,并创建记分牌
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    #创建一艘飞船
    ship = Ship(ai_settings, screen)
    #创建一个用于存储子弹的编组
    bullets = Group()
    aliens = Group()
    #创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    #开始游戏主循环
    while True:

        gf.check_events(ai_settings, screen, stats, play_button, ship,
                aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, 
                aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets,
            play_button)

run_game()
