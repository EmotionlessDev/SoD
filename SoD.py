import pygame as pg
import sys
from Constants import *
pg.init()


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
        if not player.sprite.in_castle:
            # sky
            sky.draw(virtual_surface)
            # clouds
            clouds.update()
            # world
            vil_decoration_group.update(player.sprite.scroll, virtual_surface)
            vil_blocks_group.update(player.sprite.scroll, virtual_surface)
            vil_script_group.update(player.sprite.scroll, virtual_surface)
            # ground
            ground_collisions = pg.sprite.spritecollide(player.sprite, vil_blocks_group, False)
            script_collisions = pg.sprite.spritecollide(player.sprite, vil_script_group, True)
            # player
            player.update(virtual_surface, ground_collisions, script_collisions)
            # Enemies
            ground_collisions_enemies = pg.sprite.groupcollide(
                enemies_group, vil_blocks_group, False, False
            )
            enemies_group.draw(virtual_surface)
            enemies_group.update(ground_collisions_enemies, vil_blocks_group, virtual_surface)

        else:
            if player.sprite.new_room:
                index = random.randint(0, len(room_list) - 1)
                room = World(room_list[index], room_dec[index], script_list[index], tile_size)
                room.world_generation(cst_blocks_group, cst_decoration_group, cst_script_group,
                                      pictures_bl, pictures_dec, script_blocks,
                                      virtual_surface.get_width() + 3 * tile_size)
                player.sprite.new_room = False
                for enemy in enemies_group:
                    en_hp += 10
                    en_dam += 5
                hill_change = random.randint(1, 10)
                if hill_change == 1:
                    player.sprite.hp += 10
                    if player.sprite.hp == player.sprite.start_hp:
                        player.sprite.start_hp += 10
                player.sprite.damage += 10

            # background
            background_group.draw(virtual_surface)
            # world
            cst_decoration_group.update(player.sprite.scroll, virtual_surface)
            cst_blocks_group.update(player.sprite.scroll, virtual_surface)
            cst_script_group.update(player.sprite.scroll, virtual_surface)
            # ground
            ground_collisions = pg.sprite.spritecollide(player.sprite, cst_blocks_group, False)
            script_collisions = pg.sprite.spritecollide(player.sprite, cst_script_group, True)
            # player
            player.update(virtual_surface, ground_collisions, script_collisions)
            # Enemies
            ground_collisions_enemies = pg.sprite.groupcollide(
                enemies_group, cst_blocks_group, False, False
            )
            enemies_group.draw(virtual_surface)
            enemies_group.update(ground_collisions_enemies, cst_blocks_group, virtual_surface)

    else:
        menu.draw()

    pg.display.flip()
    clock.tick(FPS)
