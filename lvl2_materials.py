import pygame
import os
import sys
from work_with_sprites import load_image


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
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
                                                          (200 + x * self.cell_size + 40, 75 + y * self.cell_size + 22)),
                                        2)
