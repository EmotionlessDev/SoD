import pygame as pg
from Blocks import Block
pg.init()


class World:
    def __init__(self, world_map, decor, tile_size):
        self.world_map = world_map
        self.tile_size = tile_size
        self.world_x = 0
        self.decor = decor

    def world_generation(self, surface, pictures, group_spr, group_texture):
        for row in range(len(self.world_map)):
            for col in range(len(self.world_map[row])):
                x = self.world_x + col * self.tile_size
                y = row * self.tile_size

                if self.world_map[row][col] == " ":
                    pg.draw.rect(surface, pg.Color('gray67'), (x, y, self.tile_size, self.tile_size), 1)
                else:
                    group_spr.add(Block(pictures[self.world_map[row][col]][0],
                                        (self.tile_size, self.tile_size), (x, y),
                                        pictures[self.world_map[row][col]][1],
                                        pictures[self.world_map[row][col]][2]))

                if self.decor[row][col] != " ":
                    group_texture.add(Block(pictures[self.decor[row][col]][0],
                                            (self.tile_size, self.tile_size), (x, y),
                                            pictures[self.decor[row][col]][1],
                                            pictures[self.decor[row][col]][2]))
