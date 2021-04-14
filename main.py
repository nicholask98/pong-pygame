import pygame
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

class Paddle:
    def __init__():
        pass


class Player(Paddle):
    def __init__():
        pass


class Opponent(Paddle):
    def __init__():
        pass




SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


done = False

while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
    
    screen.fill((255, 255, 255))

    pressed = pygame.key.get_pressed()
    for key in pressed:
        if key == K_UP







    pygame.display.update()