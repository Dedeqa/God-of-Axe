import pygame
import func
import config as cfg
import images as img

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()


screen = pygame.display.set_mode(cfg.size)
pygame.display.set_caption("God of Axe")
pygame.display.set_icon(img.icon)

func.menu()
