
import pygame
from constants import *
from logger import log_state

def main():

    # print("Starting Asteroids with pygame version: VERSION")
    # print(f'Screen width: {SCREEN_WIDTH}')
    # print(f'Screen height: {SCREEN_HEIGHT}')
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # keep playing while game is open
    while True:
        log_state()
        for event in pygame.event.get():
            pass

        # this lets exit button work
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # make screen filled and then display so user knows where ship and rocks are
        screen.fill('black')
        pygame.display.flip()

if __name__ == "__main__":
    main()
