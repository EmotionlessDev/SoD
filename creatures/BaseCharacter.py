import pygame as pg
import Constants

clock = pg.time.Clock()

running = True

class BaseCharacter(pg.sprite.Sprite):
    def __init__(self, image_name, frame_count, x, y, width, height):
        pg.sprite.Sprite.__init__(self)

        self.x = x
        self.y = y

        self.image = pg.image.load(r"creatures/sprites/" + image_name + ".png").convert_alpha()
        self.image = pg.transform.scale(self.image, (width * frame_count, height))

        self.frame_width = int(self.image.get_width() / frame_count)
        self.frame_height = self.image.get_height()


        self.image_rect = pg.Rect(x, y, self.frame_width, self.frame_height)

        self.frame_count = frame_count
        self.frame = 0



    def draw(self):

        self.image_rect = pg.Rect(self.x, self.y, self.frame_width, self.frame_height)

        Constants.virtual_surface.fill("black")
        Constants.virtual_surface.blit(self.image, self.image_rect,
                    (self.frame_width * int(self.frame), 0, self.frame_width, self.frame_height))
        # pg.draw.rect(screen, ("white"), self.image_rect, 2)





