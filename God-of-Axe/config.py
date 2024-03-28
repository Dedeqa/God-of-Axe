import pygame
import images as img
import path_func as f

pygame.init()

WIDTH = 1920  # Параметры окна
HEIGHT = 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT))
size = screen.get_size()
label = pygame.Rect(0, 0, 200, 200)

FPS = 60  # Количество FPS

clock = pygame.time.Clock()

#Лист со всеми объектами
all_sprites = pygame.sprite.Group()
list_all_sprites = []

random_list = [40, 25, 30]
temp_random_list = [40, 25, 30]

random_dub = 40
random_elka = 25
random_palma = 30

# menu_sound_flag = True  # флаг нахождения в меню
menu_active_flag = False
# play_game_active_flag = False
start_game_sound_flag = True  # флаг запуска игры для воспроизведения музыки
pause_active_flag = False
play_game_active_flag = False
lose_game_active_flag = False
win_game_active_flag = False
add_flag = True
first_elem_flag = True
lose_flag = False  # флаг поражения
workshop_active_flag = False  # флаг нахождения в мастерской
main_active_flag = False # флаг для main
delta = 125  # "радиус" спавна деревьев
delta_monsters = 200  # "радиус" спавна монстров
delta_hero = 600
# Список деревьев ------------------------------------------------------------------------------------------------------
tree_list_x = []
tree_list_y = []

trees1 = []
trees2 = []
trees3 = []

trees_rects_right = []
trees_rects_left = []
trees_rects_top = []
trees_rects_bottom = []

# Список мобов ---------------------------------------------------------------------------------------------------------

monsterList = []
monster_list_x = []
monster_list_y = []

# Шрифты ---------------------------------------------------------------------------------------------------------------
my_font_p = f.resource_path('Fonts/Jfwildwood-ldYZ.ttf')
font_interface_p = f.resource_path('Fonts/HoltwoodOneSC-Regular.ttf')

# Координаты для перемещения фона---------------------------------------------------------------------------------------
bg_x = 0
bg_y = 0

# Направление персонажа ------------------------------------------------------------------------------------------------
vector = 'right'

# Все кнопки меню ------------------------------------------------------------------------------------------------------
# Кнопка Play ----------------------------------------------------------------------------------------------------------
play_transform = pygame.transform.scale(img.play, (270, 126))
play_rect = play_transform.get_rect()
play_rect.center = (size[0] // 2, 215)

# Нажатая нопка Play ---------------------------------------------------------------------------------------------------
active_play_transform = pygame.transform.scale(img.active_play, (270, 114))
active_play_rect = active_play_transform.get_rect()
active_play_rect.center = (size[0] // 2, 221)

# Кнопка Options -------------------------------------------------------------------------------------------------------
options_rect = img.options.get_rect()
options_rect.center = (size[0] // 2, 350)

# Нажатая кнопка Options -----------------------------------------------------------------------------------------------
active_options_rect = img.active_options.get_rect()
active_options_rect.center = (size[0] // 2, 356)

# Кнопка Quite ---------------------------------------------------------------------------------------------------------
quit_rect = img.quite.get_rect()
quit_rect.center = (size[0] // 2, 476)

# Нажатая кнопка Quite -------------------------------------------------------------------------------------------------
active_quite_rect = img.active_quite.get_rect()
active_quite_rect.center = (size[0] // 2, 482)

# --------------------------------------------- Объекты в Options ------------------------------------------------------
# Tablet (табличка) ----------------------------------------------------------------------------------------------------
tablet_transform = pygame.transform.scale(img.tablet, (500, 264))
tablet_rect = tablet_transform.get_rect()
tablet_rect.center = (size[0] // 2, 375)

# Music_label (надпись music) ------------------------------------------------------------------------------------------
music_label_rect = img.music_label.get_rect()
music_label_rect.center = (size[0] // 2, 275)

# Scale1 (шкала громкости музыки) --------------------------------------------------------------------------------------
scale1_rect = img.scale1.get_rect()
scale1_rect.center = (size[0] // 2, 335)

# Sounds_label (надпись sounds) ----------------------------------------------------------------------------------------
sounds_label_rect = img.sounds_label.get_rect()
sounds_label_rect.center = (size[0] // 2, 395)

# Scale2 (шкала громкости звуков) --------------------------------------------------------------------------------------
scale2_rect = img.scale2.get_rect()
scale2_rect.center = (size[0] // 2, 455)

# Point1 (ползунок изменения громкости музыки) -------------------------------------------------------------------------
point1_rect = img.point1.get_rect()
point1_rect.center = (scale1_rect.right, scale1_rect.centery)

# Point2 (ползунок изменения громкости звуков) -------------------------------------------------------------------------
point2_rect = img.point2.get_rect()
point2_rect.center = (scale2_rect.right, scale2_rect.centery)

# Надпись God of Axe в Меню --------------------------------------------------------------------------------------------
menu_title = pygame.font.Font(f'{my_font_p}', 100).render("BIG PENIS", True, (224, 153, 9))
menu_title_rect = menu_title.get_rect()
menu_title_rect.bottomleft = (0, size[1])

# ------------------------------------------------ Кнопки паузы --------------------------------------------------------
# Надпись Pause --------------------------------------------------------------------------------------------------------
pause_label_transform = pygame.transform.scale(img.pause_label, (400, 113))
pause_label_rect = pause_label_transform.get_rect()
pause_label_rect.center = (size[0] // 2, 100)

# Кнопка Continue ------------------------------------------------------------------------------------------------------
continue_rect = img.continue_.get_rect()
continue_rect.center = (size[0] // 2, 300)

# Нажатая кнопка Continue ----------------------------------------------------------------------------------------------
continue_active_rect = img.continue_active.get_rect()
continue_active_rect.center = (size[0] // 2, 306)

# Кнопка Options -------------------------------------------------------------------------------------------------------
Options_rect = img.Options.get_rect()
Options_rect.center = (size[0] // 2, 426)

# Нажатая кнопка Options -----------------------------------------------------------------------------------------------
Options_active_rect = img.Options_active.get_rect()
Options_active_rect.center = (size[0] // 2, 432)

# Кнопка Menu ----------------------------------------------------------------------------------------------------------
menu_rect = img.menu.get_rect()
menu_rect.center = (size[0] // 2, 552)

# Нажатая кнопка Menu --------------------------------------------------------------------------------------------------
menu_active_rect = img.menu_active.get_rect()
menu_active_rect.center = (size[0] // 2, 558)

# Условие победы -------------------------------------------------------------------------------------------------------
goal = 5
# Время игровой сессии -------------------------------------------------------------------------------------------------
in_game_time = 0
