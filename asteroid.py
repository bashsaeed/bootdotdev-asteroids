from calendar import c
import pygame
import random
from circleshape import CircleShape
import constants


class Asteroid(CircleShape):
    def __init__(self, x, y, radius) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen) -> None:
        pygame.draw.circle(
            screen, color="white", center=self.position, radius=self.radius, width=2
        )

    def update(self, dt) -> None:
        self.move(dt)

    def move(self, dt) -> None:
        self.position += self.velocity * dt

    def split(self) -> None:
        self.kill()

        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)

        a = self.velocity.rotate(random_angle)
        b = self.velocity.rotate(-random_angle)

        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS

        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = a * 1.2
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = b * 1.2
