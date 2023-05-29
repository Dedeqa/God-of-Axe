import pygame

pygame.init()
WIDTH = 1920
HEIGHT = 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Иконка игры ----------------------------------------------------------------------------------------------------------
icon = pygame.image.load('Images/menu/icons/icon_axe.png').convert_alpha()

# --------------------------------------------------- Все кнопки меню --------------------------------------------------
# Кнопка Play ----------------------------------------------------------------------------------------------------------
play = pygame.image.load('Images/menu/buttons/play.png').convert_alpha()

# Нажатая нопка Play ---------------------------------------------------------------------------------------------------
active_play = pygame.image.load('Images/menu/buttons/play_active.png').convert_alpha()

# Кнопка Options -------------------------------------------------------------------------------------------------------
options = pygame.image.load('Images/menu/buttons/options.png').convert_alpha()

# Нажатая кнопка Options -----------------------------------------------------------------------------------------------
active_options = pygame.image.load('Images/menu/buttons/options_active.png').convert_alpha()

# Кнопка Quite ---------------------------------------------------------------------------------------------------------
quite = pygame.image.load('Images/menu/buttons/quite.png').convert_alpha()

# Нажатая кнопка Quite -------------------------------------------------------------------------------------------------
active_quite = pygame.image.load('Images/menu/buttons/quite_active.png').convert_alpha()

# --------------------------------------------- Объекты в Options ------------------------------------------------------
# Tablet (табличка) ----------------------------------------------------------------------------------------------------
tablet = pygame.image.load('Images/menu/icons/Tablet.png').convert_alpha()

timer_tablet = pygame.transform.scale(tablet, (250, 50)).convert_alpha()

# Music_label (надпись music) ------------------------------------------------------------------------------------------
music_label = pygame.image.load('Images/menu/labels/music_label.png').convert_alpha()

# Scale1 (шкала громкости музыки) --------------------------------------------------------------------------------------
scale1 = pygame.image.load('Images/menu/icons/scale1.png').convert_alpha()

# Sounds_label (надпись sounds) ----------------------------------------------------------------------------------------
sounds_label = pygame.image.load('Images/menu/labels/sounds_label.png').convert_alpha()

# Scale2 (шкала громкости звуков) --------------------------------------------------------------------------------------
scale2 = pygame.image.load('Images/menu/icons/scale2.png').convert_alpha()

# Point1 (ползунок изменения громкости музыки) -------------------------------------------------------------------------
point1 = pygame.image.load('Images/menu/icons/point1.png').convert_alpha()

# Point2 (ползунок изменения громкости звуков) -------------------------------------------------------------------------
point2 = pygame.image.load('Images/menu/icons/point2.png').convert_alpha()

# Фон меню -------------------------------------------------------------------------------------------------------------
menu_bg = pygame.image.load('Images/backgrounds/bg_menu.jpg').convert_alpha()
game_bg = pygame.image.load('Images/backgrounds/game_field.png').convert_alpha()

# ------------------------------------------------ Кнопки паузы --------------------------------------------------------
# Надпись Pause --------------------------------------------------------------------------------------------------------
pause_label = pygame.image.load('Images/menu/labels/pause_label.png').convert_alpha()

# Кнопка Continue ------------------------------------------------------------------------------------------------------
continue_ = pygame.image.load('Images/menu/buttons/continue.png').convert_alpha()

# Нажатая кнопка Continue ----------------------------------------------------------------------------------------------
continue_active = pygame.image.load('Images/menu/buttons/continue_active.png').convert_alpha()

# Кнопка Options -------------------------------------------------------------------------------------------------------
Options = pygame.image.load('Images/menu/buttons/options.png').convert_alpha()

# Нажатая кнопка Options -----------------------------------------------------------------------------------------------
Options_active = pygame.image.load('Images/menu/buttons/options_active.png').convert_alpha()

# Кнопка Menu ----------------------------------------------------------------------------------------------------------
menu = pygame.image.load('Images/menu/buttons/menu.png').convert_alpha()

# Нажатая кнопка Menu -------------------------------------------------------------------------------------------------
menu_active = pygame.image.load('Images/menu/buttons/menu_active.png').convert_alpha()

# Серый фон для паузы --------------------------------------------------------------------------------------------------
bg_pause_new = pygame.image.load('Images/backgrounds/pause_bg_new.jpeg').convert_alpha()

# --------------------------------------------- Спрайты персонажа ------------------------------------------------------
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

# ----------------------------------------------- Спрайты минотавра ----------------------------------------------------

# Хотьба вниз ----------------------------------------------------------------------------------------------------------
minotaur_walk_bottom = [
    pygame.transform.scale(
        pygame.image.load('Images/monsters/walk_bottom/minotaur-S-stand.png').convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load('Images/monsters/walk_bottom/minotaur-S-step1.png').convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load('Images/monsters/walk_bottom/minotaur-S-step2.png').convert_alpha(), (50, 50))
]
# Хотьба вверх ---------------------------------------------------------------------------------------------------------
minotaur_walk_top = [
    pygame.transform.scale(
        pygame.image.load('Images/monsters/walk_top/minotaur-N-stand.png').convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load('Images/monsters/walk_top/minotaur-N-step1.png').convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load('Images/monsters/walk_top/minotaur-N-step2.png').convert_alpha(), (50, 50))
]

# Хотьба влево ---------------------------------------------------------------------------------------------------------
minotaur_walk_left = [
    pygame.transform.scale(
        pygame.image.load('Images/monsters/walk_left/minotaur-W-stand.png').convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load('Images/monsters/walk_left/minotaur-W-step1.png').convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load('Images/monsters/walk_left/minotaur-W-step2.png').convert_alpha(), (50, 50))
]

# Ходьба вправо --------------------------------------------------------------------------------------------------------
minotaur_walk_right = [
    pygame.transform.scale(
        pygame.image.load('Images/monsters/walk_right/minotaur_stand_right.png').convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load('Images/monsters/walk_right/minotaur_step1_right.png').convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load('Images/monsters/walk_right/minotaur_step2_right.png').convert_alpha(), (50, 50))
]
# Получение урона Player -----------------------------------------------------------------------------------------------
woodcutter_hurt_right = [
    pygame.transform.scale(pygame.image.load(
        'Images/Player/Woodcutter_hurt_right/Woodcutter_hurt1.png').convert_alpha(), (50, 50)),
    pygame.transform.scale(pygame.image.load(
        'Images/Player/Woodcutter_hurt_right/Woodcutter_hurt2.png').convert_alpha(), (50, 50)),
    pygame.transform.scale(pygame.image.load(
        'Images/Player/Woodcutter_hurt_right/Woodcutter_hurt3.png').convert_alpha(), (50, 50))
]
woodcutter_hurt_left = [
    pygame.transform.scale(pygame.image.load(
        'Images/Player/Woodcutter_hurt_left/Woodcutter_hurt_left1.png').convert_alpha(), (50, 50)),
    pygame.transform.scale(pygame.image.load(
        'Images/Player/Woodcutter_hurt_left/Woodcutter_hurt_left2.png').convert_alpha(), (50, 50)),
    pygame.transform.scale(pygame.image.load(
        'Images/Player/Woodcutter_hurt_left/Woodcutter_hurt_left3.png').convert_alpha(), (50, 50)),
]
# --------------------------------------------- Интерфейс --------------------------------------------------------------

# Иконка яблока --------------------------------------------------------------------------------------------------------
apple_icon = pygame.transform.scale(pygame.image.load('Images/Interface/apple_icon.png').convert_alpha(), (30, 30))

# Иконка древесины -----------------------------------------------------------------------------------------------------
wood_icon = pygame.transform.scale(pygame.image.load('Images/Interface/drevesina_icon.png').convert_alpha(), (30, 30))

# Иконка кокоса --------------------------------------------------------------------------------------------------------
coconut_icon = pygame.transform.scale(pygame.image.load('Images/Interface/coconut_icon.png').convert_alpha(), (30, 30))

# Иконка шишки ---------------------------------------------------------------------------------------------------------
shishka_icon = pygame.transform.scale(pygame.image.load('Images/Interface/shishka_icon.png').convert_alpha(), (30, 30))

# Окно You Died --------------------------------------------------------------------------------------------------------
die_bg = pygame.transform.scale(pygame.image.load("Images/backgrounds/Vic.jpg").convert_alpha(), (1920, 1080))

# Фон при победе -------------------------------------------------------------------------------------------------------
vic_bg = pygame.transform.scale(pygame.image.load('Images/backgrounds/blue_vic_bg.jpg').convert_alpha(), (1920, 1080))
