
import random

from circleshape import *
from constants import *
from logger import log_event


class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):

        self.kill()
        if self.radius() <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")
        change_angle = random.uniform(20, 50)

        first_new = self.velocity.rotate(change_angle)
        second_new = self.velocity.rotate(-1 * change_angle)
        new_size = self.radius - ASTEROID_MIN_RADIUS

        asteroid_1 = Asteroid(self.x, self.y, new_size)
        asteroid_2 = Asteroid(self.x, self.y, new_size)
        asteroid_1.velocity = 1.2 * first_new
        asteroid_2.velocity = 1.2 * second_new



