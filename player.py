import pygame
from circleshape import CircleShape
import constants
from shot import Shot


class Player(CircleShape):
    def __init__(self, x, y) -> None:
        super().__init__(x, y, constants.PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown = 0

    def draw(self, screen) -> None:
        pygame.draw.polygon(screen, color="white", points=self.triangle(), width=2)

    def triangle(self) -> list:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def update(self, dt) -> None:
        keys = pygame.key.get_pressed()

        if self.shot_cooldown > 0:
            self.shot_cooldown -= dt

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def rotate(self, dt) -> None:
        self.rotation += constants.PLAYER_TURN_SPEED * dt

    def move(self, dt) -> None:
        direction = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += direction * constants.PLAYER_SPEED * dt

    def shoot(self) -> Shot:
        if self.shot_cooldown > 0:
            return
        direction = pygame.Vector2(0, 1).rotate(self.rotation)
        position = self.position + direction * self.radius
        shot = Shot(position.x, position.y)
        shot.velocity = direction * constants.PLAYER_SHOOT_SPEED
        self.shot_cooldown = constants.PLAYER_SHOOT_COOLDOWN
