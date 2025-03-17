import pygame
from circleshape import CircleShape
import constants


class Player(CircleShape):
    def __init__(self, x, y) -> None:
        super().__init__(x, y, constants.PLAYER_RADIUS)
        self.rotation = 0

    def triangle(self) -> list:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen) -> None:
        pygame.draw.polygon(screen, color="white", points=self.triangle(), width=2)

    def update(self, dt) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.move(dt)
        if keys[pygame.K_DOWN]:
            self.move(-dt)
        if keys[pygame.K_RIGHT]:
            self.rotate(dt)
        if keys[pygame.K_LEFT]:
            self.rotate(-dt)

    def rotate(self, dt) -> None:
        self.rotation += constants.PLAYER_TURN_SPEED * dt

    def move(self, dt) -> None:
        direction = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += direction * constants.PLAYER_SPEED * dt
