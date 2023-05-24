import config as cfg
import images as img
import sounds
import pygame
import time
import classes
import random
import mobs
import sprite_func

pygame.mixer.pre_init(44100, -16, 1, 512)


def start_game():
    if cfg.start_game_flag:
        # cfg.play_music.play(-1)
        cfg.start_game_flag = False
    monster_generator(30)
    tree_generator1(400)
    # tree_generator2(150)
    while True:
        cfg.clock.tick(cfg.FPS)
        # print(cfg.clock.get_fps())
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause()

        cfg.screen.blit(img.game_bg, (-1920 + cfg.bg_x, -1080 + cfg.bg_y))  # 1 зона
        cfg.screen.blit(img.game_bg, (0 + cfg.bg_x, -1080 + cfg.bg_y))  # 2 зона
        cfg.screen.blit(img.game_bg, (1920 + cfg.bg_x, -1080 + cfg.bg_y))  # 3 зона
        cfg.screen.blit(img.game_bg, (-1920 + cfg.bg_x, 0 + cfg.bg_y))  # 4 зона
        cfg.screen.blit(img.game_bg, (0 + cfg.bg_x, 0 + cfg.bg_y))  # 5 зона
        cfg.screen.blit(img.game_bg, (1920 + cfg.bg_x, 0 + cfg.bg_y))  # 6 зона
        cfg.screen.blit(img.game_bg, (-1920 + cfg.bg_x, 1080 + cfg.bg_y))  # 7 зона
        cfg.screen.blit(img.game_bg, (0 + cfg.bg_x, 1080 + cfg.bg_y))  # 8 зона
        cfg.screen.blit(img.game_bg, (1920 + cfg.bg_x, 1080 + cfg.bg_y))  # 9 зона

        classes.all_sprites.update()
        classes.all_sprites.draw(cfg.screen)
        classes.player.draw_shield_bar(cfg.screen, 660, 10, classes.player.wood_amount, "brown",
                                       "red", "black", 150, 600, 20)
        classes.player.draw_text(cfg.screen, f'{int(classes.player.progress)}%', 14 , 960, 12)
        pygame.display.flip()


def menu():
    sounds.play_music.stop()
    if cfg.menu_flag:
        # pygame.mixer.music.play(-1)
        cfg.menu_flag = False

    start1, start2, start3 = 0, 0, 0
    while True:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        cfg.clock.tick(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        cfg.screen.blit(img.menu_bg, (0, 0))
        cfg.screen.blit(cfg.menu_title, cfg.menu_title_rect)

        if (cfg.play_rect.left <= mouse[0] <= cfg.play_rect.right) and (
                cfg.play_rect.top <= mouse[1] <= cfg.play_rect.bottom) and \
                click[0]:

            cfg.screen.blit(cfg.active_play_transform, cfg.active_play_rect)
            pygame.mixer.music.pause()
            if start1 > 2:
                sounds.click.play()
                start1 = 0
                time.sleep(0.2)
                start_game()
            start1 += 1

        else:
            cfg.screen.blit(cfg.play_transform, cfg.play_rect)

        if (cfg.options_rect.left <= mouse[0] <= cfg.options_rect.right) and (
                cfg.options_rect.top <= mouse[1] <= cfg.options_rect.bottom) and click[0]:
            cfg.screen.blit(img.active_options, cfg.active_options_rect)
            if start2 > 2:
                sounds.click.play()
                start2 = 0
                time.sleep(0.2)
                options_menu()
            start2 += 1
        else:
            cfg.screen.blit(img.options, cfg.options_rect)

        if (cfg.quite_rect.left <= mouse[0] <= cfg.quite_rect.right) and (
                cfg.quite_rect.top <= mouse[1] <= cfg.quite_rect.bottom) and \
                click[0]:
            cfg.screen.blit(img.active_quite, cfg.active_quite_rect)
            if start3 > 2:
                sounds.click.play()
                start3 = 0
                time.sleep(0.2)
                quit()
            start3 += 1
        else:
            cfg.screen.blit(img.quite, cfg.quite_rect)
        pygame.display.flip()


def pause():
    start1, start2, start3 = 0, 0, 0

    while True:

        cfg.screen.blit(img.bg_pause_new, (0, 0))
        cfg.screen.blit(cfg.pause_label_transform, cfg.pause_label_rect)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        cfg.clock.tick(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        if (cfg.continue_rect.left <= mouse[0] <= cfg.continue_rect.right) and (
                cfg.continue_rect.top <= mouse[1] <= cfg.continue_rect.bottom) and \
                click[0]:
            cfg.screen.blit(img.continue_active, cfg.continue_active_rect)

            if start1 > 2:
                sounds.click.play()
                start1 = 0
                time.sleep(0.2)
                cfg.start_game_flag = False
                start_game()
            start1 += 1
        else:
            cfg.screen.blit(img.continue_, cfg.continue_rect)

        if (cfg.Options_rect.left <= mouse[0] <= cfg.Options_rect.right) and (
                cfg.Options_rect.top <= mouse[1] <= cfg.Options_rect.bottom) and click[0]:

            cfg.screen.blit(img.Options_active, cfg.Options_active_rect)

            if start2 > 2:
                sounds.click.play()
                start2 = 0
                time.sleep(0.2)
                options_game()
            start2 += 1

        else:
            cfg.screen.blit(img.Options, cfg.Options_rect)

        if (cfg.menu_rect.left <= mouse[0] <= cfg.menu_rect.right) and (
                cfg.menu_rect.top <= mouse[1] <= cfg.menu_rect.bottom) and \
                click[0]:
            cfg.screen.blit(img.menu_active, cfg.menu_active_rect)
            if start3 > 2:
                sounds.click.play()
                start3 = 0
                time.sleep(0.2)
                pygame.mixer.music.unpause()
                cfg.start_game_flag = True
                menu()
            start3 += 1
        else:
            cfg.screen.blit(img.menu, cfg.menu_rect)
        pygame.display.flip()


def options_menu():
    while True:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        cfg.clock.tick(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sounds.play_music.stop()
                    pygame.mixer.music.unpause()
                    menu()
            if click[0] and (cfg.point1_rect.collidepoint(mouse[0], mouse[1])) and (
                    cfg.scale1_rect.left <= mouse[0] <= cfg.scale1_rect.right):
                cfg.point1_rect.center = (mouse[0], cfg.scale1_rect.centery)
                sounds.volume_music = 0.01 * ((cfg.point1_rect.centerx - cfg.scale1_rect.left) / 3)

                sounds.play_music.set_volume(sounds.volume_music)
                pygame.mixer.music.set_volume(sounds.volume_music)

            if click[0] and (cfg.point2_rect.collidepoint(mouse[0], mouse[1])) and (
                    cfg.scale2_rect.left <= mouse[0] <= cfg.scale2_rect.right):
                cfg.point2_rect.center = (mouse[0], cfg.scale2_rect.centery)
                sounds.volume_sounds = 0.01 * ((cfg.point2_rect.centerx - cfg.scale2_rect.left) / 3)

                sounds.click.set_volume(sounds.volume_sounds)
                sounds.wave.set_volume(sounds.volume_sounds)
                sounds.hit_tree.set_volume(sounds.volume_sounds)
                sounds.agr_monster.set_volume(sounds.volume_sounds)
                sounds.falling_tree.set_volume(sounds.volume_sounds)

        cfg.screen.blit(img.menu_bg, (0, 0))
        cfg.screen.blit(cfg.menu_title, cfg.menu_title_rect)
        cfg.screen.blit(cfg.tablet_transform, cfg.tablet_rect)
        cfg.screen.blit(img.music_label, cfg.music_label_rect)
        cfg.screen.blit(img.scale1, cfg.scale1_rect)
        cfg.screen.blit(img.sounds_label, cfg.sounds_label_rect)
        cfg.screen.blit(img.scale2, cfg.scale2_rect)
        cfg.screen.blit(img.point1, cfg.point1_rect)
        cfg.screen.blit(img.point2, cfg.point2_rect)

        pygame.display.flip()


def options_game():
    while True:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        cfg.clock.tick(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause()
            if click[0] and (cfg.point1_rect.collidepoint(mouse[0], mouse[1])) and (
                    cfg.scale1_rect.left <= mouse[0] <= cfg.scale1_rect.right):
                cfg.point1_rect.center = (mouse[0], cfg.scale1_rect.centery)
                sounds.volume_music = 0.01 * ((cfg.point1_rect.centerx - cfg.scale1_rect.left) / 3)

                pygame.mixer.music.set_volume(sounds.volume_music)
                sounds.play_music.set_volume(sounds.volume_music)

            if click[0] and (cfg.point2_rect.collidepoint(mouse[0], mouse[1])) and (
                    cfg.scale2_rect.left <= mouse[0] <= cfg.scale2_rect.right):
                cfg.point2_rect.center = (mouse[0], cfg.scale2_rect.centery)
                sounds.volume_sounds = 0.01 * ((cfg.point2_rect.centerx - cfg.scale2_rect.left) / 3)

                sounds.click.set_volume(sounds.volume_sounds)
                sounds.wave.set_volume(sounds.volume_sounds)
                sounds.hit_tree.set_volume(sounds.volume_sounds)
                sounds.agr_monster.set_volume(sounds.volume_sounds)
                sounds.falling_tree.set_volume(sounds.volume_sounds)

        cfg.screen.blit(cfg.tablet_transform, cfg.tablet_rect)
        cfg.screen.blit(img.music_label, cfg.music_label_rect)
        cfg.screen.blit(img.scale1, cfg.scale1_rect)
        cfg.screen.blit(img.sounds_label, cfg.sounds_label_rect)
        cfg.screen.blit(img.scale2, cfg.scale2_rect)
        cfg.screen.blit(img.point1, cfg.point1_rect)
        cfg.screen.blit(img.point2, cfg.point2_rect)

        pygame.display.flip()


def tree_generator1(n):
    count = 0
    while count < n:
        cfg.add_flag = True
        x = random.randint(-1870, 3740)
        y = random.randint(-1030, 2000)

        for i in range(count):
            if abs(cfg.tree_list_x[i] - x) < cfg.delta and abs(cfg.tree_list_y[i] - y) < cfg.delta:
                cfg.add_flag = False

        if cfg.add_flag:
            cfg.tree_list_x.append(x)
            cfg.tree_list_y.append(y)
            count += 1

    cfg.trees1 = [classes.Tree(f'Дуб{i}', 500, cfg.tree_list_x[i], cfg.tree_list_y[i], 5) for i in range(0, n - 1, 2)]
    cfg.trees2 = [classes.Tree(f'Елка{i}', 1000, cfg.tree_list_x[i], cfg.tree_list_y[i], 10) for i in
                  range(1, n - 2, 2)]

    for elem in cfg.trees1:
        classes.all_sprites.add(elem)
        cfg.trees_rects_left.append(elem.line_left)
        cfg.trees_rects_right.append(elem.line_right)
        cfg.trees_rects_top.append(elem.line_top)
        cfg.trees_rects_bottom.append(elem.line_bottom)

    for elem in cfg.trees2:
        elem.image = pygame.image.load('Images/Trees/Tree2.png')
        classes.all_sprites.add(elem)
        cfg.trees_rects_left.append(elem.line_left)
        cfg.trees_rects_right.append(elem.line_right)
        cfg.trees_rects_top.append(elem.line_top)
        cfg.trees_rects_bottom.append(elem.line_bottom)


def monster_generator(n):
    count = 0
    while count < n:
        cfg.add_flag = True
        x = random.randint(-1870, 3740)
        y = random.randint(-1030, 2000)

        for i in range(count):
            if (abs(cfg.monster_list_x[i] - x) < cfg.delta_monsters or abs(
                    cfg.monster_list_y[i] - y) < cfg.delta_monsters) and (abs(
                cfg.monster_list_x[i] - classes.player.rect.x) < cfg.delta_hero or abs(
                cfg.monster_list_y[i] - classes.player.rect.y) < cfg.delta_hero):
                cfg.add_flag = False

        if cfg.add_flag:
            cfg.monster_list_x.append(x)
            cfg.monster_list_y.append(y)
            count += 1
    cfg.monsterList = [mobs.Monster(f'Минотавр{i}', 500, cfg.monster_list_x[i], cfg.monster_list_y[i], 300, 20) for i in
                       range(n)]
    cfg.monsterList.append(mobs.min1)
    classes.all_sprites.add(mobs.min1)
    for elem in cfg.monsterList:
        classes.all_sprites.add(elem)
