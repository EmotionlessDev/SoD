import pygame as pg
pg.init()

wight, height = 800, 600
FPS = 60

screen = pg.display.set_mode((wight, height))
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
         "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG",
         "EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE",
         "EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE",
         "EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE"]

tile_size = 50

world_x, world_y = 0, -tile_size * (len(world) - (height // tile_size))

play = True
while play:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            play = False
    keys = pg.key.get_pressed()
    if keys[pg.K_a]:
        world_x += 10
    if keys[pg.K_d]:
        world_x -= 10

    if keys[pg.K_s]:
        world_y -= 10
    if keys[pg.K_w]:
        world_y += 10

    screen.fill("blue")

    for row in range(len(world)):
        for col in range(len(world[row])):
            x = world_x + col * tile_size
            y = world_y + row * tile_size

            if world[row][col] == " ":
                pg.draw.rect(screen, pg.Color('gray67'), (x, y, tile_size, tile_size), 1)
            elif world[row][col] == "G":
                pg.draw.rect(screen, pg.Color("green"), (x, y, tile_size, tile_size))
            elif world[row][col] == "E":
                pg.draw.rect(screen, pg.Color('brown'), (x, y, tile_size, tile_size))

    pg.display.update()
    clock.tick(FPS)
