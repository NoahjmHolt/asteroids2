
import pygame
import sys

from constants import *
from logger import *

from player import *
from shot import *

from asteroid import *
from asteroidfield import AsteroidField

def main():

    # print("Starting Asteroids with pygame version: VERSION")
    # print(f'Screen width: {SCREEN_WIDTH}')
    # print(f'Screen height: {SCREEN_HEIGHT}')
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    # clock
    clock = pygame.time.Clock()
    dt = 0

    # player
    mother_ship = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    danger_zone = AsteroidField()

    # keep playing while game is open
    while True:
        log_state()
        # this lets exit button work
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)
        asteroids.update(dt)

        for rock in asteroids:
            if rock.collides_with(mother_ship):
                log_event("player_hit")
                print('Game over!')
                sys.exit(0)

        # make screen filled and then display so user knows where ship and rocks are
        screen.fill('black')

        for flying in drawable:
            flying.draw(screen)
        for rock in asteroids:
            rock.draw(screen
                      )
        pygame.display.flip()

        # time keeps ticking
        new_dt = clock.tick(60)
        dt = new_dt / 1000

if __name__ == "__main__":
    main()
