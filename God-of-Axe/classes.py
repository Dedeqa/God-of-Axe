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
                if not (self.rect.colliderect(tree.line_right)):
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
                if not (self.rect.colliderect(tree.line_bottom)):
                    if self.rect.y >= 50:
                        self.speedy = -5
                    elif cfg.bg_y < 1080:
                        cfg.bg_y += 5
        if keystate[pygame.K_s]:
            if not (self.rect.colliderect(tree.line_top)):
                if self.rect.y <= 980:
                    self.speedy = 5
                elif cfg.bg_y > -1080:
                    cfg.bg_y -= 5
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        cfg.screen.fill("blue", tree.line_left)
        cfg.screen.fill("blue", tree.line_right)
        cfg.screen.fill("blue", tree.line_top)
        cfg.screen.fill("blue", tree.line_bottom)


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
        self.rect = self.image.get_rect()
        self.line_width = self.rect[2]
        self.line_height = self.rect[3]/6
        self.rect.topleft = (posx, posy)
        # self.rect_ph = pygame.Rect(posx, (self.rect.bottomleft[1] - posy) / 4 * 3 + posy, self.rect[2], self.rect[3]/6)
        self.line_left = pygame.Rect(posx, self.rect.bottomleft[1] - self.line_height, 1, self.line_height)

        self.line_right = pygame.Rect(posx + self.rect[2], (self.rect.bottomleft[1] - posy) / 4 * 3 + posy, 1,
                                      self.rect[3] / 6)
        self.line_top = pygame.Rect(posx, (self.rect.bottomleft[1] - posy) / 4 * 3 + posy, self.rect[2], 1)
        self.line_bottom = pygame.Rect(posx, (self.rect.bottomleft[1] - posy) / 4 * 3 + posy + self.rect[3] / 6,
                                       self.rect[2],
                                       1)

    def update(self):
        self.rect.x = cfg.bg_x + self.posx
        self.rect.y = cfg.bg_y + self.posy
        # self.line_left[0] = cfg.bg_x + self.posx
        # self.line_left[1] = cfg.bg_y + self.rect.y
        # self.line_right[0] += cfg.bg_x
        # self.line_right[1] += cfg.bg_y
        # self.line_top[0] += cfg.bg_x
        # self.line_top[1] += cfg.bg_y
        # self.line_bottom[0] += cfg.bg_x
        # self.line_bottom[1] += cfg.bg_y

    def take_dmg(self, dmg):
        self.hp -= dmg
        if self.hp <= 0:
            self.kill()


tree = Tree("Bereza", 100000, 960, 800, 5)
all_sprites.add(tree)
