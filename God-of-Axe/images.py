import pygame
import path_func as f

pygame.init()
WIDTH = 1920
HEIGHT = 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Иконка игры ----------------------------------------------------------------------------------------------------------
# icon = pygame.image.load('Images/menu/icons/icon_axe.png').convert_alpha()
icon_p = f.resource_path('Images/menu/icons/icon_axe.png')
icon = pygame.image.load(icon_p).convert_alpha()

# --------------------------------------------------- Все кнопки меню --------------------------------------------------
# Кнопка Play ----------------------------------------------------------------------------------------------------------
play_p = f.resource_path('Images/menu/buttons/play.png')
play = pygame.image.load(play_p).convert_alpha()

# Нажатая нопка Play ---------------------------------------------------------------------------------------------------
active_play_p = f.resource_path('Images/menu/buttons/play_active.png')
active_play = pygame.image.load(active_play_p).convert_alpha()

# Кнопка Options -------------------------------------------------------------------------------------------------------
options_p = f.resource_path('Images/menu/buttons/options.png')
options = pygame.image.load(options_p).convert_alpha()

# Нажатая кнопка Options -----------------------------------------------------------------------------------------------
active_options_p = f.resource_path('Images/menu/buttons/options_active.png')
active_options = pygame.image.load(active_options_p).convert_alpha()

# Кнопка Quite ---------------------------------------------------------------------------------------------------------
quite_p = f.resource_path('Images/menu/buttons/quite.png')
quite = pygame.image.load(quite_p).convert_alpha()

# Нажатая кнопка Quite -------------------------------------------------------------------------------------------------
active_quite_p = f.resource_path('Images/menu/buttons/quite_active.png')
active_quite = pygame.image.load(active_quite_p).convert_alpha()

# --------------------------------------------- Объекты в Options ------------------------------------------------------
# Tablet (табличка) ----------------------------------------------------------------------------------------------------
tablet_p = f.resource_path('Images/menu/icons/Tablet.png')
tablet = pygame.image.load(tablet_p).convert_alpha()

# Music_label (надпись music) ------------------------------------------------------------------------------------------
music_label_p = f.resource_path('Images/menu/labels/music_label.png')
music_label = pygame.image.load(music_label_p).convert_alpha()

# Scale1 (шкала громкости музыки) --------------------------------------------------------------------------------------
scale1_p = f.resource_path('Images/menu/icons/scale1.png')
scale1 = pygame.image.load(scale1_p)

# Sounds_label (надпись sounds) ----------------------------------------------------------------------------------------
sounds_label_p = f.resource_path('Images/menu/labels/sounds_label.png')
sounds_label = pygame.image.load(sounds_label_p)
# Scale2 (шкала громкости звуков) --------------------------------------------------------------------------------------
scale2_p = f.resource_path('Images/menu/icons/scale2.png')
scale2 = pygame.image.load(scale2_p)
# Point1 (ползунок изменения громкости музыки) -------------------------------------------------------------------------
point1_p = f.resource_path('Images/menu/icons/point1.png')
point1 = pygame.image.load(point1_p)
# Point2 (ползунок изменения громкости звуков) -------------------------------------------------------------------------
point2_p = f.resource_path('Images/menu/icons/point2.png')
point2 = pygame.image.load(point2_p)
# Фон меню -------------------------------------------------------------------------------------------------------------
menu_bg_p = f.resource_path('Images/backgrounds/bg_menu.jpg')
game_bg_p = f.resource_path('Images/backgrounds/game_field.png')
menu_bg = pygame.image.load(menu_bg_p).convert_alpha()
game_bg = pygame.image.load(game_bg_p).convert_alpha()
# ------------------------------------------------ Кнопки паузы --------------------------------------------------------
# Надпись Pause --------------------------------------------------------------------------------------------------------
pause_label_p = f.resource_path('Images/menu/labels/pause_label.png')
pause_label = pygame.image.load(pause_label_p).convert_alpha()
# Кнопка Continue ------------------------------------------------------------------------------------------------------
continue_p = f.resource_path('Images/menu/buttons/continue.png')
continue_ = pygame.image.load(continue_p).convert_alpha()
# Нажатая кнопка Continue ----------------------------------------------------------------------------------------------
continue_active_p = f.resource_path('Images/menu/buttons/continue_active.png')
continue_active = pygame.image.load(continue_active_p).convert_alpha()
# Кнопка Options -------------------------------------------------------------------------------------------------------
Options_p = f.resource_path('Images/menu/buttons/options.png')
Options = pygame.image.load(Options_p).convert_alpha()
# Нажатая кнопка Options -----------------------------------------------------------------------------------------------
Options_active_p = f.resource_path('Images/menu/buttons/options_active.png')
Options_active = pygame.image.load(Options_active_p).convert_alpha()
# Кнопка Menu ----------------------------------------------------------------------------------------------------------
menu_p = f.resource_path('Images/menu/buttons/menu.png')
menu = pygame.image.load(menu_p).convert_alpha()
# Нажатая кнопка Menu -------------------------------------------------------------------------------------------------
menu_active_p = f.resource_path('Images/menu/buttons/menu_active.png')
menu_active = pygame.image.load(menu_active_p).convert_alpha()
# Серый фон для паузы --------------------------------------------------------------------------------------------------
bg_pause_new_p = f.resource_path('Images/backgrounds/pause_bg_new.jpeg')
bg_pause_new = pygame.image.load(bg_pause_new_p).convert_alpha()
# --------------------------------------------- Спрайты персонажа ------------------------------------------------------
# Персонаж в бездействии -----------------------------------------------------------------------------------------------
woodcutter_stay_right_p = f.resource_path('Images/Player/Woodcutter_right.png')
woodcutter_stay_right = pygame.transform.scale(pygame.image.load(woodcutter_stay_right_p).convert_alpha(), (50, 50))

woodcutter_stay_left_p = f.resource_path('Images/Player/Woodcutter_left.png')
woodcutter_stay_left = pygame.transform.scale(pygame.image.load(woodcutter_stay_left_p).convert_alpha(), (50, 50))
# Хотьба вправо --------------------------------------------------------------------------------------------------------
woodcutter_walk1_r_p = f.resource_path('Images/Player/Woodcutter_walk_right/Woodcutter_walk1.png')
woodcutter_walk2_r_p = f.resource_path('Images/Player/Woodcutter_walk_right/Woodcutter_walk2.png')
woodcutter_walk3_r_p = f.resource_path('Images/Player/Woodcutter_walk_right/Woodcutter_walk3.png')
woodcutter_walk4_r_p = f.resource_path('Images/Player/Woodcutter_walk_right/Woodcutter_walk4.png')
woodcutter_walk5_r_p = f.resource_path('Images/Player/Woodcutter_walk_right/Woodcutter_walk5.png')
woodcutter_walk6_r_p = f.resource_path('Images/Player/Woodcutter_walk_right/Woodcutter_walk6.png')

woodcutter_walk_right = [
    pygame.transform.scale(
        pygame.image.load(woodcutter_walk1_r_p).convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load(woodcutter_walk2_r_p).convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load(woodcutter_walk3_r_p).convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load(woodcutter_walk4_r_p).convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load(woodcutter_walk5_r_p).convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load(woodcutter_walk6_r_p).convert_alpha(), (50, 50)),
]

# Хотьба влево ---------------------------------------------------------------------------------------------------------
woodcutter_walk1_l_p = f.resource_path('Images/Player/Woodcutter_walk_left/Woodcutter_walk1.png')
woodcutter_walk2_l_p = f.resource_path('Images/Player/Woodcutter_walk_left/Woodcutter_walk2.png')
woodcutter_walk3_l_p = f.resource_path('Images/Player/Woodcutter_walk_left/Woodcutter_walk3.png')
woodcutter_walk4_l_p = f.resource_path('Images/Player/Woodcutter_walk_left/Woodcutter_walk4.png')
woodcutter_walk5_l_p = f.resource_path('Images/Player/Woodcutter_walk_left/Woodcutter_walk5.png')
woodcutter_walk6_l_p = f.resource_path('Images/Player/Woodcutter_walk_left/Woodcutter_walk6.png')

woodcutter_walk_left = [
    pygame.transform.scale(
        pygame.image.load(woodcutter_walk1_l_p).convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load(woodcutter_walk2_l_p).convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load(woodcutter_walk3_l_p).convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load(woodcutter_walk4_l_p).convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load(woodcutter_walk5_l_p).convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load(woodcutter_walk6_l_p).convert_alpha(), (50, 50)),
]

# Бег вправо -----------------------------------------------------------------------------------------------------------
woodcutter_run1_r_p = f.resource_path('Images/Player/Woodcutter_run_right/Woodcutter_run1.png')
woodcutter_run2_r_p = f.resource_path('Images/Player/Woodcutter_run_right/Woodcutter_run2.png')
woodcutter_run3_r_p = f.resource_path('Images/Player/Woodcutter_run_right/Woodcutter_run3.png')
woodcutter_run4_r_p = f.resource_path('Images/Player/Woodcutter_run_right/Woodcutter_run4.png')
woodcutter_run5_r_p = f.resource_path('Images/Player/Woodcutter_run_right/Woodcutter_run5.png')
woodcutter_run6_r_p = f.resource_path('Images/Player/Woodcutter_run_right/Woodcutter_run6.png')

woodcutter_run_right = [
    pygame.transform.scale(
        pygame.image.load(woodcutter_run1_r_p).convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load(woodcutter_run2_r_p).convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load(woodcutter_run3_r_p).convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load(woodcutter_run4_r_p).convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load(woodcutter_run5_r_p).convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load(woodcutter_run6_r_p).convert_alpha(), (50, 50)),
]

# Бег влево ------------------------------------------------------------------------------------------------------------
woodcutter_run1_l_p = f.resource_path('Images/Player/Woodcutter_run_left/Woodcutter_run1.png')
woodcutter_run2_l_p = f.resource_path('Images/Player/Woodcutter_run_left/Woodcutter_run2.png')
woodcutter_run3_l_p = f.resource_path('Images/Player/Woodcutter_run_left/Woodcutter_run3.png')
woodcutter_run4_l_p = f.resource_path('Images/Player/Woodcutter_run_left/Woodcutter_run4.png')
woodcutter_run5_l_p = f.resource_path('Images/Player/Woodcutter_run_left/Woodcutter_run5.png')
woodcutter_run6_l_p = f.resource_path('Images/Player/Woodcutter_run_left/Woodcutter_run6.png')

woodcutter_run_left = [
    pygame.transform.scale(
        pygame.image.load(woodcutter_run1_l_p).convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load(woodcutter_run2_l_p).convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load(woodcutter_run3_l_p).convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load(woodcutter_run4_l_p).convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load(woodcutter_run5_l_p).convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load(woodcutter_run6_l_p).convert_alpha(), (50, 50)),
]

# Атака вправо ---------------------------------------------------------------------------------------------------------
woodcutter_attack1_r_p = f.resource_path('Images/Player/Woodcutter_attack_right/attack_1.png')
woodcutter_attack2_r_p = f.resource_path('Images/Player/Woodcutter_attack_right/attack_2.png')
woodcutter_attack3_r_p = f.resource_path('Images/Player/Woodcutter_attack_right/attack_3.png')
woodcutter_attack4_r_p = f.resource_path('Images/Player/Woodcutter_attack_right/attack_4.png')
woodcutter_attack5_r_p = f.resource_path('Images/Player/Woodcutter_attack_right/attack_5.png')
woodcutter_attack6_r_p = f.resource_path('Images/Player/Woodcutter_attack_right/attack_6.png')

woodcutter_attack_right = [
    pygame.transform.scale(
        pygame.image.load(woodcutter_attack1_r_p).convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load(woodcutter_attack2_r_p).convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load(woodcutter_attack3_r_p).convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load(woodcutter_attack4_r_p).convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load(woodcutter_attack5_r_p).convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load(woodcutter_attack6_r_p).convert_alpha(), (50, 50)),
]

# Атака влево ----------------------------------------------------------------------------------------------------------
woodcutter_attack1_l_p = f.resource_path('Images/Player/Woodcutter_attack_left/attack_1.png')
woodcutter_attack2_l_p = f.resource_path('Images/Player/Woodcutter_attack_left/attack_2.png')
woodcutter_attack3_l_p = f.resource_path('Images/Player/Woodcutter_attack_left/attack_3.png')
woodcutter_attack4_l_p = f.resource_path('Images/Player/Woodcutter_attack_left/attack_4.png')
woodcutter_attack5_l_p = f.resource_path('Images/Player/Woodcutter_attack_left/attack_5.png')
woodcutter_attack6_l_p = f.resource_path('Images/Player/Woodcutter_attack_left/attack_6.png')

woodcutter_attack_left = [
    pygame.transform.scale(
        pygame.image.load(woodcutter_attack1_l_p).convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load(woodcutter_attack2_l_p).convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load(woodcutter_attack3_l_p).convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load(woodcutter_attack4_l_p).convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load(woodcutter_attack5_l_p).convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load(woodcutter_attack6_l_p).convert_alpha(), (50, 50)),
]

# Смерть вправо --------------------------------------------------------------------------------------------------------
woodcutter_death1_r_p = f.resource_path('Images/Player/Woodcutter_death_right/death1.png')
woodcutter_death2_r_p = f.resource_path('Images/Player/Woodcutter_death_right/death2.png')
woodcutter_death3_r_p = f.resource_path('Images/Player/Woodcutter_death_right/death3.png')
woodcutter_death4_r_p = f.resource_path('Images/Player/Woodcutter_death_right/death4.png')
woodcutter_death5_r_p = f.resource_path('Images/Player/Woodcutter_death_right/death5.png')
woodcutter_death6_r_p = f.resource_path('Images/Player/Woodcutter_death_right/death6.png')

woodcutter_death_right = [
    pygame.transform.scale(
        pygame.image.load(woodcutter_death1_r_p).convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load(woodcutter_death2_r_p).convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load(woodcutter_death3_r_p).convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load(woodcutter_death4_r_p).convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load(woodcutter_death5_r_p).convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load(woodcutter_death6_r_p).convert_alpha(), (50, 50)),
]

# Смерть влево ---------------------------------------------------------------------------------------------------------
woodcutter_death1_l_p = f.resource_path('Images/Player/Woodcutter_death_left/death1.png')
woodcutter_death2_l_p = f.resource_path('Images/Player/Woodcutter_death_left/death2.png')
woodcutter_death3_l_p = f.resource_path('Images/Player/Woodcutter_death_left/death3.png')
woodcutter_death4_l_p = f.resource_path('Images/Player/Woodcutter_death_left/death4.png')
woodcutter_death5_l_p = f.resource_path('Images/Player/Woodcutter_death_left/death5.png')
woodcutter_death6_l_p = f.resource_path('Images/Player/Woodcutter_death_left/death6.png')

woodcutter_death_left = [
    pygame.transform.scale(
        pygame.image.load(woodcutter_death1_l_p).convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load(woodcutter_death2_l_p).convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load(woodcutter_death3_l_p).convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load(woodcutter_death4_l_p).convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load(woodcutter_death5_l_p).convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load(woodcutter_death6_l_p).convert_alpha(), (50, 50)),
]

# ----------------------------------------------- Спрайты минотавра ----------------------------------------------------

# Ходьба вниз ----------------------------------------------------------------------------------------------------------
minotaur_walk_bottom1_p = f.resource_path('Images/monsters/walk_bottom/minotaur-S-stand.png')
minotaur_walk_bottom2_p = f.resource_path('Images/monsters/walk_bottom/minotaur-S-step1.png')
minotaur_walk_bottom3_p = f.resource_path('Images/monsters/walk_bottom/minotaur-S-step2.png')

minotaur_walk_bottom = [
    pygame.transform.scale(
        pygame.image.load(minotaur_walk_bottom1_p).convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load(minotaur_walk_bottom2_p).convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load(minotaur_walk_bottom3_p).convert_alpha(), (50, 50))
]
# Ходьба вверх ---------------------------------------------------------------------------------------------------------
minotaur_walk_top1_p = f.resource_path('Images/monsters/walk_top/minotaur-N-stand.png')
minotaur_walk_top2_p = f.resource_path('Images/monsters/walk_top/minotaur-N-step1.png')
minotaur_walk_top3_p = f.resource_path('Images/monsters/walk_top/minotaur-N-step2.png')

minotaur_walk_top = [
    pygame.transform.scale(
        pygame.image.load(minotaur_walk_top1_p).convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load(minotaur_walk_top2_p).convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load(minotaur_walk_top3_p).convert_alpha(), (50, 50))
]

# Ходьба влево ---------------------------------------------------------------------------------------------------------
minotaur_walk_left1_p = f.resource_path('Images/monsters/walk_left/minotaur-W-stand.png')
minotaur_walk_left2_p = f.resource_path('Images/monsters/walk_left/minotaur-W-step1.png')
minotaur_walk_left3_p = f.resource_path('Images/monsters/walk_left/minotaur-W-step2.png')

minotaur_walk_left = [
    pygame.transform.scale(
        pygame.image.load(minotaur_walk_left1_p).convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load(minotaur_walk_left2_p).convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load(minotaur_walk_left1_p).convert_alpha(), (50, 50))
]

# Ходьба вправо --------------------------------------------------------------------------------------------------------
minotaur_walk_right1_p = f.resource_path('Images/monsters/walk_right/minotaur_stand_right.png')
minotaur_walk_right2_p = f.resource_path('Images/monsters/walk_right/minotaur_step1_right.png')
minotaur_walk_right3_p = f.resource_path('Images/monsters/walk_right/minotaur_step2_right.png')

minotaur_walk_right = [
    pygame.transform.scale(
        pygame.image.load(minotaur_walk_right1_p).convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load(minotaur_walk_right2_p).convert_alpha(), (50, 50)),
    pygame.transform.scale(
        pygame.image.load(minotaur_walk_right3_p).convert_alpha(), (50, 50))
]
# Получение урона Player -----------------------------------------------------------------------------------------------
woodcutter_hurt_right1_p = f.resource_path('Images/Player/Woodcutter_hurt_right/Woodcutter_hurt1.png')
woodcutter_hurt_right2_p = f.resource_path('Images/Player/Woodcutter_hurt_right/Woodcutter_hurt2.png')
woodcutter_hurt_right3_p = f.resource_path('Images/Player/Woodcutter_hurt_right/Woodcutter_hurt3.png')

woodcutter_hurt_right = [
    pygame.transform.scale(pygame.image.load(
        woodcutter_hurt_right1_p).convert_alpha(), (50, 50)),
    pygame.transform.scale(pygame.image.load(
        woodcutter_hurt_right2_p).convert_alpha(), (50, 50)),
    pygame.transform.scale(pygame.image.load(
        woodcutter_hurt_right3_p).convert_alpha(), (50, 50))
]

woodcutter_hurt_left1_p = f.resource_path('Images/Player/Woodcutter_hurt_left/Woodcutter_hurt_left1.png')
woodcutter_hurt_left2_p = f.resource_path('Images/Player/Woodcutter_hurt_left/Woodcutter_hurt_left2.png')
woodcutter_hurt_left3_p = f.resource_path('Images/Player/Woodcutter_hurt_left/Woodcutter_hurt_left3.png')

woodcutter_hurt_left = [
    pygame.transform.scale(pygame.image.load(
        woodcutter_hurt_left1_p).convert_alpha(), (50, 50)),
    pygame.transform.scale(pygame.image.load(
        woodcutter_hurt_left2_p).convert_alpha(), (50, 50)),
    pygame.transform.scale(pygame.image.load(
        woodcutter_hurt_left3_p).convert_alpha(), (50, 50)),
]
# --------------------------------------------- Интерфейс --------------------------------------------------------------

# Workshop -------------------------------------------------------------------------------------------------------------
workshop_tablet_p = f.resource_path('Images/workshop/workshop_tablet.png')
workshop_tablet = pygame.transform.scale(pygame.image.load(workshop_tablet_p).convert_alpha(), (800, 400))

# Иконка яблока --------------------------------------------------------------------------------------------------------
apple_icon_p = f.resource_path('Images/Interface/apple_icon.png')
apple_icon = pygame.transform.scale(pygame.image.load(apple_icon_p).convert_alpha(), (70, 70))

# Иконка древесины -----------------------------------------------------------------------------------------------------
wood_icon_p = f.resource_path('Images/Interface/drevesina_icon.png')
wood_icon = pygame.transform.scale(pygame.image.load(wood_icon_p).convert_alpha(), (70, 70))

# Иконка кокоса --------------------------------------------------------------------------------------------------------
coconut_icon_p = f.resource_path('Images/Interface/coconut_icon.png')
coconut_icon = pygame.transform.scale(pygame.image.load(coconut_icon_p).convert_alpha(), (70, 70))

# Иконка шишки ---------------------------------------------------------------------------------------------------------
shishka_icon_p = f.resource_path('Images/Interface/shishka_icon.png')
shishka_icon = pygame.transform.scale(pygame.image.load(shishka_icon_p).convert_alpha(), (70, 70))

# Иконка монетки -------------------------------------------------------------------------------------------------------
coin_icon_p = f.resource_path('Images/Interface/coin.png')
coin_icon = pygame.transform.scale(pygame.image.load(coin_icon_p).convert_alpha(), (70, 70))

# Окно инвентаря -------------------------------------------------------------------------------------------------------
inventory_tablet_p = f.resource_path('Images/Interface/inventory_tablet.png')
inventory_tablet = pygame.transform.scale(pygame.image.load(inventory_tablet_p).convert_alpha(), (800, 400))

# Окно You Died --------------------------------------------------------------------------------------------------------
die_bg_p = f.resource_path("Images/backgrounds/Vic.jpg")
die_bg = pygame.transform.scale(pygame.image.load(die_bg_p).convert_alpha(), (1920, 1080))

# Фон при победе -------------------------------------------------------------------------------------------------------
vic_bg_p = f.resource_path('Images/backgrounds/blue_vic_bg.jpg')
vic_bg = pygame.transform.scale(pygame.image.load(vic_bg_p).convert_alpha(), (1920, 1080))

# Ионка дома
house_icon = pygame.image.load('Images/other_objects/house.png')

# Кнопка Upgrade в Workshop --------------------------------------------------------------------------------------------
btn_upgrade_p = f.resource_path("Images/other_objects/btn_upgrade.png")
btn_upgrade = pygame.transform.scale(pygame.image.load(btn_upgrade_p).convert_alpha(), (300, 200))
