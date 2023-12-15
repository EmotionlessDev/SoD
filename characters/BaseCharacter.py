import pygame as pg
pg.init()


class BaseCharacter(pg.sprite.Sprite):
    def __init__(self, image_name, x, y, width, height):
        pg.sprite.Sprite.__init__(self)

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.cur_animation = "base"

        self.frame_count_from_images = {
            "base": 14,
            "attack": 10
        }


        self.images = {
            "base": pg.transform.scale(pg.image.load(r"characters/sprites/" + image_name + "_base.png").convert_alpha(), (self.width * self.frame_count_from_images["base"], self.height)),
            "attack": pg.transform.scale(pg.image.load(r"characters/sprites/" + image_name + "_attack.png").convert_alpha(),(self.width * self.frame_count_from_images["attack"], self.height)),
        }


        self.image = self.images[self.cur_animation]



        self.frame = 0

        self.rect = pg.Rect(self.x, self.y, self.width, self.height)
        self.on_ground = False
        self.last_direction = 'right'
        self.direction = "right"


    def animation(self, animation_name="base"):
        self.cur_animation = animation_name


        frame_count = self.frame_count_from_images[animation_name]
        self.frame = (self.frame + 0.2) % frame_count

        self.image = self.images[self.cur_animation]

        if self.direction =='left':
            self.image = pg.transform.flip(self.image, True, False)

    def walk(self, direction):
        self.animation()
        self.direction = direction
        if self.direction == "right":
            self.x += 10
        elif self.direction == "left":
            self.x -= 10



        self.last_direction = self.direction

    def draw(self, surface):

        # surface.blit(self.image, self.rect,
        #              (self.width * int(self.frame), 0, self.width, self.height))



        self.rect = pg.Rect(self.x, self.y, self.width, self.height)
        surface.blit(self.image, self.rect,
                     (self.width * int(self.frame), 0, self.width, self.height))
