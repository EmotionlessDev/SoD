import pygame as pg
from Blocks import Block
from ScriptBlocks import ScriptBlock
from enemies.Skeleton import Skeleton
pg.init()


class World:
    def __init__(self, world_map, decor, script, tile_size):
        self.world_map = world_map
        self.tile_size = tile_size
        self.decor = decor
        self.script = script

    def world_generation(self, pictures_bl, pictures_dec, pictures_scr, group_spr, group_texture, group_scr, surface):
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

                if self.script[row][col] != " ":
                    if ord(self.script[row][col]) in range(48, 58):
                        if self.script[row][col] == "0":
                            args = (surface, surface.get_width() // 2 - 3 * self.tile_size, self.tile_size, group_spr)
                        elif self.script[row][col] == "1":
                            args = (surface, x, self.tile_size)
                        group_scr.add(ScriptBlock(pictures_scr[self.script[row][col]][0],
                                                  (self.tile_size, self.tile_size), (x, y),
                                                  pictures_scr[self.script[row][col]][1],
                                                  pictures_scr[self.script[row][col]][2],
                                                  pictures_scr[self.script[row][col]][3], args))
                    else:
                        pictures_scr[self.script[row][col]][1].add(Skeleton(
                                                                            *pictures_scr[self.script[row][col]][0],
                                                                            x, y
                        ))
