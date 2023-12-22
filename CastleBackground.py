import pygame as pg
from Blocks import Block
pg.init()


class CastleBackground:
    def __init__(self, tile_size, group):
        self.tile_size = tile_size
        self.group = group
        self.brick = pg.image.load(r"textures/castle/brick.png")
        self.brick = pg.transform.scale(self.brick, self.tile_size)
        self.rect_brick = self.brick.get_rect()

        self.brick_vine = pg.image.load(r"textures/castle/brick._vine.png")
        self.brick_vine = pg.transform.scale(self.brick_vine, self.tile_size)
        self.rect_brick_vine = self.brick_vine.get_rect()

        self.bg_map = [
            "   a    a       ",
            " a          a   ",
            " a   a   aaa    ",
            "   a       a    ",
            "        a     a ",
            "   aaa     a    ",
            "        a aa    ",
            "    a  a        ",
            "          aaa   ",
            "    a           ",
            "aa        aa    ",
            "     aa         "
        ]

        for row in range(len(self.bg_map)):
            for col in range(len(self.bg_map[row])):
                x = col * self.tile_size[0]
                y = row * self.tile_size[0]

                #  Background drawing
                if self.bg_map[row][col] == " ":
                    self.group.add(Block(r"textures/castle/brick.png", self.tile_size, (x, y), 1, (0, 0)))
                else:
                    self.group.add(Block(r"textures/castle/brick._vine.png", self.tile_size, (x, y), 1, (0, 0)))
