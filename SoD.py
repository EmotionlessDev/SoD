import pygame as pg
import sys
from World import World
from Blocks import Block
from Constants import *
from Player import Player
from Menu import *
pg.init()

pg.display.set_caption("Shadow of Desolation")  # создание заголовка окна

world = World(world_map, world_decoration, tile_size)
sky = Block(r"textures/world/sky.png", screen_size, (0, 0), 1, (0, 0))
player = Player(r"esev-sheet(main animation).png", 14,
                virtual_surface.get_width() // 2, virtual_surface.get_height() - 4 * tile_size,
                tile_size, tile_size * 2)

world.world_generation(virtual_surface, pictures, blocks_group, decoration_group)

# virtual_surface.blit(cursor, (pg.mouse.get_pos()[0] - 2, pg.mouse.get_pos()[0] - 2))
# x, y = pygame.mouse.get_pos()
#         screen.blit(cursor, (x - 2, y - 2))
#         pygame.display.flip()

while play:
    for event in pg.event.get():
        if event.type == pg.QUIT:  # нажатие на "х"
            sys.exit()
        if event.type == pg.VIDEORESIZE:
            screen_size = event.size  # регистрация изменения окна

        # if event.type == pg.KEYDOWN:
            # if event.key == pg.K_ESCAPE:
            #     Menu.fade()

    scaled_surface = pg.transform.scale(virtual_surface, screen_size)
    screen.blit(scaled_surface, (0, 0))

    sky.draw(virtual_surface)

    decoration_group.update(player.scroll, virtual_surface)
    blocks_group.update(player.scroll, virtual_surface)

    ground_collisions = pg.sprite.spritecollide(player, blocks_group, False)

    player.update(virtual_surface, ground_collisions)

    pg.display.flip()
    clock.tick(FPS)
