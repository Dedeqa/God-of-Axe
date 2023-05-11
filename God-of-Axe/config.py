import pygame

pygame.init()
WIDTH = 1920
HEIGHT = 1080
FPS = 60
running = True
is_menu = True
clock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
current_size = screen.get_size()
last_size = current_size
info = pygame.display.Info()
size = (info.current_w, info.current_h)
screen = pygame.display.set_mode(size)

icon = pygame.image.load('Images/icon_axe.png').convert_alpha()

play = pygame.image.load('Images/play.jpg').convert_alpha()
play_transform = pygame.transform.scale(play, (270, 126))
play_rect = play_transform.get_rect()
play_rect.center = (size[0] // 2, 215)

active_play = pygame.image.load('Images/play_active.jpg').convert_alpha()
active_play_transform = pygame.transform.scale(active_play, (270, 114))
active_play_rect = active_play_transform.get_rect()
active_play_rect.center = (size[0] // 2, 221)

options = pygame.image.load('Images/options.jpg').convert_alpha()
options_rect = options.get_rect()
options_rect.center = (size[0] // 2, 350)

active_options = pygame.image.load('Images/options_active.jpg').convert_alpha()
active_options_rect = active_options.get_rect()
active_options_rect.center = (size[0] // 2, 356)

quite = pygame.image.load('Images/quite.jpg').convert_alpha()
quite_rect = quite.get_rect()
quite_rect.center = (size[0] // 2, 476)

active_quite = pygame.image.load('Images/quite.jpg').convert_alpha()
active_quite_rect = active_quite.get_rect()
active_quite_rect.center = (size[0] // 2, 482)

my_font = pygame.font.Font('Fonts/Jfwildwood-ldYZ.ttf', 100)
menu_bg = pygame.image.load('Images/final_bg_menu.jpg').convert_alpha()
menu_title = my_font.render("God of Axe", True, (224, 153, 9))
menu_title_rect = menu_title.get_rect()
menu_title_rect.bottomleft = (0, size[1])


