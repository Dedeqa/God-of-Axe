import pygame
import func


class Unit:
    def __init__(self, nm, hp):
        self.name = nm
        self.hp = hp


class Player(Unit, pygame.sprite.Sprite):
    def __init__(self, nm, width, height):
        Unit.__init__(self, nm, 100)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill('Black')
        self.rect = self.image.get_rect()
        self.rect.center = (width / 2, height / 2)
        self.weapon = Weapon(10)
        self.speedx = 0
        self.speedy = 0

    def update(self):
        global i
        self.speedx = 0
        self.speedy = 0

        keystate = pygame.key.get_pressed()
        if not (keystate[pygame.K_a] and keystate[pygame.K_d]):
            if keystate[pygame.K_a]:
                self.speedx = -5
                # self.image = walk_left[i]
                # if i == 4:
                #     i = 0
                # else:
                #     i += 1
            if keystate[pygame.K_d]:
                self.speedx = 5
                # self.image = walk_right[i]
                # if i == 4:
                #     i = 0
                # else:
                #     i += 1
        if not (keystate[pygame.K_w] and keystate[pygame.K_s]):
            if keystate[pygame.K_w]:
                self.speedy = -5
                # self.image = walk_back[i]
                # if i == 4:
                #     i = 0
                # else:
                #     i += 1
            elif keystate[pygame.K_s]:
                self.speedy = 5
                # self.image = walk_forward[i]
                # if i == 4:
                #     i = 0
                # else:
                #     i += 1
        self.rect.x += self.speedx
        self.rect.y += self.speedy
    # def attack(self):


class Weapon:
    def __init__(self, dmg):
        self.name = "Axe"
        self.damage = dmg

    def dmg_up(self):
        self.damage += 5
