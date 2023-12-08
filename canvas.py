import pygame as pg
import os


def load_image(name):  # возвращает картинку как Surface
    fullname = os.path.join(name)
    return pg.image.load(fullname).convert()
