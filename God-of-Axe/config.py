import pygame

pygame.init()

WIDTH = 1920
HEIGHT = 1080
FPS = 60

clock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
size = screen.get_size()

# Иконка игры--------------------------------------------------------------------------------------
icon = pygame.image.load('Images/icon_axe.png').convert_alpha()

# Все кнопки меню ---------------------------------------------------------------------------------
# Кнопка Play -------------------------------------------------------------------------------------
play = pygame.image.load('Images/play.jpg').convert_alpha()
play_transform = pygame.transform.scale(play, (270, 126))
play_rect = play_transform.get_rect()
play_rect.center = (size[0] // 2, 215)

# Нажатая нопка Play ------------------------------------------------------------------------------
active_play = pygame.image.load('Images/play_active.jpg').convert_alpha()
active_play_transform = pygame.transform.scale(active_play, (270, 114))
active_play_rect = active_play_transform.get_rect()
active_play_rect.center = (size[0] // 2, 221)

# Кнопка Options ----------------------------------------------------------------------------------
options = pygame.image.load('Images/options.jpg').convert_alpha()
options_rect = options.get_rect()
options_rect.center = (size[0] // 2, 350)

# Нажатая кнопка Options --------------------------------------------------------------------------
active_options = pygame.image.load('Images/options_active.jpg').convert_alpha()
active_options_rect = active_options.get_rect()
active_options_rect.center = (size[0] // 2, 356)

# Кнопка Quite ------------------------------------------------------------------------------------
quite = pygame.image.load('Images/quite.jpg').convert_alpha()
quite_rect = quite.get_rect()
quite_rect.center = (size[0] // 2, 476)

# Нажатая кнопка Quite ----------------------------------------------------------------------------
active_quite = pygame.image.load('Images/quite_active.jpg').convert_alpha()
active_quite_rect = active_quite.get_rect()
active_quite_rect.center = (size[0] // 2, 482)

# Установка шрифта --------------------------------------------------------------------------------
my_font = pygame.font.Font('Fonts/Jfwildwood-ldYZ.ttf', 100)

# Фон меню ----------------------------------------------------------------------------------------
menu_bg = pygame.image.load('Images/bg_menu.jpg').convert_alpha()


game_bg = pygame.image.load('Images/game_field.png').convert_alpha()
# Надпись God of Axe в Меню -----------------------------------------------------------------------
menu_title = my_font.render("God of Axe", True, (224, 153, 9))
menu_title_rect = menu_title.get_rect()
menu_title_rect.bottomleft = (0, size[1])

menu_music = pygame.mixer.music.load(r'Music/Piano Fantasia - Song for Denise (Wide Walking Extended Version) (mp3cut.net).mp3')

click = pygame.mixer.Sound(r'Music\zipclick.flac')
click.set_volume(0.3)