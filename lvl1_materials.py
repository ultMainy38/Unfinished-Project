import pygame
import random


def changing_marks(circle_run):
    if circle_run == ["+", "-"]:
        bruh = [["+", "+"], ["-", "+"]]
        return random.choice(bruh)
    elif circle_run == ["+", "+"]:
        bruh = [["+", "-"], ["-", "-"]]
        return random.choice(bruh)
    elif circle_run == ["-", "+"]:
        bruh = [["+", "-"], ["+", "+"]]
        return random.choice(bruh)
    elif circle_run == ["-", "-"]:
        bruh = [["-", "+"], ["+", "+"]]
        return random.choice(bruh)
    elif circle_run == [".", "."]:
        return [".", "."]


def moving_circle(circle, circle_run):
    if circle_run[0] == "+":
        circle[0] += 5
    elif circle_run[0] == "-":
        circle[0] -= 5

    if circle_run[1] == "+":
        circle[1] += 5
    elif circle_run[1] == "-":
        circle[1] -= 5


def bricks():
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

    return full_bricks


def change_direction(circle, circle_run):
    if circle[0] == 1190:
        circle_run[0] = "-"
    elif circle[0] == 0:
        circle_run[0] = "+"

    if circle[1] == 790:
        circle_run[1] = "-"
    elif circle[1] == 10:
        circle_run[1] = "+"
