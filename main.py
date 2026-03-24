
import pygame
from constants import *
from logger import log_state
from player import *

def main():

    # print("Starting Asteroids with pygame version: VERSION")
    # print(f'Screen width: {SCREEN_WIDTH}')
    # print(f'Screen height: {SCREEN_HEIGHT}')
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    # clock
    clock = pygame.time.Clock()
    dt = 0

    # player
    mother_ship = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    # keep playing while game is open
    while True:
        log_state()
        # this lets exit button work
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        # make screen filled and then display so user knows where ship and rocks are
        screen.fill('black')
        for flying in drawable:
            flying.draw(screen)
        pygame.display.flip()

        # time keeps ticking
        new_dt = clock.tick(60)
        dt = new_dt / 1000

if __name__ == "__main__":
    main()
