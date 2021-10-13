import pygame, controls 
from gun import Gun
from pygame.sprite import Group
from stats import Stats



def run():
    pygame.init()                                   #Инициализация игры
    screen = pygame.display.set_mode((700, 800))    # Графическая область игры/ размер окна горизонталь и вертикать
    pygame.display.set_caption('Космические защитники') #название ИГРЫ
    bg_color = (0, 0, 0)                                # фон цвет окна
    gun = Gun(screen)
    bullets = Group()
    inos = Group()
    controls.create_army(screen, inos)
    stats = Stats()

    while True : # любые действия в игре
        controls.events(screen, gun, bullets)
        gun.update_gun()
        controls.update(bg_color, screen, gun, inos, bullets)
        controls.update_bullets(screen ,inos, bullets)
        controls.update_inos(stats, screen, gun, inos, bullets    )

run()
