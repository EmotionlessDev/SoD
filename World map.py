import pygame as pg
from Player import Player
from textures import *
pg.init()

width, height = 800, 600
FPS = 60

screen = pg.display.set_mode((width, height))
clock = pg.time.Clock()

world = ["                                                  ",
         "                                                  ",
         "                                                  ",
         "                                                  ",
         "                                                  ",
         "                                                  ",
         "                                                  ",
         "                                                  ",
         "                                                  ",
         "                                                  ",
         "                                                  ",
         "                                                  ",
         "                                                  ",
         "                                                  ",
         "                                                  ",
         "                                                  ",
         "                                                  ",
         "                                                  ",
         "                                                  ",
         "                                                  ",
         "                                                  ",
         "EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE",
         "EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE",
         "EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE",
         "EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE"]

tile_size = 50

world_x, world_y = 0, -tile_size * (len(world) - (height // tile_size))

player = Player("images/imgonline-com-ua-Resize-4mpm1BvVfOwb16l.jpg",
                screen.get_width() // 2, screen.get_height() - world_y - tile_size)

play = True
while play:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            play = False

    keys = pg.key.get_pressed()
    if player.rect.center[0] < screen.get_width() // 2 - tile_size * 2.5:
        if world_x != player.rect.center[0]:
            world_x += 1
    elif player.rect.center[0] > screen.get_width() // 2 + tile_size * 2.5:
        if world_x != player.rect.center[0]:
            world_x -= 1

    # if keys[pg.K_s]:
    #     world_y -= 10
    # if keys[pg.K_w]:
    #     world_y += 10

    screen.fill("blue")

    for row in range(len(world)):
        for col in range(len(world[row])):
            x = world_x + col * tile_size
            y = world_y + row * tile_size

            if world[row][col] == " ":
                pg.draw.rect(screen, pg.Color('gray67'), (x, y, tile_size, tile_size), 1)
            elif world[row][col] == "E":
                ground.draw(screen, x, y)

    player.player_move()
    player.update([grass_ground])

    pg.display.update()
    clock.tick(FPS)
