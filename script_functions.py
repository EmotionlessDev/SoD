from os import walk
import pygame
from Blocks import Block
pygame.init()


def create_barriers(surface, pos_x, tile_size, group):
    #  Creating barriers
    barriers_1 = Block(r"textures/world/barrier.png", (1, surface.get_height()),
                       (pos_x - 3 * tile_size, 0), 1, (0, 0))
    barriers_2 = Block(r"textures/world/barrier.png", (1, surface.get_height()),
                       (pos_x + tile_size * 22, 0), 1, (0, 0))
    group.add(barriers_1, barriers_2)


def teleport(fade, group, obj):
    fade()
    group.empty()
    obj.in_castle = True
    pass
