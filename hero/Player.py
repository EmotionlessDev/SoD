import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self, img, x, y):
        super().__init__()
        player_walk = pygame.image.load(img).convert_alpha()
        self.image = player_walk
        self.rect = player_walk.get_rect(midbottom=(30, y))
        self.player_gravity = 0
        self.player_speed = 5
        self.player_damage = 0
        self.player_terminal_velocity = 10

    def player_move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.rect.x += self.player_speed
        if keys[pygame.K_a]:
            self.rect.x -= self.player_speed
        if keys[pygame.K_w]:
            self.player_gravity = -10

    def apply_gravity(self, ground_collisions):
        if self.player_gravity < self.player_terminal_velocity:
            self.player_gravity += 1
        if ground_collisions:
            for ground in ground_collisions:
                if self.rect.bottom <= ground.rect.top + 10:
                    self.rect.bottom = ground.rect.top
                    self.player_gravity = 0
        self.rect.y += self.player_gravity

    def update(self, ground_collisions):
        self.player_move()
        self.apply_gravity(ground_collisions)
