import pygame
import config
import time
import func

# pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()

FPS = 60
info = pygame.display.Info()
size = (info.current_w, info.current_h)

screen = pygame.display.set_mode(size)
current_size = screen.get_size()
last_size = current_size

pygame.display.set_caption("God of Axe")
clock = pygame.time.Clock()

# ---------------------------- Иконка игры -----------------------------
icon = pygame.image.load('images/icon_axe.png').convert_alpha()
pygame.display.set_icon(icon)

my_font = pygame.font.Font('fonts/Jfwildwood-ldYZ.ttf', 100)

# -------------------------------- Меню --------------------------------
play = pygame.image.load('images/play.jpg').convert_alpha()
play_transform = pygame.transform.scale(play, (270, 126))
play_rect = play_transform.get_rect()
play_rect.center = (size[0] // 2, 215)

active_play = pygame.image.load('images/play_active.jpg').convert_alpha()
active_play_transform = pygame.transform.scale(active_play, (270, 114))
active_play_rect = active_play_transform.get_rect()
active_play_rect.center = (size[0] // 2, 221)

options = pygame.image.load('images/options.jpg').convert_alpha()
options_rect = options.get_rect()
options_rect.center = (size[0] // 2, 350)

active_options = pygame.image.load('images/options_active.jpg').convert_alpha()
active_options_rect = active_options.get_rect()
active_options_rect.center = (size[0] // 2, 356)

quite = pygame.image.load('images/quite.jpg').convert_alpha()
quite_rect = quite.get_rect()
quite_rect.center = (size[0] // 2, 476)

active_quite = pygame.image.load('images/quite_active.jpg').convert_alpha()
active_quite_rect = active_quite.get_rect()
active_quite_rect.center = (size[0] // 2, 482)

menu_bg = pygame.image.load('images/final_bg_menu.jpg').convert_alpha()
menu_title = my_font.render("God of Axe", True, (224, 153, 9))
menu_title_rect = menu_title.get_rect()
menu_title_rect.bottomleft = (0, size[1])


# ----------------------------------------------------------------------
def start_game():
    config.is_menu = False
    while config.running:
        config.clock.tick(config.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                config.running = False
                quit()
        screen.fill((255, 22, 123))
        pygame.display.flip()


def menu():
    is_menu = True
    music = pygame.mixer.Sound(r'Music\tick.mp3')
    start, start1 = 0, 0
    while is_menu:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                config.running = False
                quit()

        screen.blit(menu_bg, (0, 0))
        screen.blit(menu_title, menu_title_rect)

        if (play_rect.left <= mouse[0] <= play_rect.right) and (play_rect.top <= mouse[1] <= play_rect.bottom) and \
                click[0]:
            if time.time() - start > 1:
                start = time.time()
                music.play()
            screen.blit(active_play_transform, active_play_rect)

        else:
            screen.blit(play_transform, play_rect)

        if (options_rect.left <= mouse[0] <= options_rect.right) and (
                options_rect.top <= mouse[1] <= options_rect.bottom) and click[0]:
            if time.time() - start > 1:
                start = time.time()
                music.play()
            screen.blit(active_options, active_options_rect)

        else:
            screen.blit(options, options_rect)

        if (quite_rect.left <= mouse[0] <= quite_rect.right) and (quite_rect.top <= mouse[1] <= quite_rect.bottom) and \
                click[0]:
            screen.blit(active_quite, active_quite_rect)
            if time.time() - start > 1:
                start = time.time()
                music.play()
                time.sleep(1)
                if time.time() - start1 > 5:
                    start1 = time.time()
                    start_game()

        else:
            screen.blit(quite, quite_rect)
        pygame.display.flip()


menu()
