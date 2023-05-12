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
        self.image = pygame.image.load('Images/minotaur-N-stand.png').convert_alpha()
        # self.image.fill("Orange")

        self.rect = self.image.get_rect()
        self.rect.center = (posx / 2, posy / 2)
        self.weapon = Weapon(100, 1000)
        self.speedx = 0
        self.speedy = 0

    def update(self):
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if not (keystate[pygame.K_a] and keystate[pygame.K_d]):
            if keystate[pygame.K_a]:
                print(tree.rect.x + tree.rect.topright[0], self.rect.y)
                # if not (self.rect.colliderect()):
                if self.rect.x >= 50:
                    self.speedx = -5
                elif cfg.bg_x < 1920:
                    cfg.bg_x += 5
            if keystate[pygame.K_d]:
                if not (self.rect.colliderect(tree.line_left)):
                    if self.rect.x <= 1820:
                        self.speedx = 5
                    elif cfg.bg_x > -1920:
                        cfg.bg_x -= 5

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
    def __init__(self, dmg, attack_speed):
        self.name = "Axe"
        self.damage = dmg
        self.attack_speed = attack_speed

    def dmg_up(self):
        self.damage += 5


# Экземпляр класса Player() -----------------------------------------------------------------------
all_sprites = pygame.sprite.Group()
player = Player("Albert", 100, cfg.WIDTH, cfg.HEIGHT)
all_sprites.add(player)


# --------------------------------------------------------------------------------------------------

class Tree(Unit, pygame.sprite.Sprite):
    def __init__(self, nm, hp, posx, posy, bonus):
        Unit.__init__(self, nm, hp, posx, posy)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Images/Trees/Tree1.png").convert_alpha()
        # self.image.fill("red")
        print(self.image.get_rect())
        self.rect = self.image.get_rect()
        self.rect.center = (posx, posy)
        self.line_left = pygame.Rect(posx, posy + self.image.get_rect()[3] / 4 * 3, posx + self.image.get_rect()[2],
                                     posy + self.image.get_rect()[3])

    def update(self):
        self.rect.x = cfg.bg_x + self.posx
        self.rect.y = cfg.bg_y + self.posy
        self.line_left[0] = cfg.bg_x + self.posx
        self.line_left[1] = cfg.bg_y + self.posy
        self.line_left[2] = cfg.bg_x + self.posx
        self.line_left[3] = cfg.bg_y + self.posy

    def take_dmg(self, dmg):
        self.hp -= dmg
        if self.hp <= 0:
            self.kill()


tree = Tree("Bereza", 100000, 960, 800, 5)
all_sprites.add(tree)
