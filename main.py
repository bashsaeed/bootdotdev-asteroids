#!/usr/bin/env python3
import pygame
from asteroid import Asteroid
import constants
from player import Player


def main() -> None:
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()

    Asteroid.containers = updatable_group, drawable_group, asteroid_group

    Player.containers = updatable_group, drawable_group

    player = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable_group.update(dt)

        screen.fill("black")

        for obj in drawable_group:
            obj.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
