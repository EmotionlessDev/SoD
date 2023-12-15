import pygame
import random
from math import sqrt


class Skeleton(pygame.sprite.Sprite):

    def __init__(self, sprites_idle, sprites_attack, sprites_move, x, y, target):
        super().__init__()
        self.enemy_idle = sprites_idle
        self.enemy_attack = sprites_attack
        self.enemy_move = sprites_move
        self.idle_flag = True
        self.attack_flag = False
        self.move_flag = False
        self.enemy_idle_index = 0
        self.enemy_attack_index = 0
        self.enemy_move_index = 0
        self.image = self.enemy_idle[self.enemy_idle_index]
        self.rect = self.image.get_rect(midbottom=(x, y))
        self.speed = 0
        self.damage = 1
        self.move = 0
        self.walking = None  # True - Right, False - Left, None - not walking
        self.move_delay = 0
        self.enemy_attack_radius = 10
        self.enemy_visibility_radius = 300
        self.target = target

    def movement(self):
        if self.move == 0 and self.move_delay == 0:
            self.move = random.randint(40, 100)
            self.move *= random.choice((-1, 1))
            self.move_delay = random.randint(180, 270)
            self.move_flag = False
        else:
            if self.move_delay > 0:
                self.move_delay -= 1
            elif self.move < 0:
                self.move_flag = True
                self.move += 1
                self.speed += 0.5
                self.rect.x += int(self.speed)
                if int(self.speed) == 1:
                    self.speed = 0
            elif self.move > 0:
                self.move_flag = True
                self.move -= 1
                self.speed += 0.5
                self.rect.x -= int(self.speed)
                if int(self.speed) == 1:
                    self.speed = 0

    def move_to(self, target: tuple):
        pos_x = target[0]
        pos_y = target[1]
        if self.move_delay > 0:
            self.move_delay -= 1
            self.animate_idle()
        elif self.rect.x < pos_x:
            self.speed += 0.5
            self.walking = True
            self.rect.x += int(self.speed)
            if int(self.speed) == 1:
                self.speed = 0
        elif self.rect.x > pos_x:
            self.speed += 0.5
            self.walking = False
            self.rect.x -= int(self.speed)
            if int(self.speed) == 1:
                self.speed = 0
        elif self.rect.x == pos_x:
            self.walking = None

    def in_visibility_radius(self):
        pos_x = self.rect.x
        pos_y = self.rect.y
        pos_target_x = self.target.sprite.rect.x
        pos_target_y = self.target.sprite.rect.y
        if (
            sqrt((pos_target_x - pos_x) ** 2 + (pos_target_y - pos_y) ** 2)
            < self.enemy_visibility_radius
        ):
            return True
        else:
            return False

    def dist_to_target(self):
        pos_x = self.rect.x
        pos_y = self.rect.y
        pos_target_x = self.target.sprite.rect.x
        pos_target_y = self.target.sprite.rect.y
        return sqrt((pos_target_x - pos_x) ** 2 + (pos_target_y - pos_y) ** 2)

    def attack(self):
        pass

    def animate_idle(self):
        self.enemy_idle_index += 0.1
        if self.enemy_idle_index < len(self.enemy_idle):
            self.image = self.enemy_idle[int(self.enemy_idle_index)]
        else:
            self.enemy_idle_index = 0

    def animate_move(self):
        self.enemy_move_index += 0.1
        if self.enemy_move_index < len(self.enemy_move):
            self.image = self.enemy_move[int(self.enemy_move_index)]
            if not self.walking:
                self.image = pygame.transform.flip(self.image, True, False)
        else:
            self.enemy_move_index = 0

    def animate_attack(self):
        self.enemy_attack_index += 0.1
        if self.enemy_attack_index < len(self.enemy_attack):
            self.image = self.enemy_attack[int(self.enemy_attack_index)]
        else:
            self.enemy_attack_index = 0

    def update(self):
        # if target in radius
        if self.in_visibility_radius():
            if self.dist_to_target() > 0:
                self.animate_move()
                self.move_to((self.target.sprite.rect.x, self.target.sprite.rect.y))
            else:
                self.animate_idle()
        else:
            pass
