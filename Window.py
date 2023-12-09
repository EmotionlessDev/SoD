import pygame as pg
import sys
from canvas import load_image

pg.init()

width_screen, height_screen = 800, 600  # размер экрана
FPS = 60

screen = pg.display.set_mode((width_screen, height_screen), pg.RESIZABLE)  # создание окна
screen_size = screen.get_size()

virtual_surface = pg.Surface((width_screen, height_screen))  # вертуальное пространство

pg.display.set_caption("Shadow of Desolation")  # создание заголовка окна
stone_wall = load_image(r"images/imgonline-com-ua-Resize-4mpm1BvVfOwb16l.jpg")  # задний фон
clock = pg.time.Clock()

play = True
while play:
    for event in pg.event.get():
        if event.type == pg.QUIT:  # нажатие на "х"
            sys.exit()
        if event.type == pg.VIDEORESIZE:
            screen_size = event.size  # регистрация изменения окна


    stone_wall = pg.transform.scale(stone_wall, virtual_surface.get_size())  # установление соответсвия размеров фона и окна
    virtual_surface.blit(stone_wall, [0, 0, width_screen, height_screen])  # установка заднего фона

    scaled_surface = pg.transform.scale(virtual_surface, screen_size)  # адаптация вертуального пространства под размер окна
    screen.blit(scaled_surface, (0, 0))

    pg.display.flip()
    clock.tick(FPS)

