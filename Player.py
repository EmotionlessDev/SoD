import pygame as pg
from BaseCharacter import BaseCharacter
pg.init()


class Player(BaseCharacter):

    def __init__(self, image_name, frame_count, x, y, width, height, scroll):
        super().__init__(image_name, frame_count, x, y, width, height)
        self.player_gravity = 0
        self.player_terminal_velocity = 10
        self.__last_direction = "right"
        self.jump_y = 0
        self.is_jumped = False
        self.scroll = 0

        self.__last__jerk_ticks = pg.time.get_ticks()
        self.__last_increase_interval_ticks = 0

    def walk(self, direction):

        if direction == "right":
            self.scroll = -10
        elif direction == "left":
            self.scroll = 10

        if self.__last_direction != direction:
            self.image = pg.transform.flip(self.image, True, False)

        self.__last_direction = direction

    def jerk(self):
        jerk_value = 150

        if pg.time.get_ticks() - self.__last__jerk_ticks >= 1300:
            if self.__last_direction == "right":
                self.scroll = -jerk_value
            else:
                self.scroll = jerk_value

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

    def controls(self):
        bt = pg.key.get_pressed()
        if bt[pg.K_SPACE] and self.on_ground:
            self.y += -50 + 0.5
        if bt[pg.K_d]:
            self.walk("right")
        if bt[pg.K_a]:
            self.walk('left')
        if bt[pg.K_w]:
            self.jerk()

        if not (bt[pg.K_d] or bt[pg.K_a] or bt[pg.K_w]):
            self.scroll = 0

    def update(self, surface, ground_collisions):
        self.draw(surface)
        self.controls()
        self.apply_gravity(ground_collisions)

        self.frame = (self.frame + 0.2) % self.frame_count
