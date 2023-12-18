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

all_world = pg.sprite.Group(blocks_group, decoration_group)

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
    "       P                                          ",
    "                               D                  ",
    "               DDDD      D     D                  ",
    "                        D      D                  ",
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
    "ggggggggggg                                       ",
    "                                                  ",
    "                                                  "
]

background_music = pg.mixer.music.load(r'sounds/background_music.wav')
pg.mixer.music.play(-1)

# cursor = pg.image.load(r'menu/cursor.png').convert_alpha()
# pg.mouse.set_visible(False)

font = pg.font.SysFont('serif', 50)
