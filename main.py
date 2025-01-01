import pygame
import random
from work_with_sprites import load_image, logo, play, info
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

    state = 0
    states = ["menu", "lobby", "lvl1", "lvl2", "lvl3", "abt_info", "final"]

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if states[state] == "menu":
            menu_sprites.update()
            menu_sprites.draw(screen)

        pygame.display.flip()
        time.sleep(0.05)
    pygame.quit()