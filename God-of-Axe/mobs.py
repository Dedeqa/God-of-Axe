import pygame
import config as cfg
import classes as cl

class Monster(cl.Unit, pygame.sprite.Sprite):
    def __init__(self, nm, hp, posx, posy):
        cl.Unit.__init__(self, nm, hp, posx, posy)
        pygame.sprite.Sprite.__init__(self)
