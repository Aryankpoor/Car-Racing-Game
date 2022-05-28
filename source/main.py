import pygame
import time
import math

from utils import scale_image

GRASS = scale_image(pygame.image.load("grass.jpg"), 2.5)
TRACK = scale_image(pygame.image.load("track.png"), 0.9)
TRACK_BORDER = scale_image(pygame.image.load("track-border.png"), 0.9)

FINISH = pygame.image.load("finish.png")

RED_CAR = pygame.image.load("red-car.png")
GREEN_CAR = pygame.image.load("green-car.png")

WIDTH, HEIGHT = TRACK.get_width(), TRACK.get_height()
WIN = pygame.display.set_mode((WIDTH, 700))
# You can adjust the height of window to your liking to adjust to your computer screen .
#  As I made this on a laptop i have set the height of window to fit to my laptop screen
pygame.display.set_caption("RACING GAME!!")

FPS = 60

run = True
clock = pygame.time.Clock()

while run:
    clock.tick(FPS)

    WIN.blit(GRASS, (0, 0))
    WIN.blit(TRACK, (0, 0))
    WIN.blit(FINISH, (0, 0))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

pygame.quit()        
