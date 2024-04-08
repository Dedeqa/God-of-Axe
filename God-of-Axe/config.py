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

# Лист со всеми объектами
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
monster_add_flag = True
tree_add_flag = True
first_elem_flag = True
lose_flag = False  # флаг поражения
workshop_active_flag = False  # флаг нахождения в мастерской
upgrade_active_flag = False  # флаг нахождения в Upgrade мастерской
trade_active_flag = False
inventory_active_flag = False  # флаг вызова инвентаря
main_active_flag = False  # флаг для main
delta = 125  # "радиус" спавна деревьев
delta_monsters = 200  # "радиус" спавна монстров
delta_hero = 600

difficuilt_flag = 1
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
upgrade_font_p = f.resource_path('Fonts/MclarenRegular.ttf')

# Координаты для перемещения фона---------------------------------------------------------------------------------------
bg_x = 0
bg_y = 0

# Направление персонажа ------------------------------------------------------------------------------------------------
vector = 'right'

# ----------------------------------------- Все кнопки меню ------------------------------------------------------------
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
menu_title = pygame.font.Font(f'{my_font_p}', 100).render("God of Axe", True, (224, 153, 9))
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

# Кнопка Upgrade в Workshop --------------------------------------------------------------------------------------------
# btn_upgrade_rect = img.btn_upgrade.get_rect()
# btn_upgrade_rect.center = (size[0] // 2, 100)


# Условие победы -------------------------------------------------------------------------------------------------------
goal = 500
# Время игровой сессии -------------------------------------------------------------------------------------------------
in_game_time = 0

# ----------------------------------------------- Интерфейс ------------------------------------------------------------
# Workshop -------------------------------------------------------------------------------------------------------------
workshop_tablet_rect = img.workshop_tablet.get_rect()
workshop_tablet_rect.center = (960, 550)
market_label_rect = img.market_label.get_rect()
market_label_rect.center = (980, 200)

upgrade_label_rect = img.upgrade_label.get_rect()
upgrade_label_rect.center = (610, 330)

# Upgrade --------------------------------------------------------------------------------------------------------------
upgrade_description_1 = pygame.font.Font(f'{upgrade_font_p}', 30).render(
    "Here you will help to upgrade some of your skills for a certain amount of coins.",
    True, (255, 255, 255))
upgrade_description_1_rect = upgrade_description_1.get_rect()
upgrade_description_1_rect.center = (960, 420)

upgrade_description_2 = pygame.font.Font(f'{upgrade_font_p}', 30).render(
    "Defeat your enemies and become a real God of Axe!", True, (255, 255, 255))
upgrade_description_2_rect = upgrade_description_2.get_rect()
upgrade_description_2_rect.center = (960, 460)

upgrade_description_3 = pygame.font.Font(f'{upgrade_font_p}', 30).render(
    "(Press ESC to exit from here)", True, (255, 255, 255))
upgrade_description_3_rect = upgrade_description_3.get_rect()
upgrade_description_3_rect.center = (960, 500)

level_cost_list = [10, 20, 40, 70, 110, 160]
current_power_level = 0
current_health_level = 0
current_stamina_level = 0

power_rect = img.power.get_rect()
power_rect.center = (600, 620)
power_description = pygame.font.Font(f'{upgrade_font_p}', 30).render("Axe damage", True, (255, 255, 255))
power_description_rect = power_description.get_rect()
power_description_rect.center = (570, 710)
leveling_scale_power_rect = img.leveling_scale_power0.get_rect()
leveling_scale_power_rect.center = (570, 750)
leveling_scale_power_rect = img.leveling_scale_power1.get_rect()
leveling_scale_power_rect.center = (570, 750)

health_rect = img.health.get_rect()
health_rect.center = (960, 620)
health_description = pygame.font.Font(f'{upgrade_font_p}', 30).render("Max Health", True, (255, 255, 255))
health_description_rect = power_description.get_rect()
health_description_rect.center = (960, 710)
leveling_scale_health_rect = img.leveling_scale_health0.get_rect()
leveling_scale_health_rect.center = (960, 750)

stamina_rect = img.stamina.get_rect()
stamina_rect.center = (1320, 620)
stamina_description = pygame.font.Font(f'{upgrade_font_p}', 30).render("Stamina Recovery Rate", True, (255, 255, 255))
stamina_description_rect = stamina_description.get_rect()
stamina_description_rect.center = (1320, 710)
leveling_scale_stamina_rect = img.leveling_scale_stamina0.get_rect()
leveling_scale_stamina_rect.center = (1320, 750)

buy_power_rect = img.buy.get_rect()
buy_power_rect.center = (570, 860)

buy_health_rect = img.buy.get_rect()
buy_health_rect.center = (960, 860)

buy_stamina_rect = img.buy.get_rect()
buy_stamina_rect.center = (1320, 860)

cost_power = pygame.font.Font(f'{upgrade_font_p}', 30).render(f"Cost: {level_cost_list[current_power_level]} coins",
                                                              True, "green")
cost_power_rect = cost_power.get_rect()
cost_power_rect.center = (570, 800)

cost_health = pygame.font.Font(f'{upgrade_font_p}', 30).render(f"Cost: {level_cost_list[current_health_level]} coins",
                                                               True, "green")
cost_health_rect = cost_health.get_rect()
cost_health_rect.center = (960, 800)

cost_stamina = pygame.font.Font(f'{upgrade_font_p}', 30).render(f"Cost: {level_cost_list[current_stamina_level]} coins",
                                                                True, "green")
cost_stamina_rect = cost_stamina.get_rect()
cost_stamina_rect.center = (1320, 800)

# Trade ----------------------------------------------------------------------------------------------------------------
trade_label_rect = img.trade_label.get_rect()
trade_label_rect.center = (1345, 330)
trade_arrow_rect_apple = img.trade_arrow_green.get_rect()
trade_arrow_rect_apple.center = (983, 443)
trade_arrow_rect_shishka = img.trade_arrow_green.get_rect()
trade_arrow_rect_shishka.center = (983, 543)
trade_arrow_rect_coconut = img.trade_arrow_green.get_rect()
trade_arrow_rect_coconut.center = (983, 643)
trade_arrow_rect_wood = img.trade_arrow_green.get_rect()
trade_arrow_rect_wood.center = (983, 743)

# Инвентарь ------------------------------------------------------------------------------------------------------------
inventory_tablet_rect = img.inventory_tablet.get_rect()
inventory_tablet_rect.center = (950, 400)
# Переменные сдвига карты ----------------------------------------------------------------------------------------------
value_map_shift_x = 0
value_map_shift_y = 0
