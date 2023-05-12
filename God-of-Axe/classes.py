import pygame
import func
import config as cfg


class Unit:
    def __init__(self, nm, hp, posx, posy):
        self.name = nm
        self.hp = hp
        self.posx = posx
        self.posy = posy


class Player(Unit, pygame.sprite.Sprite):
    def __init__(self, nm, hp, posx, posy):
        Unit.__init__(self, nm, hp, posx, posy)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Images/minotaur-N-stand.png')

        self.rect = self.image.get_rect()
        self.rect.center = (posx / 2, posy / 2)
        self.weapon = Weapon(10)
        self.speedx = 0
        self.speedy = 0

    def update(self):
        self.speedx = 0
        self.speedy = 0

        keystate = pygame.key.get_pressed()
        if not (keystate[pygame.K_a] and keystate[pygame.K_d]):
            if keystate[pygame.K_a]:
                if self.rect.x >= 50:
                    self.speedx = -5
                elif cfg.bg_x < 1920:
                    cfg.bg_x += 5
            if keystate[pygame.K_d]:
                if self.rect.x <= 1820:
                    self.speedx = 5
                elif cfg.bg_x > -1920:
                    cfg.bg_x -= 5
                    print(cfg.bg_x)

        if not (keystate[pygame.K_w] and keystate[pygame.K_s]):
            if keystate[pygame.K_w]:
                if self.rect.y >= 50:
                    self.speedy = -5
                elif cfg.bg_y < 1080:
                    cfg.bg_y += 5
            if keystate[pygame.K_s]:
                if self.rect.y <= 980:
                    self.speedy = 5
                elif cfg.bg_y > -1080:
                    cfg.bg_y -= 5
        self.rect.x += self.speedx
        self.rect.y += self.speedy

    # # def attack(self):


class Weapon:
    def __init__(self, dmg):
        self.name = "Axe"
        self.damage = dmg

    def dmg_up(self):
        self.damage += 5


# Экземпляр класса Player() -----------------------------------------------------------------------
all_sprites = pygame.sprite.Group()
player = Player("Albert", 100, cfg.WIDTH, cfg.HEIGHT)
all_sprites.add(player)
#--------------------------------------------------------------------------------------------------

class Tree(Unit, pygame.sprite.Sprite):
    def __init__(self, nm, hp, posx, posy, bonus):
        Unit.__init__(self, nm, hp, posx, posy)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Images/Trees/Tree1.png")
        self.rect = self.image.get_rect()
        self.rect.center = (posx, posy)
        self.bonus = bonus
    def update(self):
        self.rect.x = cfg.bg_x + self.posx
        self.rect.y = cfg.bg_y + self.posy

tree = Tree("Bereza", 300, 960, 800, 5)
all_sprites.add(tree)
