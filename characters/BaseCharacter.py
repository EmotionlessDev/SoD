import pygame as pg
pg.init()


class BaseCharacter(pg.sprite.Sprite):
    def __init__(self, image_name, x, y, width, height):
        pg.sprite.Sprite.__init__(self)

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image_name = image_name

        self.cur_animation = "base"

        self.correctiveW = 0
        self.correctiveH = 0

        self.settings_in_images = {
            # frame count / speed
            "base": (14, 0.3),
            "attack": (10, 0.6)
        }
        
        self.images = {
            "base": pg.image.load(r"characters/sprites/" + self.image_name + "_base.png").convert_alpha(),
            "attack": pg.image.load(r"characters/sprites/" + self.image_name + "_attack.png").convert_alpha()
        }


        self.image = self.images[self.cur_animation]



        self.frame = 0

        self.rect = pg.Rect(self.x , self.y , self.width, self.height)
        self.on_ground = False
        self.last_direction = 'right'
        self.direction = "right"





    def walk(self, direction):
        self.animation()
        self.direction = direction
        if self.direction == "right":
            self.x += 10
        elif self.direction == "left":
            self.x -= 10

        self.last_direction = self.direction
    def attack(self):
        self.animation('attack')

    def animation(self, animation_name="base"):
        if animation_name != self.cur_animation:
            self.frame = 0

        self.cur_animation = animation_name


        frame_count = self.settings_in_images[animation_name][0]

        self.frame = (self.frame + self.settings_in_images[animation_name][1]) % frame_count

        self.image = self.images[self.cur_animation]

        if self.direction =='left':
            self.image = pg.transform.flip(self.image, True, False)


    def draw(self, surface):
        if self.cur_animation == "base":
            cur_image = pg.transform.scale(self.image,
                                       (self.width * self.settings_in_images["base"][0], self.height))
            self.rect = pg.Rect(self.x, self.y, self.width, self.height)

            surface.blit(cur_image, self.rect,
                         ((self.width ) * int(self.frame), 0, self.width,
                          self.height))

        elif self.cur_animation == "attack":
            cur_image = pg.transform.scale(self.image,
                                       ((self.width +6 )  * self.settings_in_images["attack"][0] , self.height + 10))
            self.rect = pg.Rect(self.x + 3, self.y - 10, self.width, self.height)

            surface.blit(cur_image, self.rect,
                         ((self.width + 6) * int(self.frame), 0, self.width + 6, self.height ))









        # pg.draw.rect(surface, (64, 128, 255),
        #                  (self.x, self.y, self.width + self.correctiveW, self.height + self.correctiveH), 2)