import pygame


class Skeleton(pygame.sprite.Sprite):

    def __init__(self, img, x, y):
        super().__init__()
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect(midbottom=(x, y))
        self.speed = 0
