import pygame as pg
import sys
from World import World
from Blocks import Decoration
from Constants import *
pg.init()

pg.display.set_caption("Shadow of Desolation")  # создание заголовка окна

world = World(world_map, world_decoration, tile_size)
sky = Decoration(r"textures/world/sky.png", screen_size, (0, 0), 1, (0, 0))

world.world_generation(virtual_surface, pictures, blocks_group, decoration_group)

while play:
    for event in pg.event.get():
        if event.type == pg.QUIT:  # нажатие на "х"
            sys.exit()
        if event.type == pg.VIDEORESIZE:
            screen_size = event.size  # регистрация изменения окна

    scaled_surface = pg.transform.scale(virtual_surface, screen_size)
    screen.blit(scaled_surface, (0, 0))

    sky.draw(virtual_surface)

    decoration_group.update(0, virtual_surface)
    blocks_group.update(0, virtual_surface)

    pg.display.flip()
    clock.tick(FPS)
