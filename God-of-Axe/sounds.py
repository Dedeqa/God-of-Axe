import pygame
import path_func as f

# Фоновая музыка для меню ----------------------------------------------------------------------------------------------
menu_music_p = f.resource_path('Music/Piano Fantasia - Song for Denise (Wide Walking Extended Version).mp3')
pygame.mixer.music.load(menu_music_p)

# Фоновая музыка для игры ----------------------------------------------------------------------------------------------
play_music_p = f.resource_path(r'Music/Bad Piggies Theme - Piano Tutorial.mp3')
play_music = pygame.mixer.Sound(play_music_p)

# Звук нажатия кнопок меню ---------------------------------------------------------------------------------------------
click_p = f.resource_path(r'Music\zipclick.flac')
click = pygame.mixer.Sound(click_p)

# Звук взмаха топором --------------------------------------------------------------------------------------------------
wave_p = f.resource_path(r'Music\energichnyiy-rezkiy-vzmah-razrezayuschiy-vozduh.mp3')
wave = pygame.mixer.Sound(wave_p)

# Звук шага ------------------------------------------------------------------------------------------------------------
step_p = pygame.mixer.Sound(r'Music\korotkiy-byistryiy-shag-po-lesu.mp3')

# Звук удара о дерево --------------------------------------------------------------------------------------------------
hit_tree_p = f.resource_path(r'Music\korotkiy-chtkiy-rezkiy-udar-po-derevu.mp3')
hit_tree = pygame.mixer.Sound(hit_tree_p)

# Звук падающего дерева ------------------------------------------------------------------------------------------------
falling_tree_p = f.resource_path(r'Music\falling_tree.mp3')
falling_tree = pygame.mixer.Sound(falling_tree_p)

# Звук агра монстров ---------------------------------------------------------------------------------------------------
agr_monster_p = f.resource_path(r'Music\monster-grunt_zksbhlv_.mp3')
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
