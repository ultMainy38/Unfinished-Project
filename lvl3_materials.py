import pygame
import os
import sys

def load_image(name):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class character(pygame.sprite.Sprite):
    image = load_image("character.png")

    def __init__(self, group):
        super().__init__(group)
        self.image = character.image
        self.rect = pygame.Rect(322, 300, 52, 97)
        self.rect.x = 300
        self.rect.y = 300

def create_bullet(x, y):
    main_rect = pygame.Rect(x - 5, y - 5, 5, 5)
    bullet_pos = (x - 5, y - 5, 5)
    return (main_rect, bullet_pos)

def changing_poses(bullets, bullet_rects, circles):
    for bullet in bullets:
        if bullet != "":
            x = bullet[0]
            y = bullet[1]
            side = bullet[2]

            ind = bullets.index(bullet)

            if circles[ind] != "":
                xc = circles[ind][0]
                yc = circles[ind][1]

                if x > xc:
                    x -= 25
                elif x < xc:
                    x += 25

                if y > yc:
                    y -= 25
                elif y < yc:
                    y += 25

                bullets[ind] = (x - side, y - side, side)
                bullet_rects[ind] = pygame.Rect(x - side, y - side, side, side)

            else:
                bullets[ind] = ""
                bullet_rects = ""
