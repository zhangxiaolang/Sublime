import sys
import pygame
import ship
from alien import Alien
from bullet import Bullet

def check_keydown_events(event,ai_settings,screen,ship,bullets):
	if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
		ship.moving_left = True
	elif event.key == pygame.K_UP or event.key == pygame.K_w:
		ship.moving_up = True
	elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
		ship.moving_down = True
	elif event.key == pygame.K_SPACE or event.key == pygame.K_b:
		fire_bullert(ai_settings,screen,ship,bullets)
	elif event.key == pygame.K_q:
		sys.exit()

def check_keyup_events(event,ship):
	if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
		ship.moving_left = False
	elif event.key == pygame.K_UP or event.key == pygame.K_w:
		ship.moving_up = False
	elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
		ship.moving_down = False

def check_events(ai_settings,screen,ship,bullets):
	#响应鼠标键盘事件
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			elif event.type == pygame.KEYDOWN:
				check_keydown_events(event,ai_settings,screen,ship,bullets)

			elif event.type == pygame.KEYUP:
				check_keyup_events(event,ship)

def update_bullets(bullets):
	#更新子弹位置
	bullets.update()

	#删除已消失的子弹
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
	#print(len(bullets))

def update_screen(ai_settings,screen,ship,aliens,bullets):
	#每次循环重新绘制屏幕
	screen.fill(ai_settings.bg_color)
	for bullet in bullets:
		bullet.draw_bullet()
	ship.blitme()
	#alien.blitme()
	aliens.draw(screen)

	#让绘制的屏幕可见
	pygame.display.flip()

def fire_bullert(ai_settings,screen,ship,bullets):
	if len(bullets) < ai_settings.bullers_allowed:
		new_bullet = Bullet(ai_settings,screen,ship)
		bullets.add(new_bullet)

def creat_fleet(ai_settings, screen, aliens):
	"""创建外星人群"""
	#创建一个外星人，并计算一行可容纳多少个外星人
	#外星人间距为外星人宽度
	alien = Alien(ai_settings, screen)
	alien_width = alien.rect.width
	available_space_x = ai_settings.screen_width - 2 * alien_width
	number_alien_x = int(available_space_x / (2 * alien_width))

	#创建第一行外星人
	for alien_number in range(number_alien_x):
		#创建一个外星人并将其加入当前行
		alien = Alien(ai_settings, screen)
		alien.x = alien_width + 2 * alien_width * alien_number
		alien.rect.x = alien.x
		aliens.add(alien)

def get_number_aliens_x(ai_settings, alien_width):
	"""计算每行可以容纳多少外星人"""
	available_space_x = ai_settings.screen_width - 2 * alien_width
	number_alien_x = int(available_space_x / (2 * alien_width))
	return number_alien_x

def create_alien(ai_settings, screen, aliens, alien_number):
	"""创建一个外星人并放在当前行"""
	alien = Alien(ai_settings, screen)