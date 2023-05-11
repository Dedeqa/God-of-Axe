import config
import pygame


def quite_game():
    config.running = False
    config.is_menu = False
    quit()


def start_game():
    config.is_menu = False
    while config.running:
        config.clock.tick(config.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                config.running = False
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    menu()
                    config.running = False
                    print("ESC")

        config.screen.fill((255, 22, 123))
        pygame.display.flip()


def menu():
    is_menu = True

    # music = pygame.mixer.Sound(r'Music\tick.mp3')
    start1, start2, start3 = 0, 0, 0
    while is_menu:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        config.clock.tick(config.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                config.running = False
                quit()

        config.screen.blit(config.menu_bg, (0, 0))
        config.screen.blit(config.menu_title, config.menu_title_rect)

        if (config.play_rect.left <= mouse[0] <= config.play_rect.right) and (
                config.play_rect.top <= mouse[1] <= config.play_rect.bottom) and \
                click[0]:

            config.screen.blit(config.active_play_transform, config.active_play_rect)
            if start1 > 3:
                start1 = 0
                start_game()
                # music.play()
            start1 += 1

        else:
            config.screen.blit(config.play_transform, config.play_rect)

        if (config.options_rect.left <= mouse[0] <= config.options_rect.right) and (
                config.options_rect.top <= mouse[1] <= config.options_rect.bottom) and click[0]:
            if start2 > 3:
                start2 = 0
                # music.play()
            start2 += 1
            config.screen.blit(config.active_options, config.active_options_rect)

        else:
            config.screen.blit(config.options, config.options_rect)

        if (config.quite_rect.left <= mouse[0] <= config.quite_rect.right) and (
                config.quite_rect.top <= mouse[1] <= config.quite_rect.bottom) and \
                click[0]:
            config.screen.blit(config.active_quite, config.active_quite_rect)
            if start3 > 3:
                start3 = 0
                quite_game()
            start3 += 1
        else:
            config.screen.blit(config.quite, config.quite_rect)
        pygame.display.flip()


menu()
