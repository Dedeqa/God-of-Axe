import config as cfg
import pygame
import time
import classes

pygame.mixer.pre_init(44100, -16, 1, 512)


def start_game():
    cfg.play_music.set_volume(cfg.volume_music)
    cfg.play_music.play(-1)
    while True:
        cfg.clock.tick(cfg.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    cfg.play_music.stop()
                    pygame.mixer.music.unpause()
                    menu()
        cfg.screen.blit(cfg.game_bg, (-1920 + cfg.bg_x, -1080 + cfg.bg_y))  # 1 зона
        cfg.screen.blit(cfg.game_bg, (0 + cfg.bg_x, -1080 + cfg.bg_y))  # 2 зона
        cfg.screen.blit(cfg.game_bg, (1920 + cfg.bg_x, -1080 + cfg.bg_y))  # 3 зона
        cfg.screen.blit(cfg.game_bg, (-1920 + cfg.bg_x, 0 + cfg.bg_y))  # 4 зона
        cfg.screen.blit(cfg.game_bg, (0 + cfg.bg_x, 0 + cfg.bg_y))  # 5 зона
        cfg.screen.blit(cfg.game_bg, (1920 + cfg.bg_x, 0 + cfg.bg_y))  # 6 зона
        cfg.screen.blit(cfg.game_bg, (-1920 + cfg.bg_x, 1080 + cfg.bg_y))  # 7 зона
        cfg.screen.blit(cfg.game_bg, (0 + cfg.bg_x, 1080 + cfg.bg_y))  # 8 зона
        cfg.screen.blit(cfg.game_bg, (1920 + cfg.bg_x, 1080 + cfg.bg_y))  # 9 зона
        classes.all_sprites.update()
        classes.all_sprites.draw(cfg.screen)
        pygame.display.flip()


def menu():
    if cfg.menu_flag:
        pygame.mixer.music.play(-1)
        cfg.menu_flag = False

    start1, start2, start3 = 0, 0, 0
    while True:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        cfg.clock.tick(cfg.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        cfg.screen.blit(cfg.menu_bg, (0, 0))
        cfg.screen.blit(cfg.menu_title, cfg.menu_title_rect)

        if (cfg.play_rect.left <= mouse[0] <= cfg.play_rect.right) and (
                cfg.play_rect.top <= mouse[1] <= cfg.play_rect.bottom) and \
                click[0]:

            cfg.screen.blit(cfg.active_play_transform, cfg.active_play_rect)
            pygame.mixer.music.pause()
            if start1 > 2:
                cfg.click.play()
                start1 = 0
                time.sleep(0.2)
                start_game()
            start1 += 1

        else:
            cfg.screen.blit(cfg.play_transform, cfg.play_rect)

        if (cfg.options_rect.left <= mouse[0] <= cfg.options_rect.right) and (
                cfg.options_rect.top <= mouse[1] <= cfg.options_rect.bottom) and click[0]:
            if start2 > 2:
                cfg.click.play()
                start2 = 0
                time.sleep(0.2)
                options()
            start2 += 1
            cfg.screen.blit(cfg.active_options, cfg.active_options_rect)

        else:
            cfg.screen.blit(cfg.options, cfg.options_rect)

        if (cfg.quite_rect.left <= mouse[0] <= cfg.quite_rect.right) and (
                cfg.quite_rect.top <= mouse[1] <= cfg.quite_rect.bottom) and \
                click[0]:
            cfg.screen.blit(cfg.active_quite, cfg.active_quite_rect)
            if start3 > 2:
                cfg.click.play()
                start3 = 0
                time.sleep(0.2)
                quit()
            start3 += 1
        else:
            cfg.screen.blit(cfg.quite, cfg.quite_rect)
        pygame.display.flip()


def options():
    FPS = 120
    while True:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        cfg.clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    cfg.play_music.stop()
                    pygame.mixer.music.unpause()
                    menu()
            if click[0] and (cfg.point1_rect.collidepoint(mouse[0], mouse[1])) and (
                    cfg.scale1_rect.left <= mouse[0] <= cfg.scale1_rect.right):
                cfg.point1_rect.center = (mouse[0], cfg.scale1_rect.centery)
                cfg.volume_music = 0.01 * ((cfg.point1_rect.centerx - cfg.scale1_rect.left) / 3)
                pygame.mixer.music.set_volume(cfg.volume_music)

            if click[0] and (cfg.point2_rect.collidepoint(mouse[0], mouse[1])) and (
                    cfg.scale2_rect.left <= mouse[0] <= cfg.scale2_rect.right):
                cfg.point2_rect.center = (mouse[0], cfg.scale2_rect.centery)
                cfg.volume_sounds = 0.01 * ((cfg.point2_rect.centerx - cfg.scale2_rect.left) / 3)
                cfg.click.set_volume(cfg.volume_sounds)

        cfg.screen.blit(cfg.menu_bg, (0, 0))
        cfg.screen.blit(cfg.menu_title, cfg.menu_title_rect)
        cfg.screen.blit(cfg.tablet, cfg.tablet_rect)
        cfg.screen.blit(cfg.music_label, cfg.music_label_rect)
        cfg.screen.blit(cfg.scale1, cfg.scale1_rect)
        cfg.screen.blit(cfg.sounds_label, cfg.sounds_label_rect)
        cfg.screen.blit(cfg.scale2, cfg.scale2_rect)
        cfg.screen.blit(cfg.point1, cfg.point1_rect)
        cfg.screen.blit(cfg.point2, cfg.point2_rect)

        pygame.display.flip()
