import config as cfg
import pygame
import time
import classes
import random

pygame.mixer.pre_init(44100, -16, 1, 512)


def start_game():
    if cfg.start_game_flag:
        # cfg.play_music.play(-1)
        cfg.start_game_flag = False
    tree_generator(50)
    while True:
        cfg.clock.tick(cfg.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print(classes.tree.hp)
                    pause()

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
    cfg.play_music.stop()
    if cfg.menu_flag:
        # pygame.mixer.music.play(-1)
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
            cfg.screen.blit(cfg.active_options, cfg.active_options_rect)
            if start2 > 2:
                cfg.click.play()
                start2 = 0
                time.sleep(0.2)
                options_menu()
            start2 += 1
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


def pause():
    start1, start2, start3 = 0, 0, 0

    while True:

        cfg.screen.blit(cfg.bg_pause_new, (0, 0))
        cfg.screen.blit(cfg.pause_label_transform, cfg.pause_label_rect)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        cfg.clock.tick(cfg.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        if (cfg.continue_rect.left <= mouse[0] <= cfg.continue_rect.right) and (
                cfg.continue_rect.top <= mouse[1] <= cfg.continue_rect.bottom) and \
                click[0]:
            cfg.screen.blit(cfg.continue_active, cfg.continue_active_rect)

            if start1 > 2:
                cfg.click.play()
                start1 = 0
                time.sleep(0.2)
                cfg.start_game_flag = False
                start_game()
            start1 += 1
        else:
            cfg.screen.blit(cfg.continue_, cfg.continue_rect)

        if (cfg.Options_rect.left <= mouse[0] <= cfg.Options_rect.right) and (
                cfg.Options_rect.top <= mouse[1] <= cfg.Options_rect.bottom) and click[0]:

            cfg.screen.blit(cfg.Options_active, cfg.Options_active_rect)

            if start2 > 2:
                cfg.click.play()
                start2 = 0
                time.sleep(0.2)
                options_game()
            start2 += 1

        else:
            cfg.screen.blit(cfg.Options, cfg.Options_rect)

        if (cfg.menu_rect.left <= mouse[0] <= cfg.menu_rect.right) and (
                cfg.menu_rect.top <= mouse[1] <= cfg.menu_rect.bottom) and \
                click[0]:
            cfg.screen.blit(cfg.menu_active, cfg.menu_active_rect)
            if start3 > 2:
                cfg.click.play()
                start3 = 0
                time.sleep(0.2)
                pygame.mixer.music.unpause()
                cfg.start_game_flag = True
                menu()
            start3 += 1
        else:
            cfg.screen.blit(cfg.menu, cfg.menu_rect)
        pygame.display.flip()


def options_menu():
    while True:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        cfg.clock.tick(200)
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

                cfg.play_music.set_volume(cfg.volume_music)
                pygame.mixer.music.set_volume(cfg.volume_music)

            if click[0] and (cfg.point2_rect.collidepoint(mouse[0], mouse[1])) and (
                    cfg.scale2_rect.left <= mouse[0] <= cfg.scale2_rect.right):
                cfg.point2_rect.center = (mouse[0], cfg.scale2_rect.centery)
                cfg.volume_sounds = 0.01 * ((cfg.point2_rect.centerx - cfg.scale2_rect.left) / 3)
                cfg.click.set_volume(cfg.volume_sounds)

        cfg.screen.blit(cfg.menu_bg, (0, 0))
        cfg.screen.blit(cfg.menu_title, cfg.menu_title_rect)
        cfg.screen.blit(cfg.tablet_transform, cfg.tablet_rect)
        cfg.screen.blit(cfg.music_label, cfg.music_label_rect)
        cfg.screen.blit(cfg.scale1, cfg.scale1_rect)
        cfg.screen.blit(cfg.sounds_label, cfg.sounds_label_rect)
        cfg.screen.blit(cfg.scale2, cfg.scale2_rect)
        cfg.screen.blit(cfg.point1, cfg.point1_rect)
        cfg.screen.blit(cfg.point2, cfg.point2_rect)

        pygame.display.flip()


def options_game():
    while True:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        cfg.clock.tick(200)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause()
            if click[0] and (cfg.point1_rect.collidepoint(mouse[0], mouse[1])) and (
                    cfg.scale1_rect.left <= mouse[0] <= cfg.scale1_rect.right):
                cfg.point1_rect.center = (mouse[0], cfg.scale1_rect.centery)
                cfg.volume_music = 0.01 * ((cfg.point1_rect.centerx - cfg.scale1_rect.left) / 3)

                pygame.mixer.music.set_volume(cfg.volume_music)
                cfg.play_music.set_volume(cfg.volume_music)

            if click[0] and (cfg.point2_rect.collidepoint(mouse[0], mouse[1])) and (
                    cfg.scale2_rect.left <= mouse[0] <= cfg.scale2_rect.right):
                cfg.point2_rect.center = (mouse[0], cfg.scale2_rect.centery)
                cfg.volume_sounds = 0.01 * ((cfg.point2_rect.centerx - cfg.scale2_rect.left) / 3)

                cfg.click.set_volume(cfg.volume_sounds)

        cfg.screen.blit(cfg.tablet_transform, cfg.tablet_rect)
        cfg.screen.blit(cfg.music_label, cfg.music_label_rect)
        cfg.screen.blit(cfg.scale1, cfg.scale1_rect)
        cfg.screen.blit(cfg.sounds_label, cfg.sounds_label_rect)
        cfg.screen.blit(cfg.scale2, cfg.scale2_rect)
        cfg.screen.blit(cfg.point1, cfg.point1_rect)
        cfg.screen.blit(cfg.point2, cfg.point2_rect)

        pygame.display.flip()


def tree_generator(n):
    count = 0
    while count < n:
        x = random.randint(-1870, 3740)
        y = random.randint(-1030, 2060)
        if not (x in cfg.tree_list_x and y in cfg.tree_list_y):
            cfg.tree_list_x.append(x)
            cfg.tree_list_y.append(y)
            count += 1
    cfg.trees = [classes.Tree(f'Дерево{i}', 100, cfg.tree_list_x[i], cfg.tree_list_y[i], 5) for i in range(n)]
    cfg.trees.append(classes.tree)
    for elem in cfg.trees:
        classes.all_sprites.add(elem)

