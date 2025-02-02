import pygame
import os
import sys
import random
from work_with_sprites import load_image


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.left = 200
        self.top = 75
        self.cell_size = 45

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen, matrix):
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(screen, "WHITE", (self.left + x * self.cell_size, self.top + y * self.cell_size,
                                                   self.cell_size, self.cell_size), 1)
                if matrix[y][x] == "flag":
                    pygame.draw.polygon(screen, "WHITE", ((200 + x * self.cell_size + 5, 75 + y * self.cell_size + 5),
                                                          (200 + x * self.cell_size + 5, 75 + y * self.cell_size + 35),
                                                          (
                                                          200 + x * self.cell_size + 40, 75 + y * self.cell_size + 22)),
                                        2)
                elif matrix[y][x] == "empty":
                    pygame.draw.rect(screen, "WHITE", (self.left + x * self.cell_size, self.top + y * self.cell_size,
                                                       self.cell_size, self.cell_size))
                elif str(matrix[y][x]) in "12345678":
                    f = pygame.font.Font(None, 45)
                    text = f.render(f'{matrix[y][x]}', 1, "WHITE")
                    screen.blit(text, (self.left + x * self.cell_size + 10, self.top + y * self.cell_size + 10))


def generate_matrix():
    variants = ["empty", "bomb"]
    bombs = 60
    matrix = [[""] * 14 for i in range(10)]
    while bombs > 0:
        for y in range(14):
            for x in range(10):
                if bombs > 0:
                    cell = random.choice(variants)
                    if cell == "bomb":
                        bombs -= 1
                else:
                    cell = "empty"
                matrix[x][y] = cell

    for y in range(14):
        for x in range(10):
            if matrix[x][y] == "empty":
                counter = 0
                if x == 0:
                    if y == 0:
                        if matrix[x + 1][y] == "bomb":
                            counter += 1
                        if matrix[x][y + 1] == "bomb":
                            counter += 1
                        if matrix[x + 1][y + 1] == "bomb":
                            counter += 1
                    elif y == 13:
                        if matrix[x + 1][y] == "bomb":
                            counter += 1
                        if matrix[x][y - 1] == "bomb":
                            counter += 1
                        if matrix[x + 1][y - 1] == "bomb":
                            counter += 1
                    else:
                        if matrix[x + 1][y] == "bomb":
                            counter += 1
                        if matrix[x + 1][y + 1] == "bomb":
                            counter += 1
                        if matrix[x + 1][y - 1] == "bomb":
                            counter += 1
                        if matrix[x][y + 1] == "bomb":
                            counter += 1
                        if matrix[x][y - 1] == "bomb":
                            counter += 1

                elif x == 9:
                    if y == 0:
                        if matrix[x - 1][y] == "bomb":
                            counter += 1
                        if matrix[x][y + 1] == "bomb":
                            counter += 1
                        if matrix[x - 1][y + 1] == "bomb":
                            counter += 1
                    elif y == 13:
                        if matrix[x - 1][y] == "bomb":
                            counter += 1
                        if matrix[x][y - 1] == "bomb":
                            counter += 1
                        if matrix[x - 1][y - 1] == "bomb":
                            counter += 1
                    else:
                        if matrix[x][y - 1] == "bomb":
                            counter += 1
                        if matrix[x][y + 1] == "bomb":
                            counter += 1
                        if matrix[x - 1][y] == "bomb":
                            counter += 1
                        if matrix[x - 1][y + 1] == "bomb":
                            counter += 1
                        if matrix[x - 1][y - 1] == "bomb":
                            counter += 1
                elif y == 0:
                    if x == 0:
                        if matrix[x + 1][y] == "bomb":
                            counter += 1
                        if matrix[x][y + 1] == "bomb":
                            counter += 1
                        if matrix[x + 1][y + 1] == "bomb":
                            counter += 1
                    elif x == 9:
                        if matrix[x - 1][y] == "bomb":
                            counter += 1
                        if matrix[x][y + 1] == "bomb":
                            counter += 1
                        if matrix[x - 1][y + 1] == "bomb":
                            counter += 1
                    else:
                        if matrix[x][y + 1] == "bomb":
                            counter += 1
                        if matrix[x + 1][y + 1] == "bomb":
                            counter += 1
                        if matrix[x - 1][y + 1] == "bomb":
                            counter += 1
                        if matrix[x + 1][y] == "bomb":
                            counter += 1
                        if matrix[x - 1][y] == "bomb":
                            counter += 1

                elif y == 13:
                    if x == 0:
                        if matrix[x][y - 1] == "bomb":
                            counter += 1
                        if matrix[x + 1][y] == "bomb":
                            counter += 1
                        if matrix[x + 1][y - 1] == "bomb":
                            counter += 1
                    elif x == 9:
                        if matrix[x - 1][y] == "bomb":
                            counter += 1
                        if matrix[x][y - 1] == "bomb":
                            counter += 1
                        if matrix[x - 1][y - 1] == "bomb":
                            counter += 1
                    else:
                        if matrix[x - 1][y] == "bomb":
                            counter += 1
                        if matrix[x + 1][y] == "bomb":
                            counter += 1
                        if matrix[x][y - 1] == "bomb":
                            counter += 1
                        if matrix[x + 1][y - 1] == "bomb":
                            counter += 1
                        if matrix[x - 1][y - 1] == "bomb":
                            counter += 1
                else:
                    if matrix[x][y - 1] == "bomb":
                        counter += 1
                    if matrix[x + 1][y - 1] == "bomb":
                        counter += 1
                    if matrix[x][y + 1] == "bomb":
                        counter += 1
                    if matrix[x + 1][y + 1] == "bomb":
                        counter += 1
                    if matrix[x + 1][y] == "bomb":
                        counter += 1
                    if matrix[x - 1][y] == "bomb":
                        counter += 1
                    if matrix[x - 1][y + 1] == "bomb":
                        counter += 1
                    if matrix[x - 1][y - 1] == "bomb":
                        counter += 1

                if counter > 0:
                    matrix[x][y] = counter
            else:
                matrix[x][y] = "bomb"

    return matrix
