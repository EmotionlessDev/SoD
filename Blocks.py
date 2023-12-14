import pygame as pg
pg.init()


class Block(pg.sprite.Sprite):

    def __init__(self, image, size, position, columns, re_size):
        pg.sprite.Sprite.__init__(self)
        self.size = (size[0] + re_size[0], size[1] + re_size[1])
        self.position = position
        self.columns = columns
        self.image_sheets = pg.image.load(image).convert_alpha()
        self.frames = [self.image_sheets.subsurface(
            pg.Rect(((self.image_sheets.get_width() // self.columns) * x, 0),
                    (self.image_sheets.get_width() // self.columns, self.image_sheets.get_height()))
        ) for x in range(self.columns)]

        self.cur_frame = 0
        self.image = self.frames[0]
        self.image = pg.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect(topleft=self.position)

        self.last_update = pg.time.get_ticks()
        self.frame_rate = 100

    def animation(self):
        if self.columns > 1:
            now = pg.time.get_ticks()
            if now - self.last_update > self.frame_rate:
                self.last_update = now
                self.cur_frame = (self.cur_frame + 1) % self.columns

    def draw(self, surface):
        self.animation()
        self.image = self.frames[self.cur_frame]
        self.image = pg.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect(topleft=self.position)
        surface.blit(self.image, self.rect)

    def update(self, x, surface):
        self.draw(surface)
        self.rect.move_ip(x, 0)
        self.position = self.rect.x, self.rect.y


class Decoration(Block):

    def __init__(self, image, size, position, columns, re_size):
        super().__init__(image, size, position, columns, re_size)
