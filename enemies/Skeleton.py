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
        self.gravity = 10
        self.walking = None  # True - Right, False - Left, None - not walking
        self.move_delay = 0
        self.enemy_attack_radius = 39
        self.enemy_visibility_radius = 350
        self.target = target
        self.action_type = None
        self.idle_timer = 0
        self.target_to_move = (None, None)

    #### ON GROUND FUNCTION START ####
    # This function checks if the mob is on the ground
    # x: tuple (coords)
    # delta: int (mob step (speed actually))
    # blocks_group: list (list of all ground blocks in game)
    def on_ground(self, x: tuple, delta: int, blocks_group: list):
        rect_check = pygame.Rect(x[0] + int(delta), x[1], 1, 2)
        for ground in blocks_group:
            if rect_check.colliderect(ground.rect):
                return True
        return False

    #### ON GROUND FUNCTION END ####

    #### MOVE TO TARGET FUNCTION START ####
    # target: tuple (coords of target)
    # blocks_group: list (list of all ground blocks in game)
    # need fixes
    def move_to(self, target: tuple, blocks_group: list):
        pos_x = target[0]
        pos_y = target[1]
        if self.move_delay > 0:
            self.move_delay -= 1
            self.animate_idle()
        elif self.rect.x < pos_x:
            self.speed += 0.5
            self.walking = True
            if self.on_ground(self.rect.bottomright, int(self.speed), blocks_group):
                self.animate_move()
                self.rect.x += int(self.speed)
            else:
                self.walking = None
                self.animate_idle()
            if int(self.speed) == 1:
                self.speed = 0
        elif self.rect.x > pos_x:
            self.speed += 0.5
            self.walking = False
            if self.on_ground(self.rect.bottomleft, int(self.speed), blocks_group):
                self.animate_move()
                self.rect.x -= int(self.speed)
            else:
                self.walking = None
                self.animate_idle()
            if int(self.speed) == 1:
                self.speed = 0
        elif self.rect.x == pos_x:
            self.walking = None

    #### MOTE TO TARGET FUNCTION END ####

    #### IN RADIUS FUNCTIONS START ####
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

    # need fixes idk
    def in_attack_radius(self):
        pos_x = self.rect.centerx
        pos_y = self.rect.bottom
        pos_target_x = self.target.sprite.rect.centerx
        pos_target_y = self.target.sprite.rect.bottom
        if (
            abs(pos_x - pos_target_x) < self.enemy_attack_radius
            and abs(pos_y - pos_target_y) < self.rect.height
        ):
            return True
        else:
            return False

    #### IN RADIUS FUNCTIONS END ####

    #### DIST FUNCTIONS START ####
    def dist_to_target(self):
        pos_x = self.rect.x
        pos_y = self.rect.y
        pos_target_x = self.target.sprite.rect.x
        pos_target_y = self.target.sprite.rect.y
        return sqrt((pos_target_x - pos_x) ** 2 + (pos_target_y - pos_y) ** 2)

    def dist_to_target_x(self):
        pos_x = self.rect.x
        pos_target_x = self.target.sprite.rect.x
        return abs(pos_target_x - pos_x)

    def dist_to_target_y(self):
        pos_y = self.rect.y
        pos_target_y = self.target.sprite.rect.y
        return abs(pos_target_y - pos_y)

    #### DIST FUNCTIONS END ####
    def attack(self):
        pass

    #### FUNCTIONS FOR ANIMATIONS START ####
    def animate_idle(self):
        self.enemy_idle_index += 0.1
        if self.enemy_idle_index < len(self.enemy_idle):
            self.image = self.enemy_idle[int(self.enemy_idle_index)]
            if not self.walking:
                self.image = pygame.transform.flip(self.image, True, False)
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
            if not self.walking:
                self.image = pygame.transform.flip(self.image, True, False)
        else:
            self.enemy_attack_index = 0

    #### FUNCTIONS FOR ANIMATIONS END ####
    # ground_collisions: dict ()
    def apply_gravity(self, ground_collisions: dict):
        if self in ground_collisions:
            for ground in ground_collisions[self]:
                if self.rect.bottom >= ground.rect.top:
                    self.rect.bottom = ground.rect.top + 1
                    self.gravity = 0
        else:
            self.gravity = 10
        self.rect.y += self.gravity

    ##### LOGIC FUNCTIONS BEGIN #####
    # blocks_group: list (list of all ground blocks in game)
    def logic_in_visibility_radius(self, blocks_group: list):
        if self.dist_to_target_x() > 0:
            self.move_to(
                (self.target.sprite.rect.x, self.target.sprite.rect.y), blocks_group
            )
        else:
            self.animate_idle()

    def logic_attack(self):
        self.animate_attack()
        self.attack()

    # blocks_group: list (list of all ground blocks in game)
    def logic_idle(self, blocks_group: list):
        if self.action_type == None:
            self.action_type = random.choice(["idle", "move"])
            if self.action_type == "idle":
                self.idle_timer = random.randint(20, 50)
            if self.action_type == "move":
                self.target_to_move = (
                    random.randint(self.rect.x - 30, self.rect.x + 40),
                    random.randint(self.rect.y - 100, self.rect.y + 100),
                )
        if self.action_type == "idle":
            if self.idle_timer != 0:
                self.animate_idle()
                self.idle_timer -= 1
            else:
                self.animate_idle()
                self.action_type = None
        if self.action_type == "move":
            self.animate_move()
            self.move_to(self.target_to_move, blocks_group)
            if self.walking == None:
                self.action_type = None

    #### LOGIC FUNCTIONS END ####

    #### SCROLL FUNCTION START ####
    def scroll(self):
        self.rect.move_ip(self.target.sprite.scroll, 0)

    #### SCROLL FUNCTION END ####

    #### UPDATE BEGIN ####
    # ground_collisions: dict with collisions
    # blocks_group: list (list of all ground blocks in game)
    def update(self, ground_collisions: dict, blocks_group: list):
        # secondary calls
        self.apply_gravity(ground_collisions)
        self.scroll()
        # if target in attack radius
        if self.in_attack_radius():
            self.logic_attack()
        # if target in visibility radius
        elif self.in_visibility_radius():
            self.logic_in_visibility_radius(blocks_group)
        # if idle do random things
        else:
            self.logic_idle(blocks_group)

    #### UPDATE END ####
