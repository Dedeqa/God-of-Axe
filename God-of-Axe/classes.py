import pygame
import config as cfg
import sprite_func as func
import pygame.math as pm
import sounds
import images as img
import random


# pygame.mixer.pre_init(44100, -16, 1, 512)

class Unit:
    def __init__(self, nm, hp, posx, posy):
        self.name = nm
        self.hp = hp
        self.posx = posx
        self.posy = posy

    def draw_text(self, surf, text, size, x, y, font, color):
        font = pygame.font.Font(f'{font}', size)
        text_surface = font.render(text, True, f'{color}')
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        surf.blit(text_surface, text_rect)

    def draw_shield_bar(self, surf, x, y, pct, bg_color, bar_color, outline_color, k, bl, bh):
        if pct < 0:
            pct = 0
        BAR_LENGTH = bl
        BAR_HEIGHT = bh
        fill = (pct / k) * BAR_LENGTH
        outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
        fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
        pygame.draw.rect(surf, bg_color, outline_rect)
        pygame.draw.rect(surf, bar_color, fill_rect)
        pygame.draw.rect(surf, outline_color, outline_rect, 2)


class Player(Unit, pygame.sprite.Sprite):
    def __init__(self, nm, hp, posx, posy):

        Unit.__init__(self, nm, hp, posx, posy)
        pygame.sprite.Sprite.__init__(self)
        self.image = img.woodcutter_stay_right
        self.stamina = 100
        self.rect = self.image.get_rect()
        self.rect.center = (posx / 2, posy / 2)
        self.weapon = Weapon(100, 1000)
        self.speedx = 0
        self.speedy = 0
        self.i = 0
        self.j = 0
        self.at = 0
        self.flag_attack = False
        self.flag_take_dmg = False
        self.anim_time = 0
        self.anim_time_attack = 0
        self.wood_amount = 0
        self.oak_amount = 0
        self.fir_amount = 0
        self.progress = 0
        self.time_apple = cfg.current_time + 1000
        self.kills = 0

        self.apples_amount = 3
        self.rect_attack = pygame.Rect(self.rect[0] + self.rect[2] / 2 + 10, self.rect[1] + self.rect[3] / 3,
                                       self.rect[2] / 3 * 2,
                                       self.rect[3] / 3)
        self.line = pygame.Rect(self.rect[0] + self.rect[2] / 3, self.rect[1] + self.rect[3] / 6 - 5, self.rect[2] / 3,
                                self.rect[3] / 6 * 5)

    def update(self):


        self.progress = self.wood_amount * 100 / cfg.goal
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if self.stamina < 100 and not keystate[pygame.K_LSHIFT]:
            self.stamina += 0.5
        if not (keystate[pygame.K_a] and keystate[pygame.K_d]):

            if keystate[pygame.K_a]:
                cfg.vector = "left"

                if (self.line.collidelist(cfg.trees_rects_right)) == -1:
                    if keystate[pygame.K_LSHIFT] and self.stamina > 0:

                        if self.i == 6:
                            self.i = 0

                        self.image = img.woodcutter_run_left[self.i]
                        self.anim_time += 1

                        if self.anim_time == 5:
                            self.i += 1
                            self.anim_time = 0
                        sx = 4
                        self.stamina -= 0.5

                    else:

                        if self.i == 6:
                            self.i = 0

                        # if self.i == 1 or self.i == 4:
                        #     sounds.step.stop()
                        #     sounds.step.play()

                        self.image = img.woodcutter_walk_left[self.i]
                        self.anim_time += 1

                        if self.anim_time == 5:
                            self.i += 1
                            self.anim_time = 0

                        sx = 2
                    if self.rect.x >= 50:
                        self.speedx = -sx
                    elif cfg.bg_x < 1920:
                        cfg.bg_x += sx
                        func.update_monsters_x(cfg.monsterList, sx, flag_direction=True)
            if keystate[pygame.K_d]:
                cfg.vector = "right"
                if (self.line.collidelist(cfg.trees_rects_left)) == -1:
                    if keystate[pygame.K_LSHIFT] and self.stamina > 0:

                        if self.i == 6:
                            self.i = 0

                        self.image = img.woodcutter_run_right[self.i]
                        self.anim_time += 1

                        if self.anim_time == 5:
                            self.i += 1
                            self.anim_time = 0

                        sx = 4
                        self.stamina -= 0.5
                    else:

                        if self.i == 6:
                            self.i = 0

                        self.image = img.woodcutter_walk_right[self.i]
                        self.anim_time += 1

                        if self.anim_time == 5:
                            self.i += 1
                            self.anim_time = 0

                        sx = 1
                    if self.rect.x <= 1820:
                        self.speedx = sx
                    elif cfg.bg_x > -1920:
                        cfg.bg_x -= sx
                        func.update_monsters_x(cfg.monsterList, sx, flag_direction=False)
        if not (keystate[pygame.K_w] and keystate[pygame.K_s]):
            if keystate[pygame.K_w]:
                if (self.line.collidelist(cfg.trees_rects_bottom)) == -1:
                    if keystate[pygame.K_LSHIFT] and self.stamina > 0:

                        if self.j == 6:
                            self.j = 0

                        if cfg.vector == "right":
                            self.image = img.woodcutter_run_right[self.j]
                        else:
                            self.image = img.woodcutter_run_left[self.j]
                        self.anim_time += 1

                        if self.anim_time == 5:
                            self.j += 1
                            self.anim_time = 0

                        sy = 4
                        self.stamina -= 0.5
                    else:

                        if self.j == 6:
                            self.j = 0

                        if cfg.vector == "right":
                            self.image = img.woodcutter_walk_right[self.j]
                        else:
                            self.image = img.woodcutter_walk_left[self.j]
                        self.anim_time += 1

                        if self.anim_time == 5:
                            self.j += 1
                            self.anim_time = 0

                        sy = 2
                    if self.rect.y >= 50:
                        self.speedy = -sy
                    elif cfg.bg_y < 1080:
                        cfg.bg_y += sy
                        func.update_monsters_y(cfg.monsterList, sy, flag_direction=True)
            if keystate[pygame.K_s]:
                if (self.line.collidelist(cfg.trees_rects_top)) == -1:
                    if keystate[pygame.K_LSHIFT] and self.stamina > 0:

                        if self.j == 6:
                            self.j = 0

                        if cfg.vector == "right":
                            self.image = img.woodcutter_run_right[self.j]
                        else:
                            self.image = img.woodcutter_run_left[self.j]
                        self.anim_time += 1

                        if self.anim_time == 5:
                            self.j += 1
                            self.anim_time = 0

                        sy = 4
                        self.stamina -= 0.5
                    else:

                        if self.j == 6:
                            self.j = 0

                        if cfg.vector == "right":
                            self.image = img.woodcutter_walk_right[self.j]
                        else:
                            self.image = img.woodcutter_walk_left[self.j]
                        self.anim_time += 1

                        if self.anim_time == 5:
                            self.j += 1
                            self.anim_time = 0

                        sy = 2
                    if self.rect.y <= 980:
                        self.speedy = sy
                    elif cfg.bg_y > -1080:
                        cfg.bg_y -= sy
                        func.update_monsters_y(cfg.monsterList, sy, flag_direction=False)
        if keystate[pygame.K_e]:
            self.eat_an_apple()
        if not (keystate[pygame.K_w] or keystate[pygame.K_s] or keystate[pygame.K_a] or keystate[pygame.K_d] or
                keystate[pygame.K_SPACE] or self.flag_take_dmg):
            if cfg.vector == "right":
                self.image = img.woodcutter_stay_right
            elif cfg.vector == "left":
                self.image = img.woodcutter_stay_left

        if keystate[pygame.K_SPACE] and self.stamina >= 10:
            self.flag_attack = True
        self.attack()
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # self.line_y[0] += self.speedx
        # self.line_y[1] += self.speedy
        self.line[0] += self.speedx
        self.line[1] += self.speedy

        # cfg.screen.fill("red", self.rect)
        # cfg.screen.fill("orange", self.rect_attack)
        # cfg.screen.fill("orange", self.line)
        # for elem in cfg.trees1:
        #     cfg.screen.fill("blue", elem.line_right)
        #     cfg.screen.fill("blue", elem.line_left)
        #     cfg.screen.fill("blue", elem.line_top)
        #     cfg.screen.fill("blue", elem.line_bottom)

    def attack(self):
        if self.flag_attack:
            self.stamina -= 1
            if self.at == 0:
                sounds.wave.stop()
                sounds.wave.play()

            if cfg.vector == "right":
                self.image = img.woodcutter_attack_right[self.at]
                self.anim_time_attack += 1

                if self.anim_time_attack == 5:
                    self.at += 1
                    self.anim_time_attack = 0

                if self.at == 6:
                    self.at = 0
                    for elem in cfg.trees1:
                        if self.rect_attack.colliderect(elem):
                            elem.take_dmg(self.weapon.damage)
                    for elem in cfg.trees2:
                        if self.rect_attack.colliderect(elem):
                            elem.take_dmg(self.weapon.damage)
                    for elem in cfg.monsterList:
                        if self.rect_attack.colliderect(elem):
                            elem.take_dmg(self.weapon.damage)

                    self.flag_attack = False
            else:

                self.image = img.woodcutter_attack_left[self.at]
                self.anim_time_attack += 1

                if self.anim_time_attack == 5:
                    self.at += 1
                    self.anim_time_attack = 0

                if self.at == 6:
                    self.at = 0
                    for elem in cfg.trees1:
                        if self.rect_attack.colliderect(elem):
                            elem.take_dmg(self.weapon.damage)
                    for elem in cfg.trees2:
                        if self.rect_attack.colliderect(elem):
                            elem.take_dmg(self.weapon.damage)
                    for elem in cfg.monsterList:
                        if self.rect_attack.colliderect(elem):
                            elem.take_dmg(self.weapon.damage)
                    self.flag_attack = False

            if cfg.vector == 'right':
                self.rect_attack = pygame.Rect(self.rect[0] + self.rect[2] / 2 + 10, self.rect[1] + self.rect[3] / 3,
                                               self.rect[2] / 3 * 2,
                                               self.rect[3] / 3)
            else:
                self.rect_attack = pygame.Rect(self.rect[0] - self.rect[2] / 3, self.rect[1] + self.rect[3] / 3,
                                               self.rect[2] / 3 * 2,
                                               self.rect[3] / 3)

    def take_dmg(self, dmg):
        if self.hp > 0:
            self.flag_take_dmg = True
            self.hp -= dmg
            sounds.hit_tree.play()
        if self.hp <= 0:
            self.remove(all_sprites)
            self.kill()

    def eat_an_apple(self):
        if self.time_apple < cfg.current_time:
            if self.apples_amount > 0 and self.hp < 100:
                self.hp += 10
                self.apples_amount -= 1
                sounds.eat_apple.play()
                self.time_apple = cfg.current_time + 1000


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
        self.line_right_x = self.line_left_x + self.rect[2] / 3 - 5
        self.line_right_y = posy + self.rect[3] / 6 * 5 + 3
        self.line_top_x = posx + self.rect[2] / 3 + 3
        self.line_top_y = posy + self.rect[3] / 6 * 5 - 3
        self.line_bottom_x = self.line_top_x
        self.line_bottom_y = posy + self.rect[3] / 6 * 5 + self.rect[3] / 9
        self.bonus = bonus
        self.line_left = pygame.Rect(self.line_left_x - 3, self.line_left_y + 3, 5, self.rect[3] / 9 - 5)
        self.line_right = pygame.Rect(self.line_right_x, self.line_right_y, 5, self.rect[3] / 9 - 5)
        self.line_top = pygame.Rect(self.line_top_x, self.line_top_y, self.rect[2] / 3 - 8, 5)
        self.line_bottom = pygame.Rect(self.line_bottom_x, self.line_bottom_y, self.rect[2] / 3 - 8, 5)
        self.player_vector = (0, 0)
        self.tree_vector = (0, 0)
        self.start_hp = hp

    def update(self):

        self.player_vector = pm.Vector2(player.rect.x, player.rect.y)
        self.tree_vector = pm.Vector2(self.rect.centerx, self.rect.y + 70)
        distance = self.tree_vector.distance_to(self.player_vector)

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

        if distance <= 110:
            self.draw_shield_bar(cfg.screen, self.rect.x + 25, self.rect.y - 10, self.hp, (92, 69, 10), (140, 104, 13),
                                 "black",
                                 self.start_hp, 50, 10)

    def take_dmg(self, dmg):

        if self.hp > 0:
            self.status = True
            self.hp -= dmg
            sounds.hit_tree.play()
        if self.hp <= 0:
            if self.status:
                sounds.falling_tree.play()

            self.remove(all_sprites)
            self.kill()
            self.give_an_apple()
            self.status = False
            self.line_left[2] = 0
            self.line_left[3] = 0
            self.line_right[2] = 0
            self.line_right[3] = 0
            self.line_top[2] = 0
            self.line_top[3] = 0
            self.line_bottom[2] = 0
            self.line_bottom[3] = 0
            player.wood_amount += self.bonus
            if self.bonus == 10:
                player.fir_amount += 1
            elif self.bonus == 5:
                player.oak_amount += 1
            self.bonus = 0

    def give_an_apple(self):
        if self.status:
            chance = 0
            if self.bonus == 5:
                chance = random.randint(1, 5)
            elif self.bonus == 10:
                chance = random.randint(1, 2)
            if chance == 1:
                player.apples_amount += 1
