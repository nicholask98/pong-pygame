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
        self.height = 70

    def draw(self):
        pygame.draw.rect(screen, (0, 0, 0), (self.x, self.y, 20, self.height))


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

vel = 5

while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
    
    screen.fill((255, 255, 255))

    pressed = pygame.key.get_pressed()

    # Player Controls
    if pressed[K_UP]:
        player.y -= vel
    if pressed[K_DOWN]:
        player.y += vel

    if player.y >= SCREEN_HEIGHT - player.height:
        player.y = SCREEN_HEIGHT - player.height
    elif player.y <= 0:
        player.y = 0

    player.draw()

    pygame.display.update()
    