import pygame
import random
from work_with_sprites import load_image, logo, play, info, author, back, room, words
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


    state = 0
    states = ["menu", "lobby", "scene", "lvl1", "lvl2", "lvl3", "abt_info", "final", "lvls"]

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))
        if states[state] == "menu":
            menu_sprites.update()
            if info_button.update(event) == "yes":
                state = 6
            elif play_button.update(event) == "yes":
                state = 2
            menu_sprites.draw(screen)

        elif states[state] == "abt_info":
            info_sprites.update()
            if back_button.update(event) == "yes":
                state = 0
            info_sprites.draw(screen)

        elif states[state] == "scene":
            scene_sprites.update(event)
            scene_sprites.draw(screen)

        pygame.display.flip()
        time.sleep(0.05)
    pygame.quit()