import pygame as pg
import sys
from World import World
from Blocks import Block
from Constants import *
from Menu import Menu
from Clouds import create_cloud
from Maps import *
from enemies.Skeleton import Skeleton  # Skeleton class

pg.init()
pg.time.set_timer(pg.USEREVENT + 1, 3000)

world = World(village_map, village_decoration, village_script, tile_size)
sky = Block(r"textures/world/sky.png", screen_size, (0, 0), 1, (0, 0))

clouds = pg.sprite.Group()
create_cloud(clouds, virtual_surface)
create_cloud(clouds, virtual_surface)
create_cloud(clouds, virtual_surface)

world.world_generation(
    pictures_bl,
    pictures_dec,
    system_blocks,
    blocks_group,
    decoration_group,
    system_group,
    virtual_surface,
)

# Create test skeleton
skeleton = Skeleton(
    import_sprite("./characters/Skeleton/Idle/"),
    import_sprite("./characters/Skeleton/Attack/"),
    import_sprite("./characters/Skeleton/Move/"),
    player,
    100,
    player.sprite.rect.y,
    tile_size - 10,
    tile_size * 2 - 20,
)
enemies_group.add(skeleton)

menu = Menu(r"menu/background_menu.jpg", font, virtual_surface, 40, 241, 71)
while play:
    for event in pg.event.get():
        if event.type == pg.QUIT:  # нажатие на "х"
            sys.exit()
        if event.type == pg.VIDEORESIZE:
            screen_size = event.size  # регистрация изменения окна
        if event.type == pg.KEYDOWN and event.key == pg.K_F12:
            is_full_screen = not is_full_screen
            if is_full_screen:
                last_size = screen_size
                screen_size = full_screen_size
                screen = pg.display.set_mode(screen_size, pg.FULLSCREEN)
            else:
                screen_size = last_size
                screen = pg.display.set_mode(screen_size, pg.RESIZABLE)
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
        system_group.update(player.sprite.scroll, virtual_surface)
        # ground
        ground_collisions = pg.sprite.spritecollide(player.sprite, blocks_group, False)
        script_collisions = pg.sprite.spritecollide(player.sprite, system_group, True)
        # player
        player.update(virtual_surface, ground_collisions, script_collisions)
        # Enemies
        ground_collisions_enemies = pg.sprite.groupcollide(
            enemies_group, blocks_group, False, False
        )
        enemies_group.draw(virtual_surface)
        enemies_group.update(ground_collisions_enemies, blocks_group, virtual_surface, menu)

    else:
        menu.draw()

    pg.display.flip()
    clock.tick(60)
