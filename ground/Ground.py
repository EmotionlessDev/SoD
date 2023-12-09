import pygame


class Ground(pygame.sprite.Sprite):

    def __init__(self, img, x, y):
        super().__init__()
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect(topleft=(x, y))
