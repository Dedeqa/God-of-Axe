import pygame
import func
import config

pygame.init()

info = pygame.display.Info()
size = (info.current_w, info.current_h)

screen = pygame.display.set_mode(size)
current_size = screen.get_size()
last_size = current_size

pygame.display.set_caption("God of Axe")

# ---------------------------- Иконка игры -----------------------------

pygame.display.set_icon(config.icon)

func.menu()
