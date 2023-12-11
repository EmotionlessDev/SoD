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

pictures = {"g": r"textures/world/grass.png",
            "G": r"textures/world/ground.png",
            "D": r"textures/world/dirt.png",
            "P": r"textures/world/1102770485_.png.7d2a8d745c6512887de532b62fd12813.png"}

world_map = [
    "                                                  ",
    "                                                  ",
    "                                                  ",
    "                                                  ",
    "                                                  ",
    "                                                  ",
    "  P                                               ",
    "  P                                               ",
    "  P                                               ",
    "  P                                               ",
    "DGGGDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD",
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
    "     ggggggggggggggggggggggggggggggggggggggggggggg",
    "                                                  ",
    "                                                  "
]
