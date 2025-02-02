import os
import sys
import random
import pygame


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


class continued(pygame.sprite.Sprite):
    image1 = load_image("needed1.png")
    image2 = load_image("needed2.png")
    now = False

    def __init__(self, group):
        super().__init__(group)
        self.image = continued.image1
        self.rect = self.image.get_rect()
        self.rect.x = 900
        self.rect.y = 100

    def update(self, *args):
        if not continued.now:
            if args[0] is True:
                self.image = continued.image2
                continued.now = True
                return ""
        if continued.now:
            if self.image == continued.image2 and args and args[
                0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
                return "yes"


class lvl1(pygame.sprite.Sprite):
    image = load_image("lvl1.png")

    def __init__(self, group):
        super().__init__(group)
        self.image = lvl1.image
        self.rect = self.image.get_rect()
        self.rect.x = 350
        self.rect.y = 400

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            return "yes"


class lvl2(pygame.sprite.Sprite):
    image = load_image("lvl2.png")

    def __init__(self, group):
        super().__init__(group)
        self.image = lvl2.image
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = 400

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            if args[1] is True:
                return "yes"
            return "no"


class lvl3(pygame.sprite.Sprite):
    image = load_image("lvl3.png")

    def __init__(self, group):
        super().__init__(group)
        self.image = lvl3.image
        self.rect = self.image.get_rect()
        self.rect.x = 650
        self.rect.y = 400

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            if args[1] is True:
                return "yes"
            return "no"


class table(pygame.sprite.Sprite):
    image = load_image("lvls_table.png")

    def __init__(self, group):
        super().__init__(group)
        self.image = table.image
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 100


class message(pygame.sprite.Sprite):
    image = load_image("warning.png")

    def __init__(self, group):
        super().__init__(group)
        self.image = message.image
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 600

    def update(self, *args):
        self.remove()
        self.rect.x = random.randrange(290, 310)
        self.rect.y = random.randrange(590, 610)

class word_loose(pygame.sprite.Sprite):
    image = load_image("loose.png")

    def __init__(self, group):
        super().__init__(group)
        self.image = word_loose.image
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 75

class retry(pygame.sprite.Sprite):
    image = load_image("retry.png")

    def __init__(self, group):
        super().__init__(group)
        self.image = retry.image
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = 400

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            return "yes"


class completed(pygame.sprite.Sprite):
    image = load_image("accept.png")

    def __init__(self, group, num):
        super().__init__(group)
        self.image = completed.image
        self.rect = self.image.get_rect()
        self.rect.x = 300 + 150 * (num - 1)
        self.rect.y = 300


class checky(pygame.sprite.Sprite):
    image = load_image("is_ready.png")

    def __init__(self, group):
        super().__init__(group)
        self.image = checky.image
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 600

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            return "yes"

class choosing_title(pygame.sprite.Sprite):
    image = load_image("choose_difficulty_title.png")

    def __init__(self, group):
        super().__init__(group)
        self.image = choosing_title.image
        self.rect = self.image.get_rect()
        self.rect.x = 250
        self.rect.y = 100


class easy(pygame.sprite.Sprite):
    image = load_image("easy_mode.png")

    def __init__(self, group):
        super().__init__(group)
        self.image = easy.image
        self.rect = self.image.get_rect()
        self.rect.x = 250
        self.rect.y = 400


class normal(pygame.sprite.Sprite):
    image = load_image("normal_mode.png")

    def __init__(self, group):
        super().__init__(group)
        self.image = normal.image
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 400


class hard(pygame.sprite.Sprite):
    image = load_image("hard_mode.png")

    def __init__(self, group):
        super().__init__(group)
        self.image = hard.image
        self.rect = self.image.get_rect()
        self.rect.x = 550
        self.rect.y = 400


class ultra_hard(pygame.sprite.Sprite):
    image = load_image("ultra_hard_mode.png")

    def __init__(self, group):
        super().__init__(group)
        self.image = ultra_hard.image
        self.rect = self.image.get_rect()
        self.rect.x = 700
        self.rect.y = 400


class rules(pygame.sprite.Sprite):
    image = load_image("rules.png")

    def __init__(self, group):
        super().__init__(group)
        self.image = rules.image
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 100


class to_rules(pygame.sprite.Sprite):
    image = load_image("rules_button.png")

    def __init__(self, group):
        super().__init__(group)
        self.image = to_rules.image
        self.rect = self.image.get_rect()
        self.rect.x = 1050
        self.rect.y = 20

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            return "yes"


class clicker_button(pygame.sprite.Sprite):
    image = load_image("clicker_button.png")

    def __init__(self, group):
        super().__init__(group)
        self.image = clicker_button.image
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 400

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            return "yes"


class miner_final(pygame.sprite.Sprite):
    image = load_image("chochitaesh.png")

    def __init__(self, group):
        super().__init__(group)
        self.image = miner_final.image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0


class bad_final(pygame.sprite.Sprite):
    image = load_image("ending1_picture.png")

    def __init__(self, group):
        super().__init__(group)
        self.image = bad_final.image
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 50


class mysterious_final(pygame.sprite.Sprite):
    image = load_image("ending2_picture.png")

    def __init__(self, group):
        super().__init__(group)
        self.image = mysterious_final.image
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 50


class secret_button(pygame.sprite.Sprite):
    image = load_image("secret_button.png")

    def __init__(self, group):
        super().__init__(group)
        self.image = secret_button.image
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 300

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            return "yes"