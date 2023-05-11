import pygame

WIDTH = 1920
HEIGHT = 1080
FPS = 60
running = True
is_menu = True

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
current_size = screen.get_size()
last_size = current_size
info = pygame.display.Info()
size = (info.current_w, info.current_h)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
