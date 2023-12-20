import pygame as pg
import random
pg.init()


class Cloud(pg.sprite.Sprite):
    def __init__(self, image, size, surface, x, y, group):
        pg.sprite.Sprite.__init__(self)
        self.size = size
        self.surface = surface
        self.image = pg.image.load(image).convert_alpha()
        self.image = pg.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
        self.speed = random.randint(1, 3)

        self.add(group)

    def update(self):
        if self.rect.x < self.surface.get_width():
            self.rect.x += self.speed + 0.2
            self.surface.blit(self.image, self.rect)
        else:
            self.kill()


def create_cloud(group, surface):
    image_list = [r"textures/world/decorations/nature/cloud_big.png",
                  r"textures/world/decorations/nature/cloud_little.png",
                  r"textures/world/decorations/nature/cloud_md.png"]
    size_list = [(258, 78), (62, 20), (183, 33)]

    index = random.randint(0, len(image_list) - 1)
    x = 0 - size_list[index][0]
    y = random.randint(0, surface.get_height() // 4)

    return Cloud(image_list[index], size_list[index], surface, x, y, group)
