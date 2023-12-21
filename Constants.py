import pygame as pg
from secondary_functions import create_barriers
pg.init()

FPS = 60

info = pg.display.Info()
full_screen_size = (info.current_w, info.current_h)
is_full_screen = False

width_screen, height_screen = 800, 600
screen = pg.display.set_mode((width_screen, height_screen), pg.RESIZABLE)
screen_size = screen.get_size()
last_size = screen_size

virtual_surface = pg.Surface((width_screen, height_screen))
clock = pg.time.Clock()

play = True

tile_size = 50

blocks_group = pg.sprite.Group()
decoration_group = pg.sprite.Group()
system_group = pg.sprite.Group()

all_world = pg.sprite.Group(blocks_group, decoration_group)

pictures_bl = {
    "G": [r"textures/world/Blocks/ground.png", 1, (0, 0)],
    "D": [r"textures/world/Blocks/dirt.png", 1, (0, 0)],
    "P": [r"textures/castle/portale.png", 8, (0, tile_size * 3)],
    "F": [r"textures/castle/floor.png", 1, (0, 0)],
    "B": [r"textures/castle/brick.png", 1, (0, 0)],
    "β": [r"textures/castle/brick._vine.png", 1, (0, 0)],
    "0": [r"textures/world/void.png", 1, (0, 0)]}

pictures_dec = {
    "g": [r"textures/world/Blocks/grass.png", 1, (0, 0)],
    "b": [r"textures/world/decorations/nature/bush.png", 1, (tile_size, 0)],
    "T": [r"textures/world/decorations/nature/tree_big.png", 1, (tile_size * 5, tile_size * 4)],
    "t": [r"textures/world/decorations/nature/tree_little.png", 1, (tile_size, tile_size * 2)],
    "F": [r"textures/world/decorations/House/fence_md.png", 1, (0, 0)],
    "h": [r"textures/world/decorations/House/house1.png", 1, (tile_size * 3, tile_size * 3)],
    "S": [r"textures/world/decorations/House/shed.png", 1, (tile_size * 2, tile_size * 2)],
    "w": [r"textures/world/Blocks/wheat.png", 1, (0, 0)],
    "B": [r"textures/castle/brick.png", 1, (0, 0)],
    "β": [r"textures/castle/brick._vine.png", 1, (0, 0)],
    "→": [r"textures/buttons/d.png", 1, (0, 0)],
    "←": [r"textures/buttons/a.png", 1, (0, 0)],
    "↑": [r"textures/buttons/space.png", 1, (tile_size * 2, 0)],
    "l": [r"textures/buttons/lmb.png", 1, (0, 0)],
    "»": [r"textures/buttons/w.png", 1, (0, 0)]}

system_blocks = {
    "0": [r"textures/world/barrier.png", 1, (tile_size * 2, virtual_surface.get_height()), create_barriers]
}

world_map = [
    "                                                                                                                                                                                                                                              ",
    "                                                                                                                                                                                                                                              ",
    "                                                                                                                                                                                                                                              ",
    "                                                                                                                                                                                                                                              ",
    "                                                                                                                                                                                                                                              ",
    "                                                                                                                                                                                                                                              ",
    "       P                                                                                                                                                                                                                                      ",
    "                                                                                                                                                                                                                                              ",
    "                                                                                                                                                                                                                                              ",
    "                                    DDDDDD                                                                                                                                                                                                    ",
    "GGGGGGGGGGGGGGGDDDDDDDDDDDDDDDDDDDDDGGGGGGDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD",
    "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG"
]

world_decoration = [
    "                                                                                                                                                                                                                                              ",
    "                                                                                                                                                                                                                                              ",
    "                                                                                                                                                                                                                                              ",
    "                                                                                                                                                                                                                                              ",
    "                                                                                                                                                                                                                                              ",
    "         ← →                     ↑     T                   T      l                      »            T       T                                       T                                                                                       ",
    "                                                               h                                                                              h              h       h                       h                                                ",
    "                             t                t      t                               S        t                                                                  t        t           S                                                       ",
    "                                    g b                                                                                                                                                                                                       ",
    "                 ggg  g b  gggg   b            gg     g gg   b    FFFFwwwwwwwwwwwwwwwFFFF ggg    b  g b  gggb      gggg FFFwwwwwwwwwwwwwwwwww    FFFFFFFFFFFFF      b        FwwwwwwwF   b                  wwwwwwwwwwwwwwwwwwwwwwwwwwwwwww   ",
    "                                                                                                                                                                                                                                              ",
    "                                                                                                                                                                                                                                              "
]

world_system = [
    "                                                                                                                                                                                                                   0                          ",
    "                                                                                                                                                                                                                                              ",
    "                                                                                                                                                                                                                                              ",
    "                                                                                                                                                                                                                                              ",
    "                                                                                                                                                                                                                                              ",
    "                                                                                                                                                                                                                                              ",
    "                                                                                                                                                                                                                                              ",
    "                                                                                                                                                                                                                                              ",
    "                                                                                                                                                                                                                                              ",
    "                                                                                                                                                                                                                                              ",
    "                                                                                                                                                                                                                                              ",
    "                                                                                                                                                                                                                                              "
]

background_music = pg.mixer.music.load(r'sounds/background_music.wav')
pg.mixer.music.play(-1)

# cursor = pg.image.load(r'menu/cursor.png').convert_alpha()
# pg.mouse.set_visible(False)

font = pg.font.SysFont('serif', 50)
