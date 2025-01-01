import os
import sys
from tokenize import group
import random

import pygame


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    return image


class logo(pygame.sprite.Sprite):
    image = load_image("main_logo.png")

    def __init__(self, group):
        super().__init__(group)
        self.image = logo.image
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 100

    def update(self, *args):
        self.remove()
        self.rect.x = random.randrange(290, 310)
        self.rect.y = random.randrange(90, 110)

class play(pygame.sprite.Sprite):
    image = load_image("play_button.png")

    def __init__(self, group):
        super().__init__(group)
        self.image = play.image
        self.rect = self.image.get_rect()
        self.rect.x = 450
        self.rect.y = 450

    def update(self, *args):
        pass

class info(pygame.sprite.Sprite):
    image = load_image("add_info_button.png")

    def __init__(self, group):
        super().__init__(group)
        self.image = info.image
        self.rect = self.image.get_rect()
        self.rect.x = 450
        self.rect.y = 625

    def update(self, *args):
        pass
