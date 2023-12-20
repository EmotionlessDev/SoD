import pygame as pg
from Blocks import Block
from SystemBlocks import SkriptBlock
pg.init()


class World:
    def __init__(self, world_map, decor, system, tile_size):
        self.world_map = world_map
        self.tile_size = tile_size
        self.decor = decor
        self.system = system

    def world_generation(self, pictures_bl, pictures_dec, pictures_sys, group_spr, group_texture, group_sys, surface):
        for row in range(len(self.world_map)):
            for col in range(len(self.world_map[row])):
                x = col * self.tile_size
                y = row * self.tile_size

                if self.world_map[row][col] != " ":
                    group_spr.add(Block(pictures_bl[self.world_map[row][col]][0],
                                        (self.tile_size, self.tile_size), (x, y),
                                        pictures_bl[self.world_map[row][col]][1],
                                        pictures_bl[self.world_map[row][col]][2]))

                if self.decor[row][col] != " ":
                    group_texture.add(Block(pictures_dec[self.decor[row][col]][0],
                                            (self.tile_size, self.tile_size), (x, y),
                                            pictures_dec[self.decor[row][col]][1],
                                            pictures_dec[self.decor[row][col]][2]))

                if self.system[row][col] != " ":
                    group_sys.add(SkriptBlock(pictures_sys[self.system[row][col]][0],
                                              (self.tile_size, self.tile_size), (x, y),
                                              pictures_sys[self.system[row][col]][1],
                                              pictures_sys[self.system[row][col]][2],
                                              pictures_sys[self.system[row][col]][3],
                                              (surface, x, self.tile_size, group_spr)))
