import pygame
import time
from creatures.BaseCharacter import BaseCharacter

# pygame.init()
# W, H = 1420, 800
# screen = pygame.display.set_mode((W, H))


class Player(BaseCharacter):

    def __init__(self, image_name, frame_count, x, y, width=50, height=100):
        super().__init__(image_name, frame_count, x, y, width, height)


        self.player_gravity = 0
        self.player_terminal_velocity = 10
        self.__last_direction = "right"
        self.jump_y = 0
        self.is_jumped = False

        self.__last__jerk_ticks = pygame.time.get_ticks()
        self.__last_increase_interval_ticks = 0
    def walk(self, direction):

        if direction == "right":
            self.x += 10
        elif direction == "left":
            self.x -= 10

        if self.__last_direction != direction:
            self.image = pygame.transform.flip(self.image, 1, 0)

        self.__last_direction = direction

    def jerk(self):

        jerk_value = 150

        if pygame.time.get_ticks() - self.__last__jerk_ticks >= 1300:
            if self.__last_direction == "right":
                self.x += jerk_value
            else:
                self.x -= jerk_value


            self.__last__jerk_ticks = pygame.time.get_ticks()
    def controls(self):
        bt = pygame.key.get_pressed()
        # if bt[pygame.K_SPACE]:
        #     self.jump()
        if bt[pygame.K_d]:
            self.walk("right")
        if bt[pygame.K_a]:
            self.walk('left')
        if bt[pygame.K_w]:
            self.jerk()
    def update(self):
        self.draw()
        self.controls()

        self.frame = (self.frame + 0.2) % self.frame_count




    # def player_move(self):
    #     keys = pygame.key.get_pressed()
    #
    #     if keys[pygame.K_w]:
    #         self.player_gravity = -10
    #
    # def apply_gravity(self, ground_collisions):
    #     if self.player_gravity < self.player_terminal_velocity:
    #         self.player_gravity += 1
    #     if ground_collisions:
    #         for ground in ground_collisions:
    #             if self.image_rect.bottom <= ground.mask.get_image_rect().left + 10:
    #                 self.image_rect.bottom = ground.mask.get_image_rect().top
    #                 self.player_gravity = 0
    #     self.image_rect.y += self.player_gravity
    #
    #
    #
    # def update(self, ground_collisions):
    #     self.player_move()
    #     self.apply_gravity(ground_collisions)
