import pygame as pg
pg.init()


class BaseCharacter(pg.sprite.Sprite):
    def __init__(self, image_name, frame_count, x, y, width, height):
        pg.sprite.Sprite.__init__(self)

        self.x = x
        self.y = y

        self.image = pg.image.load(r"characters/" + image_name).convert_alpha()
        self.image = pg.transform.scale(self.image, (width * frame_count, height))
        self.frame_width = self.image.get_width() // frame_count
        self.frame_height = self.image.get_height()

        self.rect = pg.Rect(x, y, self.frame_width, self.frame_height)

        self.frame_count = frame_count
        self.frame = 0

        self.on_ground = False

    def draw(self, surface):
        self.rect = pg.Rect(self.x, self.y, self.frame_width, self.frame_height)
        surface.blit(self.image, self.rect,
                     (self.frame_width * int(self.frame), 0, self.frame_width, self.frame_height))
