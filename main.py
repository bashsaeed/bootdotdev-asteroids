#!/usr/bin/env python3
import sys
import pygame
import constants
from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import Player
from shot import Shot


def main() -> None:
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroids_group = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()

    Asteroid.containers = updatable_group, drawable_group, asteroids_group
    AsteroidField.containers = updatable_group
    asteroid_field = AsteroidField()

    Player.containers = updatable_group, drawable_group
    player = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)

    Shot.containers = updatable_group, drawable_group, shots_group

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable_group.update(dt)

        for asteroid in asteroids_group:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()

            for shot in shots_group:
                if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.split()

        screen.fill("black")

        for obj in drawable_group:
            obj.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
