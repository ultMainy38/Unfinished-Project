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
    full_bricks = []
    for x in range(0, 1200, 100):
        for y in range(0, 150, 50):
            brick = pygame.Rect(x, y, 100, 50)
            full_bricks.append(brick)

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
