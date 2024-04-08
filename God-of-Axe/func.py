import config as cfg
import images as img
import sounds
import pygame
import time
import classes
import random
import mobs


# pygame.mixer.pre_init(44100, -16, 1, 512)   # пока непонятно, нужно или нет


def main():
    start_game()
    while cfg.main_active_flag:
        # Закрытие окна ----------------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        # Меню --------------------------------
        if cfg.menu_active_flag:
            menu()
        # Окно игры ---------------------------
        if cfg.play_game_active_flag:
            play_game()

        if cfg.lose_game_active_flag:
            lose_game()

        if cfg.win_game_active_flag:
            win_game()


def start_game():
    pygame.mixer.pre_init(44100, -16, 1, 512)  # используется для инициализации звуковой системы Pygame
    pygame.init()  # запускает pygame
    # cfg.screen = pygame.display.set_mode(cfg.size) пока непонятно, нужно или нет
    pygame.display.set_caption("God of Axe")
    pygame.display.set_icon(img.icon)
    cfg.main_active_flag = True
    cfg.menu_active_flag = True


def play_game():
    # if cfg.start_game_sound_flag:
    #     sounds.play_music.play(-1)
    #     cfg.start_game_sound_flag = False     больше не воспроизводится музыка в игре
    classes.initit_units()
    cfg.list_all_sprites = cfg.all_sprites.sprites()
    monster_generator(50)
    tree_generator(400)
    while cfg.play_game_active_flag:
        pressed_keys = pygame.key.get_pressed()
        cfg.clock.tick(cfg.FPS)
        cfg.in_game_time = pygame.time.get_ticks()
        # print(cfg.clock.get_fps())
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    cfg.pause_active_flag = True
                    pause()
                # elif event.key == pygame.K_LALT:
                #     cfg.inventory_active_flag = True
                #     inventory()

        cfg.screen.blit(img.game_bg,
                        (-1920 + cfg.list_all_sprites[0].bg_x, -1080 + cfg.list_all_sprites[0].bg_y))  # 1 зона
        cfg.screen.blit(img.game_bg,
                        (0 + cfg.list_all_sprites[0].bg_x, -1080 + cfg.list_all_sprites[0].bg_y))  # 2 зона
        cfg.screen.blit(img.game_bg,
                        (1920 + cfg.list_all_sprites[0].bg_x, -1080 + cfg.list_all_sprites[0].bg_y))  # 3 зона
        cfg.screen.blit(img.game_bg,
                        (-1920 + cfg.list_all_sprites[0].bg_x, 0 + cfg.list_all_sprites[0].bg_y))  # 4 зона
        cfg.screen.blit(img.game_bg,
                        (0 + cfg.list_all_sprites[0].bg_x, 0 + cfg.list_all_sprites[0].bg_y))  # 5 зона
        cfg.screen.blit(img.game_bg,
                        (1920 + cfg.list_all_sprites[0].bg_x, 0 + cfg.list_all_sprites[0].bg_y))  # 6 зона
        cfg.screen.blit(img.game_bg,
                        (-1920 + cfg.list_all_sprites[0].bg_x, 1080 + cfg.list_all_sprites[0].bg_y))  # 7 зона
        cfg.screen.blit(img.game_bg,
                        (0 + cfg.list_all_sprites[0].bg_x, 1080 + cfg.list_all_sprites[0].bg_y))  # 8 зона
        cfg.screen.blit(img.game_bg,
                        (1920 + cfg.list_all_sprites[0].bg_x, 1080 + cfg.list_all_sprites[0].bg_y))  # 9 зона

        cfg.all_sprites.update()
        cfg.all_sprites.draw(cfg.screen)

        cfg.list_all_sprites[0].draw_info_bar(cfg.screen, 0, 1065, cfg.list_all_sprites[0].wood_amount, "brown",
                                              "yellow", "black", 500,
                                              1920, 15)
        cfg.list_all_sprites[0].draw_text(cfg.screen, f'{int(cfg.list_all_sprites[0].progress)} %', 18, 960, 1040,
                                          cfg.font_interface_p,
                                          "red")

        cfg.list_all_sprites[0].draw_info_bar(cfg.screen, 0, 18, cfg.list_all_sprites[0].hp, 'DarkRed', 'red', 'black',
                                              100, 450, 17)
        cfg.list_all_sprites[0].draw_info_bar(cfg.screen, 0, 36, cfg.list_all_sprites[0].stamina, (24, 84, 26),
                                              (255, 255, 0), 'black',
                                              100, 450, 17)
        cfg.list_all_sprites[0].draw_info_bar(cfg.screen, 0, 0, cfg.list_all_sprites[0].armor, (16, 72, 105),
                                              (27, 123, 179), 'black',
                                              100, 450, 17)

        # cfg.screen.blit(img.timer_tablet, (1663, 10))
        pygame.draw.rect(cfg.screen, 'black', (920, 10, 80, 40))
        pygame.draw.rect(cfg.screen, 'black', (830, 47, 260, 40))

        # cfg.list_all_sprites[0].draw_text(cfg.screen, 'seconds left', 32, 915, 50, cfg.my_font_p, "black")

        cfg.list_all_sprites[0].draw_text(cfg.screen, f'{600 - int(cfg.in_game_time / 1000)}', 35, 960, 13,
                                          cfg.my_font_p, (224, 153, 9))
        cfg.list_all_sprites[0].draw_text(cfg.screen, 'seconds left', 30, 960, 50, cfg.my_font_p, (224, 153, 9))

        if pressed_keys[pygame.K_TAB]:  # Реализация показа инвентаря при удержанном Tab
            cfg.screen.blit(img.inventory_tablet, cfg.inventory_tablet_rect)
            cfg.list_all_sprites[0].draw_text(cfg.screen, f'{(cfg.list_all_sprites[0].utilities[0])}', 30, 935, 440,
                                              cfg.font_interface_p,
                                              "white")
            cfg.list_all_sprites[0].draw_text(cfg.screen, f'{(cfg.list_all_sprites[0].utilities[1])}', 30, 1085, 440,
                                              cfg.font_interface_p,
                                              "white")
            cfg.list_all_sprites[0].draw_text(cfg.screen, f'{(cfg.list_all_sprites[0].utilities[2])}', 30, 1235, 440,
                                              cfg.font_interface_p,
                                              "white")
            cfg.list_all_sprites[0].draw_text(cfg.screen, f'{(cfg.list_all_sprites[0].wood_amount)}', 30, 635, 440,
                                              cfg.font_interface_p,
                                              "white")
            cfg.list_all_sprites[0].draw_text(cfg.screen, f'{(cfg.list_all_sprites[0].coins)}', 30, 785, 440,
                                              cfg.font_interface_p,
                                              "white")
            cfg.screen.blit(img.apple_icon, (900, 370))
            cfg.screen.blit(img.shishka_icon, (1050, 370))
            cfg.screen.blit(img.coconut_icon, (1200, 370))
            cfg.screen.blit(img.wood_icon, (600, 370))
            cfg.screen.blit(img.coin_icon, (750, 370))

        if cfg.workshop_active_flag:
            workshop()
        if cfg.lose_flag:
            cfg.play_game_active_flag = False
            cfg.lose_game_active_flag = True
        if cfg.list_all_sprites[0].progress >= 100:
            cfg.list_all_sprites[0].progress = 0
            cfg.play_game_active_flag = False
            cfg.win_game_active_flag = True

        pygame.display.flip()


def lose_game():
    continue_flag = False
    while cfg.lose_game_active_flag:
        cfg.screen.blit(img.die_bg, (0, 0))
        cfg.list_all_sprites[0].draw_text(cfg.screen, 'You were worse than last time!', 40, 960, 900,
                                          cfg.font_interface_p,
                                          "white")
        cfg.list_all_sprites[0].draw_text(cfg.screen, 'Press space to continue...', 30, 960, 1000, cfg.font_interface_p,
                                          "white")
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                continue_flag = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                cfg.lose_game_active_flag = False
                cfg.menu_active_flag = True
                classes.del_units()
                cfg.lose_flag = False
        if continue_flag:
            cfg.screen.fill("black")
            cfg.list_all_sprites[0].draw_text(cfg.screen,
                                              f'You have mastered only {cfg.list_all_sprites[0].progress}%',
                                              30,
                                              960, 200, cfg.font_interface_p, "red")
            cfg.list_all_sprites[0].draw_text(cfg.screen,
                                              f'You have wasted {int(cfg.in_game_time / 1000)} seconds your life',
                                              24,
                                              960, 300, cfg.font_interface_p, "orange")
            cfg.list_all_sprites[0].draw_text(cfg.screen,
                                              f'You have cut down {cfg.list_all_sprites[0].oak_amount} DUBOV, {cfg.list_all_sprites[0].fir_amount}'
                                              f'IOLOK and {cfg.list_all_sprites[0].palm_amount} PALMAS',
                                              24,
                                              960, 370, cfg.font_interface_p, "yellow")
            cfg.list_all_sprites[0].draw_text(cfg.screen,
                                              f'You have {cfg.list_all_sprites[0].utilities[0]} apples, {cfg.list_all_sprites[0].utilities[1]} '
                                              f'shishkas, {cfg.list_all_sprites[0].utilities[2]} coconuts left',
                                              24,
                                              960, 440, cfg.font_interface_p, "green")

            cfg.list_all_sprites[0].draw_text(cfg.screen,
                                              f'You have destroyed {cfg.list_all_sprites[0].kills} monsters',
                                              30,
                                              960, 510, cfg.font_interface_p, "blue")
            cfg.list_all_sprites[0].draw_text(cfg.screen,
                                              'Press Esc to exit the menu',
                                              20,
                                              960, 680, cfg.font_interface_p, "purple")
        pygame.display.flip()


def win_game():
    continue_flag = False
    while cfg.win_game_active_flag:
        cfg.screen.blit(img.vic_bg, (0, 0))
        cfg.list_all_sprites[0].draw_text(cfg.screen, 'You have become the real god of the axe!', 40, 960, 700,
                                          cfg.font_interface_p,
                                          "green")
        cfg.list_all_sprites[0].draw_text(cfg.screen, 'Press space to continue...', 30, 960, 1000, cfg.font_interface_p,
                                          "green")
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                continue_flag = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                cfg.win_game_active_flag = False
                cfg.menu_active_flag = True
                classes.del_units()
        if continue_flag:
            cfg.screen.fill("grey")
            cfg.list_all_sprites[0].draw_text(cfg.screen,
                                              f'You have mastered only {cfg.list_all_sprites[0].progress}%',
                                              30,
                                              960, 200, cfg.font_interface_p, "red")
            cfg.list_all_sprites[0].draw_text(cfg.screen,
                                              f'You have wasted {int(cfg.in_game_time / 1000)} seconds your life',
                                              24,
                                              960, 300, cfg.font_interface_p, "orange")
            cfg.list_all_sprites[0].draw_text(cfg.screen,
                                              f'You have cut down {cfg.list_all_sprites[0].oak_amount} DUBOV and {cfg.list_all_sprites[0].fir_amount}  IOLOK',
                                              24,
                                              960, 370, cfg.font_interface_p, "yellow")
            cfg.list_all_sprites[0].draw_text(cfg.screen,
                                              f'You have {cfg.list_all_sprites[0].utilities[0]} apples, {cfg.list_all_sprites[0].utilities[1]} shishkas, {cfg.list_all_sprites[0].utilities[2]} coconuts left',
                                              24,
                                              960, 440, cfg.font_interface_p, "green")

            cfg.list_all_sprites[0].draw_text(cfg.screen,
                                              f'You have destroyed {cfg.list_all_sprites[0].kills} monsters',
                                              30,
                                              960, 510, cfg.font_interface_p, "blue")
            cfg.list_all_sprites[0].draw_text(cfg.screen,
                                              'Press Esc to exit the menu',
                                              20,
                                              960, 680, cfg.font_interface_p, "purple")
        pygame.display.flip()


def menu():
    # sounds.play_music.stop()
    # if cfg.menu_sound_flag:
    # pygame.mixer.music.play(-1)
    #     cfg.menu_sound_flag = False   флаг для музыки больше не нужен (ушли от этой концепции)

    pygame.mixer.music.play(-1)  # запуск фоновой музыки
    # timer = 0
    play_delay_start, options_delay_start, quit_delay_start = 0, 0, 0
    while cfg.menu_active_flag:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        cfg.clock.tick(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        cfg.screen.blit(img.menu_bg, (0, 0))
        cfg.screen.blit(cfg.menu_title, cfg.menu_title_rect)
        # условие нажатия ЛКМ в области кнопки play


        if (cfg.options_rect.left <= mouse[0] <= cfg.options_rect.right) and (
                cfg.options_rect.top <= mouse[1] <= cfg.options_rect.bottom) and click[0]:
            cfg.screen.blit(img.active_options, cfg.active_options_rect)
            if options_delay_start > 2:
                sounds.click.play()
                options_delay_start = 0
                time.sleep(0.2)
                options_menu()
            options_delay_start += 1
        else:
            cfg.screen.blit(img.options, cfg.options_rect)

        if (cfg.quit_rect.left <= mouse[0] <= cfg.quit_rect.right) and (
                cfg.quit_rect.top <= mouse[1] <= cfg.quit_rect.bottom) and \
                click[0]:
            cfg.screen.blit(img.active_quite, cfg.active_quite_rect)
            if quit_delay_start > 2:
                sounds.click.play()
                quit_delay_start = 0
                time.sleep(0.2)
                quit()
            quit_delay_start += 1
        else:
            cfg.screen.blit(img.quite, cfg.quit_rect)

        if (cfg.play_rect.left <= mouse[0] <= cfg.play_rect.right) and (
                cfg.play_rect.top <= mouse[1] <= cfg.play_rect.bottom) and \
                click[0]:
            # помещаем иконку active_play_transform в область active_play_rect
            cfg.screen.blit(cfg.active_play_transform, cfg.active_play_rect)
            cfg.play_game_active_flag = True
            # pygame.mixer.music.stop() # фоновая музыка не отключается при нажатии на play
            if play_delay_start > 2:
                sounds.click.play()
                play_delay_start = 0
                time.sleep(0.2)
                cfg.in_game_time = 0
                # play_game()
                difficult_menu()
            play_delay_start += 1
        else:
            cfg.screen.blit(cfg.play_transform, cfg.play_rect)
        pygame.display.flip()



def difficult_menu():
    active_flag_diff = True

    easy_delay_start, medium_delay_start, hard_delay_start = 0, 0, 0

    while active_flag_diff:
        cfg.screen.blit(img.vic_bg, (0, 0))
        cfg.screen.blit(cfg.menu_title, cfg.menu_title_rect)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        cfg.clock.tick(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    active_flag_diff = False
        if (cfg.play_rect.left <= mouse[0] <= cfg.play_rect.right) and (
                cfg.play_rect.top <= mouse[1] <= cfg.play_rect.bottom) and \
                click[0]:
            cfg.screen.blit(img.easy_active, cfg.active_easy_rect)
            if easy_delay_start > 2:
                sounds.click.play()
                easy_delay_start = 0
                time.sleep(0.2)
                cfg.in_game_time = 0
                cfg.difficuilt_flag = 0
                cfg.play_game_active_flag = True
                active_flag_diff = False
                cfg.menu_active_flag = False
            easy_delay_start += 1
        else:
            cfg.screen.blit(img.easy, cfg.easy_rect)

        if (cfg.options_rect.left <= mouse[0] <= cfg.options_rect.right) and (
                cfg.options_rect.top <= mouse[1] <= cfg.options_rect.bottom) and click[0]:
            cfg.screen.blit(cfg.medium_active_transform, cfg.active_medium_rect)
            if medium_delay_start > 2:
                sounds.click.play()
                medium_delay_start = 0
                time.sleep(0.2)
                cfg.in_game_time = 0
                cfg.difficuilt_flag = 1
                cfg.play_game_active_flag = True
                active_flag_diff = False
                cfg.menu_active_flag = False
            medium_delay_start += 1
        else:
            cfg.screen.blit(cfg.medium_transform, cfg.medium_rect)

        if (cfg.quit_rect.left <= mouse[0] <= cfg.quit_rect.right) and (
                cfg.quit_rect.top <= mouse[1] <= cfg.quit_rect.bottom) and \
                click[0]:
            cfg.screen.blit(img.hard_active, cfg.active_hard_rect)
            if hard_delay_start > 2:
                sounds.click.play()
                hard_delay_start = 0
                cfg.in_game_time = 0
                cfg.difficuilt_flag = 2
                cfg.play_game_active_flag = True
                active_flag_diff = False
                cfg.menu_active_flag = False
            hard_delay_start += 1
        else:
            cfg.screen.blit(img.hard, cfg.hard_rect)
        pygame.display.flip()


def pause():
    play_delay_start, options_delay_start, quit_delay_start = 0, 0, 0
    while cfg.pause_active_flag:
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
            if play_delay_start > 2:
                sounds.click.play()
                play_delay_start = 0
                time.sleep(0.2)
                cfg.start_game_sound_flag = False
                cfg.pause_active_flag = False
            play_delay_start += 1
        else:
            cfg.screen.blit(img.continue_, cfg.continue_rect)

        if (cfg.Options_rect.left <= mouse[0] <= cfg.Options_rect.right) and (
                cfg.Options_rect.top <= mouse[1] <= cfg.Options_rect.bottom) and click[0]:

            cfg.screen.blit(img.Options_active, cfg.Options_active_rect)

            if options_delay_start > 2:
                sounds.click.play()
                options_delay_start = 0
                time.sleep(0.2)
                options_game()
            options_delay_start += 1

        else:
            cfg.screen.blit(img.Options, cfg.Options_rect)

        if (cfg.menu_rect.left <= mouse[0] <= cfg.menu_rect.right) and (
                cfg.menu_rect.top <= mouse[1] <= cfg.menu_rect.bottom) and \
                click[0]:
            cfg.screen.blit(img.menu_active, cfg.menu_active_rect)
            if quit_delay_start > 2:
                sounds.click.play()
                quit_delay_start = 0
                time.sleep(0.2)

                cfg.start_game_sound_flag = True
                cfg.pause_active_flag = False
                cfg.menu_active_flag = True
                cfg.play_game_active_flag = False
                classes.del_units()
            quit_delay_start += 1
        else:
            cfg.screen.blit(img.menu, cfg.menu_rect)
        pygame.display.flip()


def options_menu():
    active_flag = True  # Флаг активного состояния options_menu
    while active_flag:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        cfg.clock.tick(200)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # sounds.play_music.stop()
                    # pygame.mixer.music.unpause()
                    active_flag = False
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
                sounds.hit_monster.set_volume(sounds.volume_sounds)
                sounds.agr_monster.set_volume(sounds.volume_sounds)
                sounds.falling_tree.set_volume(sounds.volume_sounds)
                sounds.eat_apple.set_volume(sounds.volume_sounds)
                sounds.drink_coconut.set_volume(sounds.volume_sounds)
                sounds.take_coin.set_volume(sounds.volume_sounds)
                sounds.take_dmg1.set_volume(sounds.volume_sounds)
                sounds.take_dmg2.set_volume(sounds.volume_sounds)
                sounds.take_dmg3.set_volume(sounds.volume_sounds)
                sounds.last_hit.set_volume(sounds.volume_sounds)

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
    active_flag = True  # Флаг активного состояния options_game
    while active_flag:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        cfg.clock.tick(200)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    active_flag = False

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
                sounds.hit_monster.set_volume(sounds.volume_sounds)
                sounds.agr_monster.set_volume(sounds.volume_sounds)
                sounds.falling_tree.set_volume(sounds.volume_sounds)
                sounds.eat_apple.set_volume(sounds.volume_sounds)
                sounds.drink_coconut.set_volume(sounds.volume_sounds)
                sounds.take_coin.set_volume(sounds.volume_sounds)
                sounds.take_dmg1.set_volume(sounds.volume_sounds)
                sounds.take_dmg2.set_volume(sounds.volume_sounds)
                sounds.take_dmg3.set_volume(sounds.volume_sounds)
                sounds.last_hit.set_volume(sounds.volume_sounds)

        cfg.screen.blit(cfg.tablet_transform, cfg.tablet_rect)
        cfg.screen.blit(img.music_label, cfg.music_label_rect)
        cfg.screen.blit(img.scale1, cfg.scale1_rect)
        cfg.screen.blit(img.sounds_label, cfg.sounds_label_rect)
        cfg.screen.blit(img.scale2, cfg.scale2_rect)
        cfg.screen.blit(img.point1, cfg.point1_rect)
        cfg.screen.blit(img.point2, cfg.point2_rect)

        pygame.display.flip()


def tree_generator(n):
    count = 0
    while count < n:
        cfg.tree_add_flag = True
        x = random.randint(-1820, 3640)
        y = random.randint(-1030, 1900)
        if abs(x - cfg.all_sprites.sprites()[1].rect.center[0]) < cfg.delta + 100 and abs(
                y - cfg.all_sprites.sprites()[1].rect.center[1]) < cfg.delta + 100:
            cfg.tree_add_flag = False
        if cfg.tree_add_flag:
            for i in range(count):
                if abs(cfg.tree_list_x[i] - x) < cfg.delta and abs(cfg.tree_list_y[i] - y) < cfg.delta:
                    cfg.tree_add_flag = False

        if cfg.tree_add_flag:
            cfg.tree_list_x.append(x)
            cfg.tree_list_y.append(y)
            count += 1

    cfg.trees1 = [classes.Dub(f'Дуб{i}', 500, cfg.tree_list_x[i], cfg.tree_list_y[i], 5) for i in range(0, n - 2, 3)]
    cfg.trees2 = [classes.Elka(f'Елка{i}', 1000, cfg.tree_list_x[i], cfg.tree_list_y[i], 10) for i in
                  range(1, n - 2, 3)]
    cfg.trees3 = [classes.Palma(f'Пальма{i}', 2000, cfg.tree_list_x[i], cfg.tree_list_y[i], 20) for i in
                  range(2, n - 3, 3)]

    for elem in cfg.trees1:
        cfg.all_sprites.add(elem)
        cfg.trees_rects_left.append(elem.line_left)
        cfg.trees_rects_right.append(elem.line_right)
        cfg.trees_rects_top.append(elem.line_top)
        cfg.trees_rects_bottom.append(elem.line_bottom)

    for elem in cfg.trees2:
        cfg.all_sprites.add(elem)
        cfg.trees_rects_left.append(elem.line_left)
        cfg.trees_rects_right.append(elem.line_right)
        cfg.trees_rects_top.append(elem.line_top)
        cfg.trees_rects_bottom.append(elem.line_bottom)

    for elem in cfg.trees3:
        cfg.all_sprites.add(elem)
        cfg.trees_rects_left.append(elem.line_left)
        cfg.trees_rects_right.append(elem.line_right)
        cfg.trees_rects_top.append(elem.line_top)
        cfg.trees_rects_bottom.append(elem.line_bottom)


def monster_generator(n):
    count = 0
    while count < n:
        cfg.monster_add_flag = True
        x = random.randint(-1870, 3740)
        y = random.randint(-1030, 2000)
        if abs(x - cfg.all_sprites.sprites()[1].rect.center[0]) < cfg.delta and abs(
                y - cfg.all_sprites.sprites()[1].rect.center[1]) < cfg.delta:
            cfg.monster_add_flag = False
        if cfg.monster_add_flag:
            for i in range(count):
                if (abs(cfg.monster_list_x[i] - x) < cfg.delta_monsters and abs(
                        cfg.monster_list_y[i] - y) < cfg.delta_monsters) and (abs(
                    cfg.monster_list_x[i] - cfg.list_all_sprites[0].rect.x) < cfg.delta_hero and abs(
                    cfg.monster_list_y[i] - cfg.list_all_sprites[0].rect.y) < cfg.delta_hero):
                    cfg.monster_add_flag = False
        if cfg.monster_add_flag:
            cfg.monster_list_x.append(x)
            cfg.monster_list_y.append(y)
            count += 1

    if cfg.difficuilt_flag == 2:
        cfg.monsterList = [mobs.Monster(f'Минотавр{i}', 500, cfg.monster_list_x[i], cfg.monster_list_y[i], 500, 20)
                           for i in range(n)]
    elif cfg.difficuilt_flag == 1:
        cfg.monsterList = [mobs.Monster(f'Минотавр{i}', 400, cfg.monster_list_x[i], cfg.monster_list_y[i], 400, 15)
                           for i in range(n // 2)]
    elif cfg.difficuilt_flag == 0:
        cfg.monsterList = [mobs.Monster(f'Минотавр{i}', 300, cfg.monster_list_x[i], cfg.monster_list_y[i], 300, 10)
                           for i in range(n // 3)]

    for elem in cfg.monsterList:
        cfg.all_sprites.add(elem)


def workshop():
    while cfg.workshop_active_flag:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        cfg.screen.blit(img.workshop_tablet, cfg.workshop_tablet_rect)
        cfg.screen.blit(img.market_label, cfg.market_label_rect)
        cfg.screen.blit(img.upgrade_label, cfg.upgrade_label_rect)
        cfg.screen.blit(img.trade_label, cfg.trade_label_rect)

        if (cfg.upgrade_label_rect.left <= mouse[0] <= cfg.upgrade_label_rect.right) and (
                cfg.upgrade_label_rect.top <= mouse[1] <= cfg.upgrade_label_rect.bottom):
            cfg.screen.blit(img.upgrade_label_active, cfg.upgrade_label_rect)
            if click[0]:
                sounds.click.play()
                time.sleep(0.2)
                cfg.upgrade_active_flag = True
                upgrade()

        if (cfg.trade_label_rect.left <= mouse[0] <= cfg.trade_label_rect.right) and (
                cfg.trade_label_rect.top <= mouse[1] <= cfg.trade_label_rect.bottom):
            cfg.screen.blit(img.trade_label_active, cfg.trade_label_rect)
            if click[0]:
                sounds.click.play()
                time.sleep(0.2)
                cfg.trade_active_flag = True
                trade()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    cfg.workshop_active_flag = False
        pygame.display.flip()


def upgrade():
    mouse_up_flag = False
    while cfg.upgrade_active_flag:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    cfg.upgrade_active_flag = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_up_flag = False
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    mouse_up_flag = True

        cfg.screen.blit(cfg.upgrade_description_1, cfg.upgrade_description_1_rect)
        cfg.screen.blit(cfg.upgrade_description_2, cfg.upgrade_description_2_rect)
        cfg.screen.blit(cfg.upgrade_description_3, cfg.upgrade_description_3_rect)
        cfg.list_all_sprites[0].draw_text(cfg.screen, f"Balance: {(cfg.list_all_sprites[0].coins)} coins", 30, 980, 330,
                                          cfg.upgrade_font_p, "green")
        cfg.screen.blit(img.power, cfg.power_rect)
        cfg.screen.blit(cfg.power_description, cfg.power_description_rect)
        cfg.screen.blit(img.list_levels_scale_power[cfg.current_power_level], cfg.leveling_scale_power_rect)
        cfg.screen.blit(cfg.cost_power, cfg.cost_power_rect)

        cfg.screen.blit(img.health, cfg.health_rect)
        cfg.screen.blit(cfg.health_description, cfg.health_description_rect)
        cfg.screen.blit(img.list_levels_scale_health[cfg.current_health_level], cfg.leveling_scale_health_rect)
        cfg.screen.blit(cfg.cost_health, cfg.cost_health_rect)

        cfg.screen.blit(img.stamina, cfg.stamina_rect)
        cfg.screen.blit(cfg.stamina_description, cfg.stamina_description_rect)
        cfg.screen.blit(img.list_levels_scale_stamina[cfg.current_stamina_level], cfg.leveling_scale_stamina_rect)
        cfg.screen.blit(cfg.cost_stamina, cfg.cost_stamina_rect)

        if cfg.list_all_sprites[0].coins >= cfg.level_cost_list[cfg.current_power_level]:
            cfg.screen.blit(img.buy_active, cfg.buy_power_rect)

            if (cfg.buy_power_rect.left <= mouse[0] <= cfg.buy_power_rect.right) and (
                    cfg.buy_power_rect.top <= mouse[1] <= cfg.buy_power_rect.bottom) and click[0]:
                if mouse_up_flag and cfg.current_power_level < 5:
                    sounds.click.play()
                    time.sleep(0.2)
                    cfg.screen.blit(img.workshop_tablet, cfg.workshop_tablet_rect)
                    cfg.screen.blit(img.market_label, cfg.market_label_rect)
                    cfg.screen.blit(img.upgrade_label_active, cfg.upgrade_label_rect)
                    cfg.screen.blit(img.trade_label, cfg.trade_label_rect)
                    cfg.current_power_level += 1
                    cfg.list_all_sprites[0].coins -= cfg.level_cost_list[cfg.current_power_level]

        else:
            cfg.screen.blit(img.buy, cfg.buy_power_rect)

        if cfg.list_all_sprites[0].coins >= cfg.level_cost_list[cfg.current_health_level]:
            cfg.screen.blit(img.buy_active, cfg.buy_health_rect)

            if (cfg.buy_health_rect.left <= mouse[0] <= cfg.buy_health_rect.right) and (
                    cfg.buy_health_rect.top <= mouse[1] <= cfg.buy_health_rect.bottom) and click[0]:
                if mouse_up_flag and cfg.current_health_level < 5:
                    sounds.click.play()
                    time.sleep(0.2)
                    cfg.screen.blit(img.workshop_tablet, cfg.workshop_tablet_rect)
                    cfg.screen.blit(img.market_label, cfg.market_label_rect)
                    cfg.screen.blit(img.upgrade_label_active, cfg.upgrade_label_rect)
                    cfg.screen.blit(img.trade_label, cfg.trade_label_rect)
                    cfg.current_health_level += 1
                    cfg.list_all_sprites[0].coins -= cfg.level_cost_list[cfg.current_health_level]

        else:
            cfg.screen.blit(img.buy, cfg.buy_health_rect)

        if cfg.list_all_sprites[0].coins >= cfg.level_cost_list[cfg.current_stamina_level]:
            cfg.screen.blit(img.buy_active, cfg.buy_stamina_rect)

            if (cfg.buy_stamina_rect.left <= mouse[0] <= cfg.buy_stamina_rect.right) and (
                    cfg.buy_stamina_rect.top <= mouse[1] <= cfg.buy_stamina_rect.bottom) and click[0]:
                if mouse_up_flag and cfg.current_stamina_level < 5:
                    sounds.click.play()
                    time.sleep(0.2)
                    cfg.screen.blit(img.workshop_tablet, cfg.workshop_tablet_rect)
                    cfg.screen.blit(img.market_label, cfg.market_label_rect)
                    cfg.screen.blit(img.upgrade_label_active, cfg.upgrade_label_rect)
                    cfg.screen.blit(img.trade_label, cfg.trade_label_rect)
                    cfg.current_stamina_level += 1
                    cfg.list_all_sprites[0].coins -= cfg.level_cost_list[cfg.current_stamina_level]
        else:
            cfg.screen.blit(img.buy, cfg.buy_stamina_rect)

        pygame.display.flip()


def trade():
    mouse_up_flag = False
    while cfg.trade_active_flag:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    cfg.trade_active_flag = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_up_flag = False
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    mouse_up_flag = True

        cfg.screen.blit(img.workshop_tablet, cfg.workshop_tablet_rect)
        cfg.screen.blit(img.trade_label_active, cfg.trade_label_rect)
        cfg.screen.blit(img.upgrade_label, cfg.upgrade_label_rect)
        cfg.screen.blit(img.market_label, cfg.market_label_rect)


        cfg.list_all_sprites[0].draw_text(cfg.screen, "75", 50, 790, 405,
                                          cfg.upgrade_font_p, "black")
        cfg.list_all_sprites[0].draw_text(cfg.screen, "25", 50, 1080, 705,
                                          cfg.upgrade_font_p, "black")
        cfg.screen.blit(img.wood_icon, (1125, 710))
        cfg.list_all_sprites[0].draw_text(cfg.screen, f'{(cfg.list_all_sprites[0].utilities[0])}', 30, 500, 750,
                                          cfg.font_interface_p,
                                          "white")
        cfg.list_all_sprites[0].draw_text(cfg.screen, f'{(cfg.list_all_sprites[0].utilities[1])}', 30, 500, 660,
                                          cfg.font_interface_p,
                                          "white")
        cfg.list_all_sprites[0].draw_text(cfg.screen, f'{(cfg.list_all_sprites[0].utilities[2])}', 30, 500, 580,
                                          cfg.font_interface_p,
                                          "white")
        cfg.list_all_sprites[0].draw_text(cfg.screen, f'{(cfg.list_all_sprites[0].wood_amount)}', 30, 500, 500,
                                          cfg.font_interface_p,
                                          "white")
        cfg.list_all_sprites[0].draw_text(cfg.screen, f'{(cfg.list_all_sprites[0].coins)}', 30, 500, 420,
                                          cfg.font_interface_p,
                                          "white")
        cfg.screen.blit(img.apple_icon, (370, 740))
        cfg.screen.blit(img.shishka_icon, (370, 650))
        cfg.screen.blit(img.coconut_icon, (370, 570))
        cfg.screen.blit(img.wood_icon, (370, 490))
        cfg.screen.blit(img.coin_icon, (370, 410))
        cfg.screen.blit(img.coin_icon, (835, 410))


        if cfg.list_all_sprites[0].coins >= 10:
            cfg.screen.blit(img.trade_arrow_green, (935, 390))
            if (cfg.trade_arrow_rect_apple.left <= mouse[0] <= cfg.trade_arrow_rect_apple.right) and (
                    cfg.trade_arrow_rect_apple.top <= mouse[1] <= cfg.trade_arrow_rect_apple.bottom) and click[
                0] and mouse_up_flag:
                sounds.click.play()
                time.sleep(0.2)
                cfg.list_all_sprites[0].utilities[0] += 1
                cfg.list_all_sprites[0].coins -= 10
        else:
            cfg.screen.blit(img.trade_arrow_red, (935, 390))
        cfg.list_all_sprites[0].draw_text(cfg.screen, "1", 50, 1080, 405,
                                          cfg.upgrade_font_p, "black")
        cfg.screen.blit(img.apple_icon, (1125, 410))


        cfg.list_all_sprites[0].draw_text(cfg.screen, "175", 50, 790, 505,
                                          cfg.upgrade_font_p, "black")
        cfg.screen.blit(img.coin_icon, (835, 510))
        if cfg.list_all_sprites[0].coins >= 10:
            cfg.screen.blit(img.trade_arrow_green, (935, 490))
            if (cfg.trade_arrow_rect_shishka.left <= mouse[0] <= cfg.trade_arrow_rect_shishka.right) and (
                    cfg.trade_arrow_rect_shishka.top <= mouse[
                1] <= cfg.trade_arrow_rect_shishka.bottom) and not mouse_up_flag:
                sounds.click.play()
                time.sleep(0.2)
                cfg.list_all_sprites[0].utilities[1] += 1
                cfg.list_all_sprites[0].coins -= 10

        else:
            cfg.screen.blit(img.trade_arrow_red, (935, 490))
        cfg.list_all_sprites[0].draw_text(cfg.screen, "1", 50, 1080, 505,
                                          cfg.upgrade_font_p, "black")
        cfg.screen.blit(img.shishka_icon, (1125, 510))


        cfg.list_all_sprites[0].draw_text(cfg.screen, "275", 50, 790, 605,
                                          cfg.upgrade_font_p, "black")
        cfg.screen.blit(img.coin_icon, (835, 610))
        if cfg.list_all_sprites[0].coins >= 10:
            cfg.screen.blit(img.trade_arrow_green, (935, 590))
            if (cfg.trade_arrow_rect_coconut.left <= mouse[0] <= cfg.trade_arrow_rect_coconut.right) and (
                    cfg.trade_arrow_rect_coconut.top <= mouse[
                1] <= cfg.trade_arrow_rect_coconut.bottom) and not mouse_up_flag:
                sounds.click.play()
                time.sleep(0.2)
                cfg.list_all_sprites[0].utilities[2] += 1
                cfg.list_all_sprites[0].coins -= 10

        else:
            cfg.screen.blit(img.trade_arrow_red, (935, 590))
        cfg.list_all_sprites[0].draw_text(cfg.screen, "1", 50, 1080, 605,
                                          cfg.upgrade_font_p, "black")
        cfg.screen.blit(img.coconut_icon, (1125, 610))


        cfg.list_all_sprites[0].draw_text(cfg.screen, "100", 50, 790, 705,
                                          cfg.upgrade_font_p, "black")
        cfg.screen.blit(img.coin_icon, (835, 710))
        if cfg.list_all_sprites[0].coins >= 10:
            cfg.screen.blit(img.trade_arrow_green, (935, 690))
            if (cfg.trade_arrow_rect_wood.left <= mouse[0] <= cfg.trade_arrow_rect_wood.right) and (
                    cfg.trade_arrow_rect_wood.top <= mouse[
                1] <= cfg.trade_arrow_rect_wood.bottom) and not mouse_up_flag:
                sounds.click.play()
                time.sleep(0.2)
                cfg.list_all_sprites[0].wood_amount += 25
                cfg.list_all_sprites[0].coins -= 10
                cfg.list_all_sprites[0].draw_info_bar(cfg.screen, 0, 1065, cfg.list_all_sprites[0].wood_amount, "brown",
                                                      "yellow", "black", 500,
                                                      1920, 15)
                cfg.list_all_sprites[0].progress = cfg.list_all_sprites[0].wood_amount * 100 / cfg.goal
                cfg.screen.blit(img.trade_patch, (900, 965))
                cfg.list_all_sprites[0].draw_text(cfg.screen, f'{int(cfg.list_all_sprites[0].progress)} %', 18, 960,
                                                  1040,
                                                  cfg.font_interface_p,
                                                  "red")

        else:
            cfg.screen.blit(img.trade_arrow_red, (935, 690))
        cfg.list_all_sprites[0].draw_text(cfg.screen, "25", 50, 1080, 705,
                                          cfg.upgrade_font_p, "black")
        cfg.screen.blit(img.wood_icon, (1125, 710))
        pygame.display.flip()

