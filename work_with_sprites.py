import os
import sys
from tokenize import group
import random
import pygame
import time


def load_image(name):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
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
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            return "yes"


class info(pygame.sprite.Sprite):
    image = load_image("add_info_button.png")

    def __init__(self, group):
        super().__init__(group)
        self.image = info.image
        self.rect = self.image.get_rect()
        self.rect.x = 450
        self.rect.y = 625

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            return "yes"


class author(pygame.sprite.Sprite):
    image = load_image("author.png")

    def __init__(self, group):
        super().__init__(group)
        self.image = author.image
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 100

    def update(self, *args):
        pass


class back(pygame.sprite.Sprite):
    image = load_image("back.png")

    def __init__(self, group):
        super().__init__(group)
        self.image = back.image
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = 600

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            return "yes"


class room(pygame.sprite.Sprite):
    image = load_image("room.png")

    def __init__(self, group):
        super().__init__(group)
        self.image = room.image
        self.rect = self.image.get_rect()
        self.rect.x = 150
        self.rect.y = 0


class words(pygame.sprite.Sprite):
    image1 = load_image("dialogue1.png")
    image2 = load_image("dialogue2.png")

    def __init__(self, group):
        super().__init__(group)
        self.image = words.image1
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 500

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN:
            if self.image == words.image1:
                self.image = words.image2
