import config
import pygame


def quite_game():
    config.running = False
    config.is_menu = False


def start_game():
    config.is_menu = False
    while config.running:
        config.clock.tick(config.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                config.running = False
                quit()


        pygame.display.flip()
