import pygame as pg
import Constants
pg.init()


class Player(pg.sprite.Sprite):
    def __init__(self, x, y, width, height, hp=100, damage=10):
        pg.sprite.Sprite.__init__(self)
        self.hp = hp
        self.start_hp = hp
        self.damage = damage
        self.x = x
        self.y = y
        self.dx = x
        self.dy = y
        self.scroll = 0
        self.cur_animation = "base"
        self.float_frame = 0
        self.cur_frame = 0
        self.rect = pg.Rect(x, y, width, height)
        self.last_direction = 'right'
        self.direction = "right"
        self.direction_vector = pg.math.Vector2(0, 0)
        self.animations = {"base": [], 'attack': []}
        self.settings_frame = {"base": (14, 0.2), 'attack': (10, 0.3)}  # frames count / speed
        self.is_attacking = False
        self.surface = ''
        self.w_base = pg.image.load(r"characters/Player/base/hero_base_1.png").convert_alpha().get_width()
        self.h_base = pg.image.load(r"characters/Player/base/hero_base_1.png").convert_alpha().get_height()
        for animation_name, value in self.animations.items():

            for i in range(1, self.settings_frame[animation_name][0] + 1):
                img = pg.image.load(r"characters/Player/" + animation_name + "/hero_" + animation_name + "_" + str(
                    i) + ".png").convert_alpha()

                delta_w = (self.w_base - img.get_width()) * 1
                delta_h = (self.h_base - img.get_height()) * 0.5
                img = pg.transform.scale(img, (width + delta_w, height + delta_h))
                self.animations[animation_name].append(img)

        self.image = self.animations[self.cur_animation][self.cur_frame]

        self.jump_y = 0
        self.in_castle = False

        self.__last__jerk_ticks = pg.time.get_ticks()
        self.__last_attack_ticks = 0

        self.jerk_value = 105
        self.jump_value = 25
        self.blocks_group = []
        self.direction = pg.math.Vector2(0, 0)
        self.buffer_collision = 25
        self.on_ground = False
        self.hp = hp

    #### DRAW HP BAR FUNCTION START ####
    def draw_hp_bar(self, screen):
        cur_hp = (self.hp * 100) / self.start_hp
        bar_x = self.rect.midbottom[0]
        bar_y = self.rect.midbottom[1] + 10
        bar_cur = pg.Rect((bar_x - 25, bar_y), (50 * cur_hp / 100, 8))
        pg.draw.rect(screen, pg.Color(255, 46, 0), bar_cur)
        pg.draw.rect(screen, pg.Color(255, 254, 203), bar_cur, 2)
    #### DRAW HP BAR FUNCTION END ####

    def walk(self, direction):
        self.direction = direction
        if self.direction == "right":
            self.direction_vector.x = 0
            self.direction_vector.x += 7
        elif self.direction == "left":
            self.direction_vector.x = 0
            self.direction_vector.x -= 7
        else:
            self.direction_vector.x = 0
        self.last_direction = self.direction

    def attack(self):

        if pg.time.get_ticks() - self.__last_attack_ticks > 100:
            self.animation("attack")

            if self.last_direction == 'left':
                rect_attack = pg.Rect(self.rect.x - 100, self.rect.y, self.rect.width + 100, self.rect.height)
            if self.last_direction == 'right':
                rect_attack = pg.Rect(self.rect.x, self.rect.y, self.rect.width + 100, self.rect.height)

            pg.draw.rect( self.surface, "yellow", rect_attack, 2)
            if rect_attack.collidelist(Constants.enemies_group.sprites()) != -1 :
                for enemy in Constants.enemies_group:
                    if enemy.rect.colliderect(rect_attack):
                        enemy.hp -= self.damage
                        if enemy.hp <= 0:
                            enemy.kill()
        self.__last_attack_ticks = pg.time.get_ticks()

    def horizontal_movement_collision(self, blocks_group):

        for block in blocks_group:
            # relative block right
            point_right_top = (block.rect.x + block.rect.width + self.buffer_collision - self.scroll, block.rect.y + 20)
            point_right_center = (block.rect.x + block.rect.width + self.buffer_collision - self.scroll,
                                  block.rect.y + block.rect.height // 2)
            point_right_bottom = (block.rect.x + block.rect.width + self.buffer_collision - self.scroll,
                                  block.rect.y + block.rect.height - 20)

            if (self.rect.collidepoint(point_right_top) or self.rect.collidepoint(
                    point_right_center) or self.rect.collidepoint(point_right_bottom)) and self.direction == 'left':
                self.direction_vector.x = 0
            # relative block left
            point_left_top = (block.rect.x - self.buffer_collision - self.scroll, block.rect.y + 20)
            point_left_center = (
            block.rect.x - self.buffer_collision - self.scroll, block.rect.y + block.rect.height // 2)
            point_left_bottom = (
            block.rect.x - self.buffer_collision - self.scroll, block.rect.y + block.rect.height - 20)

            if (self.rect.collidepoint(point_left_top) or self.rect.collidepoint(
                    point_left_center) or self.rect.collidepoint(point_left_bottom)) and self.direction == 'right':
                self.direction_vector.x = 0

    def vertical_movement_collision(self, blocks_group):

        for block in blocks_group:
            overflow_rect_on_block = block.rect
            if self.rect.colliderect(overflow_rect_on_block):
                self.direction_vector.y = 0

    def apply_gravity(self):
        if self.on_ground == False:
            self.direction_vector.y += 1.1
            # self.rect.y += self.direction_vector.y
        else:

            self.direction_vector.y = 0

    def jump(self):

        self.direction_vector.y += -13

    def jerk(self):
        if pg.time.get_ticks() - self.__last__jerk_ticks >= 1300:
            self.buffer_collision = 75
            if self.last_direction == "right":
                for i in range(self.jerk_value):
                    self.direction_vector.x += 1
                    self.horizontal_movement_collision(self.blocks_group)

                self.buffer_collision = 5

            else:
                for i in range(self.jerk_value):
                    self.direction_vector.x -= 1
                    self.horizontal_movement_collision(self.blocks_group)

                self.buffer_collision = 5

            self.__last__jerk_ticks = pg.time.get_ticks()

    def controls(self):
        bt = pg.key.get_pressed()
        if bt[pg.K_SPACE] and self.direction_vector.y == 0:
            self.jump()
        if bt[pg.K_d]:
            self.walk("right")
        elif bt[pg.K_a]:
            self.walk('left')
        else:
            self.direction_vector.x = 0
        if bt[pg.K_w]:
            self.jerk()

        keys = pg.mouse.get_pressed()
        if keys[0]:
            self.attack()
        if not (bt[pg.K_d] or bt[pg.K_a] or bt[pg.K_w]):
            self.scroll = 0

    def draw(self, surface):
        self.rect = self.image.get_rect(bottomleft=(self.x, self.dy))
        surface.blit(self.image, self.rect)

        pg.draw.rect(surface, (255, 255, 255),
                     self.rect, 2)

    def animation(self, animation_name="base"):
        if self.cur_animation == 'attack':
            if self.cur_frame == self.settings_frame['attack'][0] - 1:
                self.cur_animation = 'base'

        else:
            self.cur_animation = 'base'
            self.cur_animation = animation_name

        frame_count = self.settings_frame[self.cur_animation][0]
        if self.cur_animation == 'attack':

            self.float_frame = (self.float_frame + self.settings_frame[self.cur_animation][1]) % frame_count + 0.1

        elif self.cur_animation == 'base':
            self.float_frame = (self.float_frame + self.settings_frame[self.cur_animation][1]) % frame_count
        self.cur_frame = int(self.float_frame)
        self.image = self.animations[self.cur_animation][self.cur_frame]

        if self.direction == 'left':
            self.image = pg.transform.flip(self.image, True, False)

    def script_playing(self, script_collisions):
        if script_collisions:
            for script in script_collisions:
                script.command(*script.args)

    def update(self, surface, blocks_group, script_collisions):
        self.surface = surface
        self.draw_hp_bar(surface)
        self.animation("base")
        self.apply_gravity()
        self.blocks_group = blocks_group

        self.script_playing(script_collisions)
        # не менять порядок снизу!
        self.vertical_movement_collision(blocks_group)
        self.controls()

        self.scroll = -self.direction_vector.x

        self.horizontal_movement_collision(blocks_group)
        self.dx += self.direction_vector.x
        self.dy += self.direction_vector.y

        # self.rect.x += self.dx
        # self.rect.y += self.dy

        self.scroll = -self.direction_vector.x
        self.draw(surface)
