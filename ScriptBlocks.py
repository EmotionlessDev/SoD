import pygame as pg
from Blocks import Block
pg.init()


class ScriptBlock(Block):
    def __init__(self, image, size, position, columns, re_size, command, args):
        super().__init__(image, size, position, columns, re_size)
        self.command = command
        self.args = args
        self.size = (size[0] + re_size[0], size[1] + re_size[1])
        self.image = pg.image.load(image).convert_alpha()
        self.image = pg.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect(topleft=self.position)
