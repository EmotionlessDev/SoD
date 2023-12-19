import pygame as pg
import sys
from World import World
from Blocks import Block
from Constants import *
from Player import Player
from Menu import Menu
from Clouds import create_cloud
from import_sprite import import_sprite  # function for importion sprite in dir
from enemies.Skeleton import Skeleton  # Skeleton class
pg.init()
pg.time.set_timer(pg.USEREVENT + 1, 3000)

pg.display.set_caption("Shadow of Desolation")  # создание заголовка окна

world = World(world_map, world_decoration, tile_size)
sky = Block(r"textures/world/sky.png", screen_size, (0, 0), 1, (0, 0))

clouds = pg.sprite.Group()
create_cloud(clouds, virtual_surface)
create_cloud(clouds, virtual_surface)
create_cloud(clouds, virtual_surface)

player = pg.sprite.GroupSingle()
player.add(
    Player(
        r"esev-sheet(main animation).png",
        14,
        virtual_surface.get_width() // 2,
        virtual_surface.get_height() - 4 * tile_size,
        tile_size,
        tile_size * 2
    )
)

world.world_generation(pictures_bl, pictures_dec, blocks_group, decoration_group)

# Create test skeleton
skeleton = Skeleton(
    import_sprite("./characters/Skeleton/Idle/"),
    import_sprite("./characters/Skeleton/Attack/"),
    import_sprite("./characters/Skeleton/Move/"),
    100,
    player.sprite.rect.y,
    player,
)
skeleton_group = pg.sprite.Group()
skeleton_group.add(skeleton)

menu = Menu(r"menu/background_menu.jpg", font, virtual_surface, 40, 241, 71)

while play:
    for event in pg.event.get():
        if event.type == pg.QUIT:  # нажатие на "х"
            sys.exit()
        if event.type == pg.VIDEORESIZE:
            screen_size = event.size  # регистрация изменения окна
        if event.type == pg.USEREVENT + 1 and menu.playing:
            create_cloud(clouds, virtual_surface)
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE and menu.playing:
                menu.playing = False
                menu.fade()

    scaled_surface = pg.transform.scale(virtual_surface, screen_size)
    screen.blit(scaled_surface, (0, 0))

    if menu.playing:
        # sky
        sky.draw(virtual_surface)
        # clouds
        clouds.update()
        # world
        decoration_group.update(player.sprite.scroll, virtual_surface)
        blocks_group.update(player.sprite.scroll, virtual_surface)
        # ground
        ground_collisions = pg.sprite.spritecollide(player.sprite, blocks_group, False)
        # player
        player.update(virtual_surface, ground_collisions)
        # Enemies
        skeleton_group.draw(virtual_surface)
        skeleton_group.update()

    else:
        menu.draw()

    pg.display.flip()
    clock.tick(FPS)
