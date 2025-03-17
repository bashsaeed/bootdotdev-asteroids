#!/usr/bin/env python3
import pygame
import constants
from player import Player


def main() -> None:
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    player = Player(constants.SCREEN_WIDTH // 2, constants.SCREEN_HEIGHT // 2)

    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()

    player.containers = updatable_group, drawable_group

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
