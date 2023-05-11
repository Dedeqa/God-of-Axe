import config
import pygame
import time


def quite_game():
    config.running = False
    config.is_menu = False
    quit()


def start_game():
    while True:
        config.clock.tick(config.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    menu()

        config.screen.fill((255, 22, 123))
        pygame.display.flip()


def menu():
    music = pygame.mixer.Sound(r'Music\tick.mp3')
    start1, start2, start3 = 0, 0, 0
    while True:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        config.clock.tick(config.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        config.screen.blit(config.menu_bg, (0, 0))
        config.screen.blit(config.menu_title, config.menu_title_rect)

        if (config.play_rect.left <= mouse[0] <= config.play_rect.right) and (
                config.play_rect.top <= mouse[1] <= config.play_rect.bottom) and \
                click[0]:

            config.screen.blit(config.active_play_transform, config.active_play_rect)

            if start1 > 2:
                music.play()
                start1 = 0
                time.sleep(0.2)
                start_game()
            start1 += 1

        else:
            config.screen.blit(config.play_transform, config.play_rect)

        if (config.options_rect.left <= mouse[0] <= config.options_rect.right) and (
                config.options_rect.top <= mouse[1] <= config.options_rect.bottom) and click[0]:
            if start2 > 2:
                music.play()
                start2 = 0
                time.sleep(0.2)
            start2 += 1
            config.screen.blit(config.active_options, config.active_options_rect)

        else:
            config.screen.blit(config.options, config.options_rect)

        if (config.quite_rect.left <= mouse[0] <= config.quite_rect.right) and (
                config.quite_rect.top <= mouse[1] <= config.quite_rect.bottom) and \
                click[0]:
            config.screen.blit(config.active_quite, config.active_quite_rect)
            if start3 > 2:
                music.play()
                start3 = 0
                time.sleep(0.2)
                quite_game()
            start3 += 1
        else:
            config.screen.blit(config.quite, config.quite_rect)
        pygame.display.flip()
