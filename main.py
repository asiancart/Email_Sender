import pygame
import time
import os

run = True
WIDTH, HEIGHT = 1000, 500
FPS = 60

# Red Green and Blue
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")


def red():
    WIN.fill((250, 0, 0))
    pygame.display.update()
    time.sleep(1)


def green():
    WIN.fill((0, 250, 0))
    pygame.display.update()
    time.sleep(1)


def blue():
    WIN.fill((0, 0, 250))
    pygame.display.update()
    time.sleep(1)


def rgb():
    while run == True:
        red()
        green()
        blue()


def main():
    rgb()
    clock = pygame.time.Clock()
    run = True
    while run == True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()


if __name__ == "__main__":
    main()