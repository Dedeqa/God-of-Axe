import config
import pygame
import time

pygame.mixer.pre_init(44100, -16, 1, 512)


def start_game():
    config.play_music.set_volume(0.009)
    config.play_music.play(-1)
    while True:
        config.clock.tick(config.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    config.play_music.stop()
                    pygame.mixer.music.unpause()
                    menu()

        config.screen.blit(config.game_bg, (0, 0))
        pygame.display.flip()


def menu():
    if config.menu_flag:
        pygame.mixer.music.set_volume(0.07)
        pygame.mixer.music.play(-1)
        config.menu_flag = False

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
            pygame.mixer.music.pause()
            if start1 > 2:
                config.click.play()
                start1 = 0
                time.sleep(0.2)
                start_game()
            start1 += 1

        else:
            config.screen.blit(config.play_transform, config.play_rect)

        if (config.options_rect.left <= mouse[0] <= config.options_rect.right) and (
                config.options_rect.top <= mouse[1] <= config.options_rect.bottom) and click[0]:
            if start2 > 2:
                config.click.play()
                start2 = 0
                time.sleep(0.2)
                options()
            start2 += 1
            config.screen.blit(config.active_options, config.active_options_rect)

        else:
            config.screen.blit(config.options, config.options_rect)

        if (config.quite_rect.left <= mouse[0] <= config.quite_rect.right) and (
                config.quite_rect.top <= mouse[1] <= config.quite_rect.bottom) and \
                click[0]:
            config.screen.blit(config.active_quite, config.active_quite_rect)
            if start3 > 2:
                config.click.play()
                start3 = 0
                time.sleep(0.2)
                quit()
            start3 += 1
        else:
            config.screen.blit(config.quite, config.quite_rect)
        pygame.display.flip()


def options():
    while True:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        config.clock.tick(config.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    config.play_music.stop()
                    pygame.mixer.music.unpause()
                    menu()

        config.screen.blit(config.menu_bg, (0, 0))
        config.screen.blit(config.menu_title, config.menu_title_rect)
        config.screen.blit(config.tablet, config.tablet_rect)
        config.screen.blit(config.music_label, config.music_label_rect)
        config.screen.blit(config.scale1, config.scale1_rect)
        config.screen.blit(config.sounds_label, config.sounds_label_rect)
        config.screen.blit(config.scale2, config.scale2_rect)

        pygame.display.flip()
