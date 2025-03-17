import pygame
from circleshape import CircleShape
import constants


class Shot(CircleShape):
    def __init__(self, x, y) -> None:
        super().__init__(x, y, constants.SHOT_RADIUS)

    def draw(self, screen) -> None:
        pygame.draw.circle(
            screen,
            color="white",
            center=self.position,
            radius=self.radius,
            width=2,
        )

    def update(self, dt) -> None:
        self.position += self.velocity * dt
