import pygame
import func
import config

pygame.init()

screen = pygame.display.set_mode(config.size)
pygame.display.set_caption("God of Axe")
pygame.display.set_icon(config.icon)

func.menu()
