import pygame

pygame.init()

WIDTH = 1920
HEIGHT = 1080
FPS = 120

clock = pygame.time.Clock()

menu_flag = True
start_game_flag = True

screen = pygame.display.set_mode((WIDTH, HEIGHT))
size = screen.get_size()

# Иконка игры--------------------------------------------------------------------------------------
icon = pygame.image.load('Images/icon_axe.png').convert_alpha()

# Все кнопки меню ---------------------------------------------------------------------------------
# Кнопка Play -------------------------------------------------------------------------------------
play = pygame.image.load('Images/play.png').convert_alpha()
play_transform = pygame.transform.scale(play, (270, 126))
play_rect = play_transform.get_rect()
play_rect.center = (size[0] // 2, 215)

# Нажатая нопка Play ------------------------------------------------------------------------------
active_play = pygame.image.load('Images/play_active.png').convert_alpha()
active_play_transform = pygame.transform.scale(active_play, (270, 114))
active_play_rect = active_play_transform.get_rect()
active_play_rect.center = (size[0] // 2, 221)

# Кнопка Options ----------------------------------------------------------------------------------
options = pygame.image.load('Images/options.png').convert_alpha()
options_rect = options.get_rect()
options_rect.center = (size[0] // 2, 350)

# Нажатая кнопка Options --------------------------------------------------------------------------
active_options = pygame.image.load('Images/options_active.png').convert_alpha()
active_options_rect = active_options.get_rect()
active_options_rect.center = (size[0] // 2, 356)

# Кнопка Quite ------------------------------------------------------------------------------------
quite = pygame.image.load('Images/quite.png').convert_alpha()
quite_rect = quite.get_rect()
quite_rect.center = (size[0] // 2, 476)

# Нажатая кнопка Quite ----------------------------------------------------------------------------
active_quite = pygame.image.load('Images/quite_active.png').convert_alpha()
active_quite_rect = active_quite.get_rect()
active_quite_rect.center = (size[0] // 2, 482)

# Объекты в Options --------------------------------------------------------------------------------
# Tablet (табличка) --------------------------------------------------------------------------------
tablet = pygame.image.load('Images/Tablet.png')
tablet_transform = pygame.transform.scale(tablet, (500, 264))
tablet_rect = tablet_transform.get_rect()
tablet_rect.center = (size[0] // 2, 375)

# Music_label (надпись music) ---------------------------------------------------------------------
music_label = pygame.image.load('Images/music_label.png')
music_label_rect = music_label.get_rect()
music_label_rect.center = (size[0] // 2, 275)

# Scale1 (шкала громкости музыки) -----------------------------------------------------------------
scale1 = pygame.image.load('Images/scale1.png')
scale1_rect = scale1.get_rect()
scale1_rect.center = (size[0] // 2, 335)

# Sounds_label (надпись sounds) -------------------------------------------------------------------
sounds_label = pygame.image.load('Images/sounds_label.png')
sounds_label_rect = sounds_label.get_rect()
sounds_label_rect.center = (size[0] // 2, 395)

# Scale2 (шкала громкости звуков) -----------------------------------------------------------------
scale2 = pygame.image.load('Images/scale2.png')
scale2_rect = scale2.get_rect()
scale2_rect.center = (size[0] // 2, 455)

# Point1 (ползунок изменения громкости музыки) ----------------------------------------------------
point1 = pygame.image.load('Images/point1.png')
point1_rect = point1.get_rect()
point1_rect.center = (scale1_rect.right, scale1_rect.centery)

# Point2 (ползунок изменения громкости звуков) ----------------------------------------------------
point2 = pygame.image.load('Images/point2.png')
point2_rect = point2.get_rect()
point2_rect.center = (scale2_rect.right, scale2_rect.centery)

# -------------------------------------------------------------------------------------------------
# Установка шрифта --------------------------------------------------------------------------------
my_font = pygame.font.Font('Fonts/Jfwildwood-ldYZ.ttf', 100)

# Фон меню ----------------------------------------------------------------------------------------
menu_bg = pygame.image.load('Images/bg_menu.jpg').convert_alpha()
game_bg = pygame.image.load('Images/game_field.png').convert_alpha()

# Надпись God of Axe в Меню -----------------------------------------------------------------------
menu_title = my_font.render("God of Axe", True, (224, 153, 9))
menu_title_rect = menu_title.get_rect()
menu_title_rect.bottomleft = (0, size[1])

# Фоновая музыка для меню -------------------------------------------------------------------------
pygame.mixer.music.load(
    r'Music/Piano Fantasia - Song for Denise (Wide Walking Extended Version).mp3')

# Фоновая музыка для игры -------------------------------------------------------------------------
play_music = pygame.mixer.Sound(r'Music/Bad Piggies Theme - Piano Tutorial.mp3')

# Звук нажатия кнопок меню ------------------------------------------------------------------------
click = pygame.mixer.Sound(r'Music\zipclick.flac')

volume_music = 1.0
volume_sounds = 1.0

# Координаты для перемещения фона------------------------------------------------------------------
bg_x = 0
bg_y = 0

# Кнопки паузы ------------------------------------------------------------------------------------
# Надпись Pause -----------------------------------------------------------------------------------
pause_label = pygame.image.load('Images/pause_label.png')
pause_label_transform = pygame.transform.scale(pause_label, (400, 113))
pause_label_rect = pause_label_transform.get_rect()
pause_label_rect.center = (size[0] // 2, 100)

# Кнопка Continue ---------------------------------------------------------------------------------
continue_ = pygame.image.load('Images/continue.png').convert_alpha()
continue_rect = continue_.get_rect()
continue_rect.center = (size[0] // 2, 300)

# Нажатая кнопка Continue -------------------------------------------------------------------------
continue_active = pygame.image.load('Images/continue_active.png').convert_alpha()
continue_active_rect = continue_active.get_rect()
continue_active_rect.center = (size[0] // 2, 306)

# Кнопка Options ----------------------------------------------------------------------------------
Options = pygame.image.load('Images/options.png').convert_alpha()
Options_rect = Options.get_rect()
Options_rect.center = (size[0] // 2, 426)

# Нажатая кнопка Options --------------------------------------------------------------------------
Options_active = pygame.image.load('Images/options_active.png').convert_alpha()
Options_active_rect = Options_active.get_rect()
Options_active_rect.center = (size[0] // 2, 432)

# Кнопка Menu -------------------------------------------------------------------------------------
menu = pygame.image.load('Images/menu.png').convert_alpha()
menu_rect = menu.get_rect()
menu_rect.center = (size[0] // 2, 552)

#  Нажатая кнопка Menu ----------------------------------------------------------------------------
menu_active = pygame.image.load('Images/menu_active.png').convert_alpha()
menu_active_rect = menu_active.get_rect()
menu_active_rect.center = (size[0] // 2, 558)

# Серый фон для паузы -----------------------------------------------------------------------------
bg_pause_new = pygame.image.load('Images/pause_bg_new.jpeg')
# -------------------------------------------------------------------------------------------------