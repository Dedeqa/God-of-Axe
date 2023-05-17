import pygame

pygame.init()

WIDTH = 1920
HEIGHT = 1080
FPS = 40

clock = pygame.time.Clock()

menu_flag = True
start_game_flag = True

screen = pygame.display.set_mode((WIDTH, HEIGHT))
size = screen.get_size()

# Иконка игры-----------------------------------------------------------------------------------------------------------
icon = pygame.image.load('Images/menu/icons/icon_axe.png').convert_alpha()

# Все кнопки меню ------------------------------------------------------------------------------------------------------

# Кнопка Play ----------------------------------------------------------------------------------------------------------
play = pygame.image.load('Images/menu/buttons/play.png').convert_alpha()
play_transform = pygame.transform.scale(play, (270, 126))
play_rect = play_transform.get_rect()
play_rect.center = (size[0] // 2, 215)

# Нажатая нопка Play ---------------------------------------------------------------------------------------------------
active_play = pygame.image.load('Images/menu/buttons/play_active.png').convert_alpha()
active_play_transform = pygame.transform.scale(active_play, (270, 114))
active_play_rect = active_play_transform.get_rect()
active_play_rect.center = (size[0] // 2, 221)

# Кнопка Options -------------------------------------------------------------------------------------------------------
options = pygame.image.load('Images/menu/buttons/options.png').convert_alpha()
options_rect = options.get_rect()
options_rect.center = (size[0] // 2, 350)

# Нажатая кнопка Options -----------------------------------------------------------------------------------------------
active_options = pygame.image.load('Images/menu/buttons/options_active.png').convert_alpha()
active_options_rect = active_options.get_rect()
active_options_rect.center = (size[0] // 2, 356)

# Кнопка Quite ---------------------------------------------------------------------------------------------------------
quite = pygame.image.load('Images/menu/buttons/quite.png').convert_alpha()
quite_rect = quite.get_rect()
quite_rect.center = (size[0] // 2, 476)

# Нажатая кнопка Quite -------------------------------------------------------------------------------------------------
active_quite = pygame.image.load('Images/menu/buttons/quite_active.png').convert_alpha()
active_quite_rect = active_quite.get_rect()
active_quite_rect.center = (size[0] // 2, 482)

# Объекты в Options ----------------------------------------------------------------------------------------------------

# Tablet (табличка) ----------------------------------------------------------------------------------------------------
tablet = pygame.image.load('Images/menu/icons/Tablet.png')
tablet_transform = pygame.transform.scale(tablet, (500, 264))
tablet_rect = tablet_transform.get_rect()
tablet_rect.center = (size[0] // 2, 375)

# Music_label (надпись music) ------------------------------------------------------------------------------------------
music_label = pygame.image.load('Images/menu/labels/music_label.png')
music_label_rect = music_label.get_rect()
music_label_rect.center = (size[0] // 2, 275)

# Scale1 (шкала громкости музыки) --------------------------------------------------------------------------------------
scale1 = pygame.image.load('Images/menu/icons/scale1.png')
scale1_rect = scale1.get_rect()
scale1_rect.center = (size[0] // 2, 335)

# Sounds_label (надпись sounds) ----------------------------------------------------------------------------------------
sounds_label = pygame.image.load('Images/menu/labels/sounds_label.png')
sounds_label_rect = sounds_label.get_rect()
sounds_label_rect.center = (size[0] // 2, 395)

# Scale2 (шкала громкости звуков) --------------------------------------------------------------------------------------
scale2 = pygame.image.load('Images/menu/icons/scale2.png')
scale2_rect = scale2.get_rect()
scale2_rect.center = (size[0] // 2, 455)

# Point1 (ползунок изменения громкости музыки) -------------------------------------------------------------------------
point1 = pygame.image.load('Images/menu/icons/point1.png')
point1_rect = point1.get_rect()
point1_rect.center = (scale1_rect.right, scale1_rect.centery)

# Point2 (ползунок изменения громкости звуков) -------------------------------------------------------------------------
point2 = pygame.image.load('Images/menu/icons/point2.png')
point2_rect = point2.get_rect()
point2_rect.center = (scale2_rect.right, scale2_rect.centery)

# ----------------------------------------------------------------------------------------------------------------------

# Установка шрифта -----------------------------------------------------------------------------------------------------
my_font = pygame.font.Font('Fonts/Jfwildwood-ldYZ.ttf', 100)

# Фон меню -------------------------------------------------------------------------------------------------------------
menu_bg = pygame.image.load('Images/backgrounds/bg_menu.jpg').convert_alpha()
game_bg = pygame.image.load('Images/backgrounds/game_field.png').convert_alpha()

# Надпись God of Axe в Меню --------------------------------------------------------------------------------------------
menu_title = my_font.render("God of Axe", True, (224, 153, 9))
menu_title_rect = menu_title.get_rect()
menu_title_rect.bottomleft = (0, size[1])

# Фоновая музыка для меню ----------------------------------------------------------------------------------------------
pygame.mixer.music.load(
    r'Music/Piano Fantasia - Song for Denise (Wide Walking Extended Version).mp3')

# Фоновая музыка для игры ----------------------------------------------------------------------------------------------
play_music = pygame.mixer.Sound(r'Music/Bad Piggies Theme - Piano Tutorial.mp3')

# Звук нажатия кнопок меню ---------------------------------------------------------------------------------------------
click = pygame.mixer.Sound(r'Music\zipclick.flac')

volume_music = 1.0
volume_sounds = 1.0

# Координаты для перемещения фона---------------------------------------------------------------------------------------
bg_x = 0
bg_y = 0

# Кнопки паузы ---------------------------------------------------------------------------------------------------------

# Надпись Pause --------------------------------------------------------------------------------------------------------
pause_label = pygame.image.load('Images/menu/labels/pause_label.png')
pause_label_transform = pygame.transform.scale(pause_label, (400, 113))
pause_label_rect = pause_label_transform.get_rect()
pause_label_rect.center = (size[0] // 2, 100)

# Кнопка Continue ------------------------------------------------------------------------------------------------------
continue_ = pygame.image.load('Images/menu/buttons/continue.png').convert_alpha()
continue_rect = continue_.get_rect()
continue_rect.center = (size[0] // 2, 300)

# Нажатая кнопка Continue ----------------------------------------------------------------------------------------------
continue_active = pygame.image.load('Images/menu/buttons/continue_active.png').convert_alpha()
continue_active_rect = continue_active.get_rect()
continue_active_rect.center = (size[0] // 2, 306)

# Кнопка Options -------------------------------------------------------------------------------------------------------
Options = pygame.image.load('Images/menu/buttons/options.png').convert_alpha()
Options_rect = Options.get_rect()
Options_rect.center = (size[0] // 2, 426)

# Нажатая кнопка Options -----------------------------------------------------------------------------------------------
Options_active = pygame.image.load('Images/menu/buttons/options_active.png').convert_alpha()
Options_active_rect = Options_active.get_rect()
Options_active_rect.center = (size[0] // 2, 432)

# Кнопка Menu ----------------------------------------------------------------------------------------------------------
menu = pygame.image.load('Images/menu/buttons/menu.png').convert_alpha()
menu_rect = menu.get_rect()
menu_rect.center = (size[0] // 2, 552)

#  Нажатая кнопка Menu -------------------------------------------------------------------------------------------------
menu_active = pygame.image.load('Images/menu/buttons/menu_active.png').convert_alpha()
menu_active_rect = menu_active.get_rect()
menu_active_rect.center = (size[0] // 2, 558)

# Серый фон для паузы --------------------------------------------------------------------------------------------------
bg_pause_new = pygame.image.load('Images/backgrounds/pause_bg_new.jpeg').convert_alpha()
# ----------------------------------------------------------------------------------------------------------------------

# Анимации персонажа ---------------------------------------------------------------------------------------------------

# Направление персонажа ------------------------------------------------------------------------------------------------
vector = 'right'

# Персонаж в бездействии -----------------------------------------------------------------------------------------------
woodcutter_stay_right = pygame.transform.scale(pygame.image.load('Images/Player/Woodcutter_right.png').convert_alpha(),
                                               (50, 50))
woodcutter_stay_left = pygame.transform.scale(pygame.image.load('Images/Player/Woodcutter_left.png').convert_alpha(),
                                              (50, 50))
# Хотьба вправо --------------------------------------------------------------------------------------------------------
woodcutter_walk_right = [
    pygame.transform.scale(
        pygame.image.load('Images/Player/Woodcutter_walk_right/Woodcutter_walk1.png').convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load('Images/Player/Woodcutter_walk_right/Woodcutter_walk2.png').convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load('Images/Player/Woodcutter_walk_right/Woodcutter_walk3.png').convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load('Images/Player/Woodcutter_walk_right/Woodcutter_walk4.png').convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load('Images/Player/Woodcutter_walk_right/Woodcutter_walk5.png').convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load('Images/Player/Woodcutter_walk_right/Woodcutter_walk6.png').convert_alpha(), (50, 50)),
]

# Хотьба влево ---------------------------------------------------------------------------------------------------------
woodcutter_walk_left = [
    pygame.transform.scale(
        pygame.image.load('Images/Player/Woodcutter_walk_left/Woodcutter_walk1.png').convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load('Images/Player/Woodcutter_walk_left/Woodcutter_walk2.png').convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load('Images/Player/Woodcutter_walk_left/Woodcutter_walk3.png').convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load('Images/Player/Woodcutter_walk_left/Woodcutter_walk4.png').convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load('Images/Player/Woodcutter_walk_left/Woodcutter_walk5.png').convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load('Images/Player/Woodcutter_walk_left/Woodcutter_walk6.png').convert_alpha(), (50, 50)),
]

# Бег вправо -----------------------------------------------------------------------------------------------------------
woodcutter_run_right = [
    pygame.transform.scale(
        pygame.image.load('Images/Player/Woodcutter_run_right/Woodcutter_run1.png').convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load('Images/Player/Woodcutter_run_right/Woodcutter_run2.png').convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load('Images/Player/Woodcutter_run_right/Woodcutter_run3.png').convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load('Images/Player/Woodcutter_run_right/Woodcutter_run4.png').convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load('Images/Player/Woodcutter_run_right/Woodcutter_run5.png').convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load('Images/Player/Woodcutter_run_right/Woodcutter_run6.png').convert_alpha(), (50, 50)),
]

# Бег влево ------------------------------------------------------------------------------------------------------------
woodcutter_run_left = [
    pygame.transform.scale(
        pygame.image.load('Images/Player/Woodcutter_run_left/Woodcutter_run1.png').convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load('Images/Player/Woodcutter_run_left/Woodcutter_run2.png').convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load('Images/Player/Woodcutter_run_left/Woodcutter_run3.png').convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load('Images/Player/Woodcutter_run_left/Woodcutter_run4.png').convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load('Images/Player/Woodcutter_run_left/Woodcutter_run5.png').convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load('Images/Player/Woodcutter_run_left/Woodcutter_run6.png').convert_alpha(), (50, 50)),
]

# Атака вправо ---------------------------------------------------------------------------------------------------------
woodcutter_attack_right = [
    pygame.transform.scale(
        pygame.image.load('Images/Player/Woodcutter_attack_right/attack_1.png').convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load('Images/Player/Woodcutter_attack_right/attack_2.png').convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load('Images/Player/Woodcutter_attack_right/attack_3.png').convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load('Images/Player/Woodcutter_attack_right/attack_4.png').convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load('Images/Player/Woodcutter_attack_right/attack_5.png').convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load('Images/Player/Woodcutter_attack_right/attack_6.png').convert_alpha(), (50, 50)),
]

# Атака влево ----------------------------------------------------------------------------------------------------------
woodcutter_attack_left = [
    pygame.transform.scale(
        pygame.image.load('Images/Player/Woodcutter_attack_left/attack_1.png').convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load('Images/Player/Woodcutter_attack_left/attack_2.png').convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load('Images/Player/Woodcutter_attack_left/attack_3.png').convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load('Images/Player/Woodcutter_attack_left/attack_4.png').convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load('Images/Player/Woodcutter_attack_left/attack_5.png').convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load('Images/Player/Woodcutter_attack_left/attack_6.png').convert_alpha(), (50, 50)),
]

tree_list_x = []
tree_list_y = []
trees = []
