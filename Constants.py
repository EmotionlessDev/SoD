import pygame as pg
pg.init()

FPS = 60

width_screen, height_screen = 800, 600
screen = pg.display.set_mode((width_screen, height_screen), pg.RESIZABLE)
screen_size = screen.get_size()

virtual_surface = pg.Surface((width_screen, height_screen))
clock = pg.time.Clock()

play = True

tile_size = 50

blocks_group = pg.sprite.Group()
decoration_group = pg.sprite.Group()

pictures = {"g": [r"textures/world/Blocks/grass.png", 1, (0, 0)],
            "G": [r"textures/world/Blocks/ground.png", 1, (0, 0)],
            "D": [r"textures/world/Blocks/dirt.png", 1, (0, 0)],
            "P": [r"textures/castle/portale.png", 8, (0, tile_size * 3)]}

world_map = [
    "                                                  ",
    "                                                  ",
    "                                                  ",
    "                                                  ",
    "                                                  ",
    "                                                  ",
    "  P                                               ",
    "                                                  ",
    "                                                  ",
    "                                                  ",
    "DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD",
    "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG"
]

world_decoration = [
    "                                                  ",
    "                                                  ",
    "                                                  ",
    "                                                  ",
    "                                                  ",
    "                                                  ",
    "                                                  ",
    "                                                  ",
    "                                                  ",
    "gggggggggggggggggggggggggggggggggggggggggggggggggg",
    "                                                  ",
    "                                                  "
]
