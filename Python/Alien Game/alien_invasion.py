import sys
import pygame
import game_functions as gf
from ship import Ship
from settings import Settings
from pygame.sprite import Group
def run_game():
	#初始化游戏并创建一个屏幕对象
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption('Alien Invasion')

	#创建飞船
	ship = Ship(ai_settings,screen)

	#创建子弹编组
	bullets = Group()

	#游戏主循环
	while True:
		#监视键盘鼠标事件
		gf.check_events(ai_settings,screen,ship,bullets)

		#键盘事件监测
		ship.update()
		gf.update_bullets(bullets)

		#每次循环重新绘制屏幕
		gf.update_screen(ai_settings,screen,ship,bullets)

run_game()