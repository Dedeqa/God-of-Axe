import pygame
import config as cfg
import classes as cl
import math


class Monster(cl.Unit, pygame.sprite.Sprite):
    def __init__(self, nm, hp, posx, posy):
        cl.Unit.__init__(self, nm, hp, posx, posy)
        pygame.sprite.Sprite.__init__(self)
        self.image = cfg.minotaur_walk_bottom[0]
        self.rect = self.image.get_rect()
        self.rect.center = (posx, posy)
        self.speed = 1
        self.speedx = 0
        self.speedy = 0
        self.kx = 0
        self.ky = 0
    def update(self):
        if self.posx <= cl.player.rect.centerx:
            self.kx = 1
            dx = cl.player.rect.centerx - self.posx
        else:
            self.kx = -1
            dx = self.posx - cl.player.rect.centerx
        if self.posy <= cl.player.rect.centery:
            self.ky = 1
            dy = cl.player.rect.centery - self.posy
        else:
            self.ky = -1
            dy = self.posy - cl.player.rect.centery
        if dx == 0:
            self.speedx = 0
            self.speedy = self.speed * self.ky
        elif dy == 0:
            self.speedy = 0
            self.speedx = self.speed * self.kx
        else:
            a = math.atan(dy / dx)
            self.speedx = self.speed * math.cos(a)
            self.speedy = self.speed * math.sin(a)
        self.rect.x += math.ceil(self.speedx)
        self.rect.y += math.ceil(self.speedy)

min1 = Monster("Jaba", 100, 1, 1)
cl.all_sprites.add(min1)