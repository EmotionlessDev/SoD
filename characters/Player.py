import pygame as pg
from characters.BaseCharacter import BaseCharacter
pg.init()


class Player(BaseCharacter):

    def __init__(self, image_name, x, y, width, height):
        super().__init__(image_name, x, y, width, height)

        self.player_gravity = 0
        self.player_terminal_velocity = 10
        self.jump_y = 0
        self.is_jumped = False

        self.__last__jerk_ticks = pg.time.get_ticks()
        self.__last_increase_interval_ticks = 0



    def jerk(self):
        jerk_value = 150

        if pg.time.get_ticks() - self.__last__jerk_ticks >= 1300:
            if self.last_direction == "right":
                self.x += jerk_value
            else:
                self.x -= jerk_value

            self.__last__jerk_ticks = pg.time.get_ticks()

    def apply_gravity(self, ground_collisions):
        if ground_collisions:
            for ground in ground_collisions:
                if self.rect.bottom >= ground.rect.top + 10:
                    self.rect.bottom = ground.rect.top + 10
                    self.player_gravity = 0
                    self.on_ground = True
        elif self.player_gravity < self.player_terminal_velocity:
            self.on_ground = False
            self.player_gravity += 1
        self.y += self.player_gravity

    def jump(self):
        self.y += -50 + 0.5

    def attack(self):
        self.animation('attack')
        print("seffsfse")

    def controls(self):
        bt = pg.key.get_pressed()
        if bt[pg.K_SPACE] and self.on_ground:
            self.jump()
        elif bt[pg.K_d]:
            self.walk("right")
        elif bt[pg.K_a]:
            self.walk('left')
        elif bt[pg.K_w]:
            self.jerk()
        elif bt[pg.K_e]:
            self.attack()
        else:
            self.animation("base")




    def update(self, surface, ground_collisions):
        self.draw(surface)
        self.controls()
        self.apply_gravity(ground_collisions)


