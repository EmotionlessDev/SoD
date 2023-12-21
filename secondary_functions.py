from os import walk
import pygame
from Blocks import Block
pygame.init()


def import_sprite(path):
    surface_list = []
    for _, __, img_file in walk(path):
        for image in img_file:
            full_path = f"{path}/{image}"
            try:
                img_surface = pygame.image.load(full_path).convert_alpha()
                surface_list.append(img_surface)
            except pygame.error as e:
                print(f"Error loading image {full_path}: {e}")
    return surface_list


def create_barriers(surface, pos_x, tile_size, group):
    barriers_1 = Block(r"textures/world/barrier.png", (1, surface.get_height()),
                       (pos_x - 3 * tile_size, 0), 1, (0, 0))
    barriers_2 = Block(r"textures/world/barrier.png", (1, surface.get_height()),
                       (pos_x + tile_size * 22, 0), 1, (0, 0))
    group.add(barriers_1, barriers_2)
