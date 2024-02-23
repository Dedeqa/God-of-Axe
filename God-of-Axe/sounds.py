import pygame
import path_func as f
pygame.init()

# Фоновая музыка для меню ----------------------------------------------------------------------------------------------
menu_music_p = f.resource_path(r'Music/Piano Fantasia - Song for Denise (Wide Walking Extended Version).mp3')
pygame.mixer.music.load(menu_music_p)

# Фоновая музыка для игры ----------------------------------------------------------------------------------------------
play_music_p = f.resource_path(r'Music/Bad Piggies Theme - Piano Tutorial.mp3')
play_music = pygame.mixer.Sound(play_music_p)

# Звук нажатия кнопок меню ---------------------------------------------------------------------------------------------
click_p = f.resource_path(r'Music/zipclick.flac')
click = pygame.mixer.Sound(click_p)

# Звук взмаха топором --------------------------------------------------------------------------------------------------
wave_p = f.resource_path(r'Music/energichnyiy-rezkiy-vzmah-razrezayuschiy-vozduh.mp3')
wave = pygame.mixer.Sound(wave_p)

# Звук шага ------------------------------------------------------------------------------------------------------------
step_p = pygame.mixer.Sound(r'Music/korotkiy-byistryiy-shag-po-lesu.mp3')

# Звук удара о дерево --------------------------------------------------------------------------------------------------
hit_tree_p = f.resource_path(r'Music/korotkiy-chtkiy-rezkiy-udar-po-derevu.mp3')
hit_tree = pygame.mixer.Sound(hit_tree_p)

# Звуки получения урона ------------------------------------------------------------------------------------------------
take_dmg1_p = f.resource_path(r'Music/take_dmg1.mp3')
take_dmg2_p = f.resource_path(r'Music/take_dmg2.mp3')
take_dmg3_p = f.resource_path(r'Music/take_dmg3.mp3')
last_hit_p = f.resource_path(r'Music/last_hit.mp3')


take_dmg1 = pygame.mixer.Sound(take_dmg1_p)
take_dmg2 = pygame.mixer.Sound(take_dmg2_p)
take_dmg3 = pygame.mixer.Sound(take_dmg3_p)

index = 0

take_dmg_sounds_list = [take_dmg1, take_dmg2, take_dmg3]

last_hit = pygame.mixer.Sound(last_hit_p)

# Звук удара по монстру ------------------------------------------------------------------------------------------------
hit_monster_p = f.resource_path(r'Music/rassechenie-ploti-boevym-toporom-48.mp3')
hit_monster = pygame.mixer.Sound(hit_monster_p)

# Звук падающего дерева ------------------------------------------------------------------------------------------------
falling_tree_p = f.resource_path(r'Music/falling_tree.mp3')
falling_tree = pygame.mixer.Sound(falling_tree_p)

# Звук агра монстров ---------------------------------------------------------------------------------------------------
agr_monster_p = f.resource_path(r'Music/monster-grunt_zksbhlv_.mp3')
agr_monster = pygame.mixer.Sound(agr_monster_p)

# Звук поедания яблока -------------------------------------------------------------------------------------------------
eat_apple_p = f.resource_path(r'Music/the_sound_of_eating_an_apple.mp3')
eat_apple = pygame.mixer.Sound(eat_apple_p)

# Звук выпивания кокоса
drink_coconut_p = f.resource_path(r'Music/eat_coconut.mp3')
drink_coconut = pygame.mixer.Sound(drink_coconut_p)

# Громкость звуков -----------------------------------------------------------------------------------------------------
volume_music = 1.0
volume_sounds = 1.0
volume_wave = 1.0
volume_hit_tree = 1.0
volume_agr_monster = 1.0
volume_falling_tree = 1.0
