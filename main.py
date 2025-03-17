#!/usr/bin/env python3
import sys
import pygame
import constants
from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import Player


def main() -> None:
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()

    Asteroid.containers = updatable_group, drawable_group, asteroid_group
    AsteroidField.containers = updatable_group
    asteroid_field = AsteroidField()

    Player.containers = updatable_group, drawable_group
    player = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable_group.update(dt)

        for asteroid in asteroid_group:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()

        screen.fill("black")

        for obj in drawable_group:
            obj.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
