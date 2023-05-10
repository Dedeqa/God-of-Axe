import pygame
WIDTH = 700
HEIGHT = 500
FPS = 60
running = True
is_menu = True
is_fullscreen = False
screen = pygame.display.set_mode((WIDTH,HEIGHT), pygame.RESIZABLE)
current_size = screen.get_size()
last_size = current_size
