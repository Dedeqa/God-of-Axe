import pygame

# Фоновая музыка для меню ----------------------------------------------------------------------------------------------
pygame.mixer.music.load(
    r'Music/Piano Fantasia - Song for Denise (Wide Walking Extended Version).mp3')

# Фоновая музыка для игры ----------------------------------------------------------------------------------------------
play_music = pygame.mixer.Sound(r'Music/Bad Piggies Theme - Piano Tutorial.mp3')

# Звук нажатия кнопок меню ---------------------------------------------------------------------------------------------
click = pygame.mixer.Sound(r'Music\zipclick.flac')

# Звук взмаха топором --------------------------------------------------------------------------------------------------
wave = pygame.mixer.Sound(r'Music\energichnyiy-rezkiy-vzmah-razrezayuschiy-vozduh.mp3')

# Звук шага ------------------------------------------------------------------------------------------------------------
step = pygame.mixer.Sound(r'Music\korotkiy-byistryiy-shag-po-lesu.mp3')

# Звук удара о дерево --------------------------------------------------------------------------------------------------
hit_tree = pygame.mixer.Sound(r'Music\korotkiy-chtkiy-rezkiy-udar-po-derevu.mp3')

# Звук падающего дерева ------------------------------------------------------------------------------------------------
falling_tree = pygame.mixer.Sound(r'Music\falling_tree.mp3')

# Звук агра монстров ---------------------------------------------------------------------------------------------------
agr_monster = pygame.mixer.Sound(r'Music\monster-grunt_zksbhlv_.mp3')

# Звук поедания яблока -------------------------------------------------------------------------------------------------
eat_apple = pygame.mixer.Sound(r'Music/the_sound_of_eating_an_apple.mp3')

# Звук выпивания кокоса
drink_coconut = pygame.mixer.Sound(r'Music/eat_coconut.mp3')

# Громкость звуков -----------------------------------------------------------------------------------------------------
volume_music = 1.0
volume_sounds = 1.0
volume_wave = 1.0
volume_hit_tree = 1.0
volume_agr_monster = 1.0
volume_falling_tree = 1.0
