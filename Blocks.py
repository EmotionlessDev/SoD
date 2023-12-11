import pygame as pg
pg.init()


class Block(pg.sprite.Sprite):

    def __init__(self, image, size, position):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(image).convert_alpha()
        self.image = pg.transform.scale(self.image, size)
        self.rect = self.image.get_rect(topleft=position)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Decoration(Block):

    def __init__(self, image, size, position):
        super().__init__(image, size, position)
