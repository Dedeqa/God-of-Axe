import pygame
import func
import config as cfg
import time


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
        self.image = pygame.image.load('Images/Player/Woodcutter_right.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (posx / 2, posy / 2)
        self.weapon = Weapon(100, 1000)
        self.speedx = 0
        self.speedy = 0
        self.i = 0
        self.at = 0

    def update(self):
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if not (keystate[pygame.K_a] and keystate[pygame.K_d]):
            if keystate[pygame.K_a]:
                cfg.vector = "left"
                if not (self.rect.colliderect(tree.line_right)):
                    if keystate[pygame.K_LSHIFT]:
                        if self.i == 6:
                            self.i = 0
                        self.image = cfg.woodcutter_run_left[self.i]
                        self.i += 1

                        sx = 10
                    else:
                        if self.i == 6:
                            self.i = 0
                        self.image = cfg.woodcutter_walk_left[self.i]
                        self.i += 1

                        sx = 5
                    if self.rect.x >= 50:
                        self.speedx = -sx
                    elif cfg.bg_x < 1920:
                        cfg.bg_x += sx
            if keystate[pygame.K_d]:
                cfg.vector = "right"
                if not (self.rect.colliderect(tree.line_left)):
                    if keystate[pygame.K_LSHIFT]:
                        if self.i == 6:
                            self.i = 0
                        self.image = cfg.woodcutter_run_right[self.i]
                        self.i += 1

                        sx = 10
                    else:
                        if self.i == 6:
                            self.i = 0
                        self.image = cfg.woodcutter_walk_right[self.i]
                        self.i += 1

                        sx = 5
                    if self.rect.x <= 1820:
                        self.speedx = sx
                    elif cfg.bg_x > -1920:
                        cfg.bg_x -= sx
        if not (keystate[pygame.K_w] and keystate[pygame.K_s]):
            if keystate[pygame.K_w]:
                if not (self.rect.colliderect(tree.line_bottom)):
                    if keystate[pygame.K_LSHIFT]:
                        if self.i == 6:
                            self.i = 0
                        if cfg.vector == "right":
                            self.image = cfg.woodcutter_run_right[self.i]
                        else:
                            self.image = cfg.woodcutter_run_left[self.i]
                        self.i += 1
                        sy = 10
                    else:
                        if self.i == 6:
                            self.i = 0
                        if cfg.vector == "right":
                            self.image = cfg.woodcutter_walk_right[self.i]
                        else:
                            self.image = cfg.woodcutter_walk_left[self.i]
                        self.i += 1

                        sy = 5
                    if self.rect.y >= 50:
                        self.speedy = -sy
                    elif cfg.bg_y < 1080:
                        cfg.bg_y += sy

                    # if self.rect.y >= 50:
                    #     self.speedy = -5
                    # elif cfg.bg_y < 1080:
                    #     cfg.bg_y += 5
            if keystate[pygame.K_s]:
                if not (self.rect.colliderect(tree.line_top)):
                    if keystate[pygame.K_LSHIFT]:
                        if self.i == 6:
                            self.i = 0
                        if cfg.vector == "right":
                            self.image = cfg.woodcutter_run_right[self.i]
                        else:
                            self.image = cfg.woodcutter_run_left[self.i]
                        self.i += 1
                        sy = 10
                    else:
                        if self.i == 6:
                            self.i = 0
                        if cfg.vector == "right":
                            self.image = cfg.woodcutter_walk_right[self.i]
                        else:
                            self.image = cfg.woodcutter_walk_left[self.i]
                        self.i += 1

                        sy = 5
                    if self.rect.y <= 980:
                        self.speedy = sy
                    elif cfg.bg_y > -1080:
                        cfg.bg_y -= sy
        if not (keystate[pygame.K_w] or keystate[pygame.K_s] or keystate[pygame.K_a] or keystate[pygame.K_d] or
                keystate[pygame.K_e]):
            if cfg.vector == "right":
                self.image = pygame.image.load('Images/Player/Woodcutter_right.png').convert_alpha()
            elif cfg.vector == "left":
                self.image = pygame.image.load('Images/Player/Woodcutter_left.png').convert_alpha()
        if keystate[pygame.K_e]:
            self.attack()
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # cfg.screen.fill("blue", tree.line_left)
        # cfg.screen.fill("blue", tree.line_right)
        # cfg.screen.fill("blue", tree.line_top)
        # cfg.screen.fill("blue", tree.line_bottom)
        pygame.time.delay(60)

    def attack(self):

        if cfg.vector == "right":
                self.image = cfg.woodcutter_attack_right[self.at]
        else:
            self.image = cfg.woodcutter_attack_left[self.at]
        self.at += 1
        if self.at == 5:
            self.at = 0

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
        self.line_left_x = posx + self.rect[2] / 3
        self.line_left_y = posy + self.rect[3] / 6 * 5 + 3
        self.line_right_x = self.line_left_x + self.rect[2] / 3
        self.line_right_y = posy + self.rect[3] / 6 * 5 + 3
        self.line_top_x = posx + self.rect[2] / 3 + 3
        self.line_top_y = posy + self.rect[3] / 6 * 5
        self.line_bottom_x = self.line_top_x
        self.line_bottom_y = posy + self.rect[3] / 6 * 5 + self.rect[3] / 9

        self.line_left = pygame.Rect(self.line_left_x, self.line_left_y, 1, self.rect[3] / 9 - 8)
        self.line_right = pygame.Rect(self.line_right_x, self.line_right_y, 1, self.rect[3] / 9 - 8)
        self.line_top = pygame.Rect(self.line_top_x, self.line_top_y, self.rect[2] / 3 - 8, 1)
        self.line_bottom = pygame.Rect(self.line_bottom_x, self.line_bottom_y, self.rect[2] / 3 - 8, 1)

    def update(self):
        self.rect.x = cfg.bg_x + self.posx
        self.rect.y = cfg.bg_y + self.posy
        self.line_left[0] = cfg.bg_x + self.line_left_x
        self.line_left[1] = cfg.bg_y + self.line_left_y
        self.line_right[0] = cfg.bg_x + self.line_right_x
        self.line_right[1] = cfg.bg_y + self.line_right_y
        self.line_top[0] = cfg.bg_x + self.line_top_x
        self.line_top[1] = cfg.bg_y + self.line_top_y
        self.line_bottom[0] = cfg.bg_x + self.line_bottom_x
        self.line_bottom[1] = cfg.bg_y + self.line_bottom_y

    def take_dmg(self, dmg):
        self.hp -= dmg
        if self.hp <= 0:
            self.kill()


tree = Tree("Bereza", 100000, 960, 800, 5)
all_sprites.add(tree)
