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

# Paddle classes
class Paddle:
    def __init__(self):
        self.height = 70
        self.width = 20

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 0), (self.x, self.y, self.width, self.height))

class Player(Paddle):
    def __init__(self):
        Paddle.__init__(self)
        self.x = 30
        self.y = 30

class Opponent(Paddle):
    def __init__(self):
        pass


# Ball class
class Ball:
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        self.size = 15
        self.x = SCREEN_WIDTH/2 - self.size
        self.y = SCREEN_HEIGHT/2 - self.size
        self.last_paddle = 'RIGHT'
        self.last_wall = 'BOTTOM'

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 0), (self.x, self.y, self.size, self.size))


    # FIXME: finish get last collisions method first. Then use it to complete Ball Movement Method
    def get_last_collisions(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        if self.last_wall == 'BOTTOM':
            if self.y <= 0:
                self.last_wall = 'TOP'
                self.y = 0
            if self.last_paddle == 'RIGHT':
                if self.x <= 0:
                    self.last_paddle = 'LEFT'
                    self.x = 0
            elif self.last_paddle == 'LEFT':
                if self.x >= SCREEN_WIDTH:
                    self.last_paddle = 'LEFT'
                    self.x = SCREEN_WIDTH - self.size
        elif self.last_wall == 'TOP':
            if self.last_paddle == 'LEFT':
                pass
            elif self.last_paddle == 'RIGHT':
                pass

    # FIXME: Ball Movement section
    # FIXME: Write code that uses get_last_collisions to send ball in the intended diagonal direction.
    def move(self):
        pass

def main():
    SCREEN_WIDTH = 1024
    SCREEN_HEIGHT = 768

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    player = Player()
    ball = Ball(SCREEN_WIDTH, SCREEN_HEIGHT)
    done = False

    vel = 3

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

        # Top/Bottom barrier collision detection
        if player.y >= SCREEN_HEIGHT - player.height:
            player.y = SCREEN_HEIGHT - player.height
        elif player.y <= 0:
            player.y = 0



        player.draw(screen)
        ball.draw(screen)

        pygame.display.update()




if __name__ == '__main__':
    main()