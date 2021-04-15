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
    def __init__(self):
        pass

    def draw(self):
        pygame.draw.rect(screen, (0, 0, 0), (self.x, self.y, 20, 70))


class Player(Paddle):
    def __init__(self):
        Paddle.__init__(self)
        self.x = 30
        self.y = 30



class Opponent(Paddle):
    def __init__(self):
        pass


SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = Player()

done = False

while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
    
    screen.fill((255, 255, 255))

    pressed = pygame.key.get_pressed()

    for key in pressed:
        if key == pygame.locals.K_UP:
            player.y -= 5
        if key == pygame.locals.K_DOWN:
            player.y += 5

    player.draw()

    pygame.display.update()