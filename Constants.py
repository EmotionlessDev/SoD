import pygame as pg
from script_functions import *
from import_sprite import import_sprite  # function for importion sprite in dir
from Player import Player
from World import World
from Blocks import Block
from Menu import Menu
from Maps import *
from Clouds import create_cloud
from CastleBackground import CastleBackground
from enemies.Skeleton import Skeleton  # Skeleton class
pg.init()
pg.time.set_timer(pg.USEREVENT + 1, 3000)


#  System screen size of user's computer
info = pg.display.Info()
full_screen_size = (info.current_w, info.current_h)
is_full_screen = False

#  Start window
width_screen, height_screen = 800, 600
screen = pg.display.set_mode((width_screen, height_screen), pg.RESIZABLE)
screen_size = screen.get_size()
last_size = screen_size
pg.display.set_caption("Shadow of Desolation")  # создание заголовка окна
pg.display.set_icon(pg.image.load(r"characters/esev-icon.png"))

#  Virtual space for create resizable objects
virtual_surface = pg.Surface((width_screen, height_screen))

#  FPS counter
FPS = 60
clock = pg.time.Clock()

#  Trigger condition
play = True

#  Menu
menu = Menu(r"menu/background_menu.jpg", pg.font.SysFont('serif', 50), virtual_surface, 40, 241, 71)

#  Width and height of standard block
tile_size = 50

#  Blocks groups for village
vil_blocks_group = pg.sprite.Group()
vil_decoration_group = pg.sprite.Group()
vil_script_group = pg.sprite.Group()

#  Characters
player = pg.sprite.GroupSingle()
player.add(
    Player(
        virtual_surface.get_width() // 2,
        virtual_surface.get_height() - 4 * tile_size,
        tile_size,
        tile_size * 2,
    )
)
enemies_group = pg.sprite.Group()

#  Dicts with textures and scripts
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
script_blocks = {
    "0": [r"textures/world/barrier.png", 1, (tile_size * 2, virtual_surface.get_height()),
          create_barriers, (virtual_surface, virtual_surface.get_width() // 2 - 3 * tile_size,
                            tile_size, vil_blocks_group)],
    "1": [r"textures/world/barrier.png", 1, (tile_size * 2, virtual_surface.get_height()),
          teleport, (menu.fade, enemies_group, player.sprite)],
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

#  Background music
background_music = pg.mixer.music.load(r'sounds/background_music.wav')
#pg.mixer.music.play(0)

#  Start location
village = World(village_map, village_decoration, village_script, tile_size)
sky = Block(r"textures/world/sky.png", screen_size, (0, 0), 1, (0, 0))
clouds = pg.sprite.Group()
create_cloud(clouds, virtual_surface)
create_cloud(clouds, virtual_surface)
create_cloud(clouds, virtual_surface)
village.world_generation(
    pictures_bl,
    pictures_dec,
    script_blocks,
    vil_blocks_group,
    vil_decoration_group,
    vil_script_group,
    virtual_surface,
)

#  Block groups for castle
background_group = pg.sprite.Group()
cst_blocks_group = pg.sprite.Group()
cst_decoration_group = pg.sprite.Group()
cst_script_group = pg.sprite.Group()

#  Castle location
castle_background = CastleBackground((tile_size, tile_size), background_group)
castle = World(front_entrance_map, front_entrance_decoration, front_entrance_script, tile_size)
castle.world_generation(
    pictures_bl,
    pictures_dec,
    script_blocks,
    cst_blocks_group,
    cst_decoration_group,
    cst_script_group,
    virtual_surface
)
