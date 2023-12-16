import pygame as pg

pg.init()


class BaseCharacter(pg.sprite.Sprite):
    def __init__(self, image_name, x, y, width, height):
        pg.sprite.Sprite.__init__(self)

        self.x = x
        self.y = y
        self.width = 100
        self.height = 200

        self.frame_count_from_images = {
            "base": 14,
            "attack": 10
        }

        self.kW = pg.image.load(r"characters/sprites/" + image_name + "_attack.png").convert_alpha().get_width() // self.frame_count_from_images["base"] // width
        self.kH = pg.image.load(r"characters/sprites/" + image_name + "_attack.png").convert_alpha().get_height() // height



        self.imagesNotNormalize = {
            "base": pg.image.load(r"characters/sprites/" + image_name + "_base.png").convert_alpha(),
            "attack": pg.image.load(r"characters/sprites/" + image_name + "_attack.png").convert_alpha(),
        }
        # ----------------
        self.images = {}

        for image_type in self.imagesNotNormalize.keys():
            width = self.imagesNotNormalize[image_type].get_width() * self.kW
            height = self.imagesNotNormalize[image_type].get_height() * self.kH
            self.images[image_type] = pg.transform.scale(
                pg.image.load(r"characters/sprites/" + image_name + "_" + image_type + ".png").convert_alpha(),
                (width, height))

        self.cur_animation = "base"
        self.image = self.images[self.cur_animation]
        self.frame = 0

        self.rect = pg.Rect(self.x, self.y, self.width * self.kW  , self.height * self.kH)
        self.on_ground = False
        self.last_direction = 'right'
        self.direction = "right"

    def animation(self, animation_name="base"):
        self.cur_animation = animation_name

        frame_count = self.frame_count_from_images[animation_name]
        self.frame = (self.frame + 0.2) % frame_count

        self.image = self.images[self.cur_animation]

        if self.direction == 'left':
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

        self.rect = pg.Rect(self.x, self.y, self.width, self.height)
        surface.blit(self.image, self.rect,
                     (self.width * int(self.frame), 0, self.width * self.kW, self.height * self.kH))
