import pygame as pg
pg.init()


class Barrier:
    def __init__(self, width, height, group, x):
        self.width = width
        self.height = height
        self.group = group
        self.x = x

        self.image = pg.image.load(r"textures/world/barrier.png").convert_alpha()
        self.image = pg.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect(topleft=(self.x, 0))
        self.rect.y = 0

        self.group.add(self)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self, scroll, surface):
        self.draw(surface)
        self.rect.move_ip(scroll, 0)
