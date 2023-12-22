import pygame as pg
from script_functions import *
from import_sprite import import_sprite  # function for importion sprite in dir
from Player import Player
pg.init()

FPS = 60

info = pg.display.Info()
full_screen_size = (info.current_w, info.current_h)
is_full_screen = False

width_screen, height_screen = 800, 600
screen = pg.display.set_mode((width_screen, height_screen), pg.RESIZABLE)
screen_size = screen.get_size()
last_size = screen_size

pg.display.set_caption("Shadow of Desolation")  # создание заголовка окна
pg.display.set_icon(pg.image.load(r"characters/esev-icon.png"))

virtual_surface = pg.Surface((width_screen, height_screen))
clock = pg.time.Clock()

play = True

tile_size = 50

blocks_group = pg.sprite.Group()
decoration_group = pg.sprite.Group()
system_group = pg.sprite.Group()

player = pg.sprite.GroupSingle()
player.add(
    Player(
        r"esev-sheet(main animation).png",
        14,
        virtual_surface.get_width() // 2,
        virtual_surface.get_height() - 4 * tile_size,
        tile_size,
        tile_size * 2,
    )
)

enemies_group = pg.sprite.Group()

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
    "0": [r"textures/world/barrier.png", 1, (tile_size * 2, virtual_surface.get_height()), create_barriers],
    "1": [r"textures/world/barrier.png", 1, (tile_size * 2, virtual_surface.get_height()), teleport],
    "P": [[import_sprite(r"./characters/Peasant/Idle/"),
          import_sprite(r"./characters/Peasant/Attack/"),
          import_sprite(r"./characters/Peasant/Move/"),
          player], enemies_group],
    "D": [[import_sprite(r"./characters/Dog/Idle/"),
          import_sprite(r"./characters/Dog/Attack/"),
          import_sprite(r"./characters/Dog/Move/"),
          player], enemies_group],
    "F": [[import_sprite(r"./characters/Farmer/Idle/"),
          import_sprite(r"./characters/Farmer/Attack/"),
          import_sprite(r"./characters/Farmer/Move/"),
          player], enemies_group]
}

background_music = pg.mixer.music.load(r'sounds/background_music.wav')
pg.mixer.music.play(-1)

# cursor = pg.image.load(r'menu/cursor.png').convert_alpha()
# pg.mouse.set_visible(False)

font = pg.font.SysFont('serif', 50)
