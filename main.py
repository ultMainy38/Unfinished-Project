import sys
import pygame
import random
from work_with_sprites import load_image, logo, play, info, author, back, room, words, continued, lvl1, lvl2, lvl3, \
    table, message, word_loose, retry, completed
from lvl1_materials import changing_marks, moving_circle, bricks, change_direction
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
    circle2 = [600, 500, 20]
    circle3 = [600, 500, 20]
    pad = [500, 600, 150, 30]

    pygame.quit()
    pygame.init()
    size = width, height = 1200, 800
    screen2 = pygame.display.set_mode(size)
    pygame.draw.rect(screen2, "WHITE", pad)
    pygame.draw.circle(screen2, "WHITE", circle[:2], circle[2])

    full_bricks = bricks()

    for brick in full_bricks:
        pygame.draw.rect(screen2, "WHITE", brick, 7)

    pygame.display.flip()

    main_rect = pygame.Rect(pad)
    main_circle = pygame.Rect(580, 480, 40, 40)
    main_circle2 = pygame.Rect(0, 0, 40, 40)
    main_circle3 = pygame.Rect(0, 0, 40, 40)

    circle_run = [".", "."]
    circle_run2 = [".", "."]
    circle_run3 = [".", "."]
    start = False

    clock = pygame.time.Clock()
    FPS = 240

    aim = 24
    now = 0
    win = ""

    pause_sprites = pygame.sprite.Group()
    uhoh = word_loose(pause_sprites)
    retry_button = retry(pause_sprites)

    lvl_selecting = False

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
                        circle_run = ["+", "-"]
                        start = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pad[0] <= x <= pad[0] + 150 and pad[1] <= y <= pad[1] + 30:
                    replacing = True
                    dx = x - pad[0]
                    dy = y - pad[1]

        if win == "":
            if main_rect.colliderect(main_circle) or main_rect.colliderect(main_circle2) or main_rect.colliderect(
                    main_circle3):
                win = False

            if now == 8:
                circle_run2 = ["+", "-"]
            if now == 16:
                circle_run3 = ["-", "-"]

            for brick in full_bricks:
                if brick.colliderect(main_circle):
                    full_bricks.remove(brick)
                    now += 1
                    circle_run = changing_marks(circle_run)
                if now >= 8:
                    if brick.colliderect(main_circle2):
                        full_bricks.remove(brick)
                        now += 1
                        circle_run2 = changing_marks(circle_run2)
                if now >= 16:
                    if brick.colliderect(main_circle3):
                        full_bricks.remove(brick)
                        now += 1
                        circle_run3 = changing_marks(circle_run3)

            screen2.fill((0, 0, 0))

            if start:
                moving_circle(circle, circle_run)
                change_direction(circle, circle_run)

            if now >= 8:
                moving_circle(circle2, circle_run2)
                change_direction(circle2, circle_run2)
                if now >= 16:
                    moving_circle(circle3, circle_run3)
                    change_direction(circle3, circle_run3)

            main_circle = pygame.Rect(circle[0] - circle[2], circle[1] - circle[2], circle[2] * 2, circle[2] * 2)
            if now >= 8:
                main_circle2 = pygame.Rect(circle2[0] - circle2[2], circle2[1] - circle2[2], circle2[2] * 2,
                                           circle2[2] * 2)
                if now >= 16:
                    main_circle3 = pygame.Rect(circle3[0] - circle3[2], circle3[1] - circle3[2], circle3[2] * 2,
                                               circle3[2] * 2)

            pygame.draw.rect(screen2, "WHITE", pad)
            pygame.draw.circle(screen2, "WHITE", (circle[0], circle[1]), circle[2])
            if now >= 8:
                pygame.draw.circle(screen2, "WHITE", (circle2[0], circle2[1]), circle2[2])
                if now >= 16:
                    pygame.draw.circle(screen2, "WHITE", (circle3[0], circle3[1]), circle3[2])

            for brick in full_bricks:
                pygame.draw.rect(screen2, "WHITE", brick, 7)

            if now == 24:
                lvl1_completed = True
                win = True
                lvl1_running = False
                lvl_selecting = True

        elif not win:
            replacing = False
            screen2.fill((0, 0, 0))
            pause_sprites.update()
            if retry_button.update(event) == "yes":
                win = ""

                main_rect = pygame.Rect(pad)
                main_circle = pygame.Rect(580, 480, 40, 40)
                main_circle2 = pygame.Rect(0, 0, 40, 40)
                main_circle3 = pygame.Rect(0, 0, 40, 40)

                circle_run = [".", "."]
                circle_run2 = [".", "."]
                circle_run3 = [".", "."]
                start = False

                replacing = False
                x, y = 0, 0
                dx, dy = 0, 0
                circle = [600, 500, 20]
                circle2 = [600, 500, 20]
                circle3 = [600, 500, 20]
                pad = [500, 600, 150, 30]

                full_bricks = bricks()
                now = 0
            pause_sprites.draw(screen2)

        pygame.display.flip()
        clock.tick(FPS)

pygame.quit()
pygame.init()
clock = pygame.time.Clock()

size = width, height = 1200, 800
screen3 = pygame.display.set_mode(size)

lvls_sprites = pygame.sprite.Group()
button1 = lvl1(lvls_sprites)
button2 = lvl2(lvls_sprites)
button3 = lvl3(lvls_sprites)
name_of_stage = table(lvls_sprites)
compl = completed(lvls_sprites, 1)

already_checked1 = False
already_checked2 = False

while lvl_selecting:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lvl_selecting = False

    lvls_sprites.update()
    lvls_sprites.draw(screen3)

    pygame.display.flip()
    clock.tick(FPS)


