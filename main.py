import sys

import pygame
import random
from work_with_sprites import load_image, logo, play, info, author, back, room, words, continued, lvl1, lvl2, lvl3, \
    table, message
import time

if __name__ == "__main__":
    pygame.init()
    size = width, height = 1200, 800
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Unfinished Project: меню")

    menu_sprites = pygame.sprite.Group()
    logot = logo(menu_sprites)
    play_button = play(menu_sprites)
    info_button = info(menu_sprites)

    info_sprites = pygame.sprite.Group()
    word = author(info_sprites)
    back_button = back(info_sprites)

    scene_sprites = pygame.sprite.Group()
    rooms = room(scene_sprites)
    dialogue = words(scene_sprites)
    continue_button = continued(scene_sprites)

    lvls_sprites = pygame.sprite.Group()
    button1 = lvl1(lvls_sprites)
    button2 = lvl2(lvls_sprites)
    button3 = lvl3(lvls_sprites)
    name_of_stage = table(lvls_sprites)
    already_checked1 = False
    already_checked2 = False

    state = 0
    states = ["menu", "lobby", "scene", "lvl1", "lvl2", "lvl3", "abt_info", "final", "lvls", "pause"]
    lvl1_completed = False
    lvl2_completed = False
    lvl3_completed = False

    running = True
    lvl1_running = False
    lvl2_running = False
    lvl3_running = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("BLACK")
        if states[state] == "menu":
            menu_sprites.update()
            if info_button.update(event) == "yes":
                state = 6
            elif play_button.update(event) == "yes":
                state = 2
            menu_sprites.draw(screen)
            time.sleep(0.05)

        elif states[state] == "abt_info":
            info_sprites.update()
            if back_button.update(event) == "yes":
                state = 0
            info_sprites.draw(screen)

        elif states[state] == "scene":
            scene_sprites.update(event)
            if dialogue.image == words.image2:
                if not continued.now:
                    continue_button.update(True)
            if continue_button.update(event) == "yes":
                state = -2
            scene_sprites.draw(screen)

        elif states[state] == "lvls":
            if button1.update(event) == "yes":
                state = 3
                lvl1_running = True
                running = False

            if button2.update(event, lvl1_completed) == "yes":
                lvl2_running = True
                running = False
            elif button2.update(event, lvl1_completed) == "no":
                if not already_checked1 and not already_checked2:
                    warning = message(lvls_sprites)
                    already_checked1, already_checked2 = True, True

            if button3.update(event, lvl2_completed) == "yes":
                state = 5
                lvl3_running = True
                running = False

            elif button3.update(event, lvl2_completed) == "no":
                if not already_checked1 and not already_checked2:
                    warning = message(lvls_sprites)
                    already_checked1, already_checked2 = True, True

            lvls_sprites.update()
            lvls_sprites.draw(screen)
            time.sleep(0.05)

        elif states[state] == "lvl1":
            lvl1_completed = "now"

        pygame.display.flip()

    replacing = False
    x, y = 0, 0
    dx, dy = 0, 0
    circle = [600, 500, 20]
    pad = [500, 600, 150, 30]

    pygame.quit()
    pygame.init()
    size = width, height = 1200, 800
    screen2 = pygame.display.set_mode(size)
    pygame.draw.rect(screen2, "WHITE", pad)
    pygame.draw.circle(screen2, "WHITE", circle[:2], circle[2])

    brick1 = pygame.Rect(0, 0, 100, 50)
    brick2 = pygame.Rect(100, 0, 100, 50)
    brick3 = pygame.Rect(200, 0, 100, 50)
    brick4 = pygame.Rect(300, 0, 100, 50)
    brick5 = pygame.Rect(400, 0, 100, 50)
    brick6 = pygame.Rect(500, 0, 100, 50)
    brick7 = pygame.Rect(600, 0, 100, 50)
    brick8 = pygame.Rect(700, 0, 100, 50)
    brick9 = pygame.Rect(800, 0, 100, 50)
    brick10 = pygame.Rect(900, 0, 100, 50)
    brick11 = pygame.Rect(1000, 0, 100, 50)
    brick12 = pygame.Rect(1100, 0, 100, 50)
    brick13 = pygame.Rect(0, 50, 100, 50)
    brick14 = pygame.Rect(100, 50, 100, 50)
    brick15 = pygame.Rect(200, 50, 100, 50)
    brick16 = pygame.Rect(300, 50, 100, 50)
    brick17 = pygame.Rect(400, 50, 100, 50)
    brick18 = pygame.Rect(500, 50, 100, 50)
    brick19 = pygame.Rect(600, 50, 100, 50)
    brick20 = pygame.Rect(700, 50, 100, 50)
    brick21 = pygame.Rect(800, 50, 100, 50)
    brick22 = pygame.Rect(900, 50, 100, 50)
    brick23 = pygame.Rect(1000, 50, 100, 50)
    brick24 = pygame.Rect(1100, 50, 100, 50)

    full_bricks = [brick1, brick2, brick3, brick4, brick5, brick6, brick7, brick8, brick9, brick10, brick11, brick12,
                   brick13, brick14, brick15, brick16, brick17, brick18, brick19, brick20, brick21, brick22, brick23,
                   brick24]

    for brick in full_bricks:
        pygame.draw.rect(screen2, "WHITE", brick, 7)

    pygame.display.flip()

    main_rect = pygame.Rect(pad)
    main_circle = pygame.Rect(580, 480, 40, 40)

    circle_run = [".", "."]
    start = False

    clock = pygame.time.Clock()
    FPS = 240

    aim = 24
    now = 0

    while lvl1_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                lvl1_running = False
            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                if replacing:
                    screen2.fill((0, 0, 0))
                    pad = [x - dx, y - dy, 150, 30]
                    pygame.draw.rect(screen2, "WHITE", pad)
                    main_rect = pygame.Rect(pad)
                    if not start:
                        circle_run = ["-", "-"]
                        start = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pad[0] <= x <= pad[0] + 150 and pad[1] <= y <= pad[1] + 30:
                    replacing = True
                    dx = x - pad[0]
                    dy = y - pad[1]

        if main_rect.colliderect(main_circle):
            pygame.quit()
            sys.exit()

        for brick in full_bricks:
            if brick.colliderect(main_circle):
                full_bricks.remove(brick)
                now += 1
                if circle_run == ["+", "-"]:
                    circle_run = ["+", "+"]
                elif circle_run == ["+", "+"]:
                    circle_run = ["+", "-"]
                elif circle_run == ["-", "+"]:
                    circle_run = ["+", "+"]
                elif circle_run == ["-", "-"]:
                    circle_run = ["-", "+"]

        if circle[0] == 1190:
            circle_run[0] = "-"
        elif circle[0] == 10:
            circle_run[1] = "+"

        if circle[1] == 790:
            circle[1] = "-"
        elif circle[1] == 10:
            circle[1] = "+"

        if circle_run[0] == "+":
            circle[0] += 3
        elif circle_run[0] == "-":
            circle[0] -= 3

        if circle_run[1] == "+":
            circle[1] += 3
        elif circle_run[1] == "-":
            circle[1] -= 3

        main_circle = pygame.Rect(circle[0] - circle[2], circle[1] - circle[2], circle[2] * 2, circle[2] * 2)

        pygame.draw.rect(screen2, "WHITE", pad)
        pygame.draw.circle(screen2, "WHITE", (circle[0], circle[1]), circle[2])

        for brick in full_bricks:
            pygame.draw.rect(screen2, "WHITE", brick, 7)


        pygame.display.flip()
        clock.tick(FPS)
