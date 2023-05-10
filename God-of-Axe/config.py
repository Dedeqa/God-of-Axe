import pygame
WIDTH = 1920
HEIGHT = 1080
FPS = 60
running = True
is_menu = True
is_fullscreen = False
screen = pygame.display.set_mode((WIDTH,HEIGHT), pygame.RESIZABLE)
current_size = screen.get_size()
last_size = current_size
info = pygame.display.Info()
FULLSCREEN_SIZE = (info.current_w, info.current_h)
screen = pygame.display.set_mode(FULLSCREEN_SIZE)
clock = pygame.time.Clock()
