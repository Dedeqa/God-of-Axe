import pygame
import config as cfg
import sprite_func as func
import pygame.math as pm
import sounds
import images as img
import random

pygame.mixer.pre_init(44100, -16, 1, 512)


class Unit:
    def __init__(self, nm, hp, posx, posy):
        self.name = nm
        self.hp = hp
        self.posx = posx
        self.posy = posy

    def draw_text(self, surf, text, size, x, y, font, color):
        font = pygame.font.Font(font, size)
        text_surface = font.render(text, True, color)
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
        self.armor = 25
        self.stamina_recovery = 0.5
        self.rect = self.image.get_rect()
        self.rect.center = (posx / 2, posy / 2)
        self.weapon = Weapon(100, 1000)
        self.speedx = 0
        self.speedy = 0
        self.i = 0
        self.j = 0
        self.at = 0

        self.death_timer = cfg.current_time + 100
        self.death_index = 0

        self.flag_attack = False
        self.flag_take_dmg = False
        self.anim_time = 0
        self.anim_time_attack = 0

        self.wood_amount = 0
        self.oak_amount = 0
        self.fir_amount = 0
        self.palm_amount = 0
        self.progress = 0

        self.time_apple = cfg.current_time + 1000
        self.time_shishka = cfg.current_time + 1000
        self.time_coconut = cfg.current_time + 1000

        self.coconut_timer = self.time_coconut + 7000

        self.kills = 0

        self.utilities = [3, 0, 0]

        self.rect_attack = pygame.Rect(self.rect[0] + self.rect[2] / 2 + 10, self.rect[1] + self.rect[3] / 3,
                                       self.rect[2] / 3 * 2,
                                       self.rect[3] / 3)
        self.line = pygame.Rect(self.rect[0] + self.rect[2] / 3, self.rect[1] + self.rect[3] / 6 - 5, self.rect[2] / 3,
                                self.rect[3] / 6 * 5)

    def update(self):

        if self.coconut_timer < cfg.current_time:
            self.stamina_recovery = 0.5
        self.progress = self.wood_amount * 100 / cfg.goal
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if self.stamina < 100 and not keystate[pygame.K_LSHIFT]:
            self.stamina += self.stamina_recovery
        elif self.stamina > 100:
            self.stamina = 100
        if self.hp > 0:
            if not (keystate[pygame.K_a] and keystate[pygame.K_d]):

                if keystate[pygame.K_a]:
                    cfg.vector = "left"

                    if (self.line.collidelist(cfg.trees_rects_right)) == -1 and not self.line.colliderect(
                            house.line_right):
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
                        if self.rect.x >= 100:
                            self.speedx = -sx
                        elif cfg.bg_x < 1820:
                            cfg.bg_x += sx
                            func.update_monsters_x(cfg.monsterList, sx, flag_direction=True)
                if keystate[pygame.K_d]:
                    cfg.vector = "right"
                    if (self.line.collidelist(cfg.trees_rects_left)) == -1 and not self.line.colliderect(
                            house.line_left):
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

                            sx = 2
                        if self.rect.x <= 1820:
                            self.speedx = sx
                        elif cfg.bg_x > -1820:
                            cfg.bg_x -= sx
                            func.update_monsters_x(cfg.monsterList, sx, flag_direction=False)
            if not (keystate[pygame.K_w] and keystate[pygame.K_s]):
                if keystate[pygame.K_w]:
                    if (self.line.collidelist(cfg.trees_rects_bottom)) == -1 and not self.line.colliderect(
                            house.line_bottom):
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
                        if self.rect.y >= 100:
                            self.speedy = -sy
                        elif cfg.bg_y < 1080:
                            cfg.bg_y += sy
                            func.update_monsters_y(cfg.monsterList, sy, flag_direction=True)
                if keystate[pygame.K_s]:
                    if (self.line.collidelist(cfg.trees_rects_top)) == -1 and not self.line.colliderect(house.line_top):
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
            if keystate[pygame.K_c]:
                self.eat_an_apple()

            if keystate[pygame.K_z]:
                self.eat_a_coconut()

            if keystate[pygame.K_x]:
                self.eat_a_shishka()

            if keystate[pygame.K_e] and (
                    self.line.colliderect(house.line_left) or self.line.colliderect(house.line_right) or
                    self.line.colliderect(house.line_bottom) or self.line.colliderect(house.line_top)):
                cfg.workshop_flag = True
            elif not (self.line.colliderect(house.line_left) or self.line.colliderect(house.line_right) or
                    self.line.colliderect(house.line_bottom) or self.line.colliderect(house.line_top)):
                cfg.workshop_flag = False

            if not (keystate[pygame.K_w] or keystate[pygame.K_s] or keystate[pygame.K_a] or keystate[pygame.K_d] or
                    keystate[pygame.K_SPACE] or self.flag_take_dmg):
                if cfg.vector == "right":
                    self.image = img.woodcutter_stay_right
                elif cfg.vector == "left":
                    self.image = img.woodcutter_stay_left

            if keystate[pygame.K_SPACE] and self.stamina >= 10:
                self.flag_attack = True
            self.attack()
        else:

            if cfg.vector == "right":
                if self.death_index < 7 and self.death_timer < cfg.current_time:

                    if self.death_index <= 5:
                        self.image = img.woodcutter_death_right[self.death_index]
                        self.death_timer = cfg.current_time + 100
                    else:
                        self.death_timer = cfg.current_time + 1000
                    self.death_index += 1
                elif self.death_index == 7 and self.death_timer < cfg.current_time:
                    self.remove(all_sprites)
                    self.kill()
                    cfg.lose_flag = True
            elif cfg.vector == "left":
                if self.death_index < 7 and self.death_timer < cfg.current_time:

                    if self.death_index <= 5:
                        self.image = img.woodcutter_death_left[self.death_index]
                        self.death_timer = cfg.current_time + 100
                    else:
                        self.death_timer = cfg.current_time + 1000
                    self.death_index += 1
                elif self.death_index == 7 and self.death_timer < cfg.current_time:
                    self.remove(all_sprites)
                    self.kill()
                    cfg.lose_flag = True

        self.rect.x += self.speedx
        self.rect.y += self.speedy

        self.line[0] += self.speedx
        self.line[1] += self.speedy

        # cfg.screen.fill("red", self.rect)
        # cfg.screen.fill("orange", self.rect_attack)
        # cfg.screen.fill("orange", self.line)
        for elem in cfg.trees1:
            cfg.screen.fill("blue", elem.line_right)
            cfg.screen.fill("blue", elem.line_left)
            cfg.screen.fill("blue", elem.line_top)
            cfg.screen.fill("blue", elem.line_bottom)
        for elem in cfg.trees2:
            cfg.screen.fill("blue", elem.line_right)
            cfg.screen.fill("blue", elem.line_left)
            cfg.screen.fill("blue", elem.line_top)
            cfg.screen.fill("blue", elem.line_bottom)
        for elem in cfg.trees3:
            cfg.screen.fill("blue", elem.line_right)
            cfg.screen.fill("blue", elem.line_left)
            cfg.screen.fill("blue", elem.line_top)
            cfg.screen.fill("blue", elem.line_bottom)

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
                    for elem in cfg.trees3:
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
                    for elem in cfg.trees3:
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

        self.flag_take_dmg = True

        if self.armor > 0:
            self.hp -= dmg - (self.armor / 100) * dmg
            self.armor -= dmg // 2
        elif self.armor <= 0:
            self.hp -= dmg

        if self.hp > 0:
            sounds.take_dmg_sounds_list[sounds.index].play()
            sounds.index += 1

            if sounds.index == 3:
                sounds.index = 0
        else:
            sounds.last_hit.play()

    def eat_an_apple(self):
        if self.time_apple < cfg.current_time:
            if self.utilities[0] > 0 and self.hp < 100:
                if self.hp + 10 <= 100:
                    self.hp += 10
                elif self.hp + 10 > 100:
                    self.hp = 100
                self.utilities[0] -= 1
                sounds.eat_apple.play()
                self.time_apple = cfg.current_time + 1000

    def eat_a_shishka(self):
        if self.time_shishka < cfg.current_time:
            if self.utilities[1] > 0 and self.armor < 100:
                if self.armor + 25 <= 100:
                    self.armor += 25
                elif self.armor + 25 > 100:
                    self.armor = 100
                self.utilities[1] -= 1
                sounds.falling_tree.play()
                self.time_shishka = cfg.current_time + 1000
        elif self.armor > 100:
            self.armor = 100

    def eat_a_coconut(self):

        if self.time_coconut < cfg.current_time:
            if self.utilities[2] > 0:
                self.utilities[2] -= 1
                self.stamina_recovery = 1.5
                sounds.drink_coconut.play()
                self.time_coconut = cfg.current_time + 5100
                self.coconut_timer = self.time_coconut


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

    def __init__(self, nm, hp, posx, posy, bonus, drop, random_index):

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

        self.drop = drop
        self.random_index = random_index

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
            self.give_drop()
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
            elif self.bonus == 25:
                player.palm_amount += 1
            self.bonus = 0

    def give_drop(self):

        if self.status:

            chance = random.randint(1, 100)

            if 0 <= chance <= cfg.temp_random_list[self.random_index]:
                player.utilities[self.drop] += 1
                cfg.temp_random_list[self.random_index] = cfg.random_list[self.random_index]
            else:
                cfg.temp_random_list[self.random_index] += 10


class Dub(Tree):
    def __init__(self, nm, hp, posx, posy, bonus, drop=0, random_index=0):
        Tree.__init__(self, nm, hp, posx, posy, bonus, drop, random_index)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Images/Trees/Tree1.png").convert_alpha()


class Elka(Tree):
    def __init__(self, nm, hp, posx, posy, bonus, drop=1, random_index=1):
        Tree.__init__(self, nm, hp, posx, posy, bonus, drop, random_index)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Images/Trees/Tree2.png").convert_alpha()


class Palma(Tree):
    def __init__(self, nm, hp, posx, posy, bonus, drop=2, random_index=2):
        Tree.__init__(self, nm, hp, posx, posy, bonus, drop, random_index)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Images/Trees/Tree3.png").convert_alpha()


class House(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        self.posx = posx
        self.posy = posy
        self.image = img.house_icon
        self.rect = self.image.get_rect()
        self.rect.center = (posx, posy)

        self.line_left = pygame.Rect(self.posx - 10, self.posy + 60, 1, self.rect[3] - 60)
        self.line_right = pygame.Rect(posx + self.rect[2] - 30, posy + 60, 1, self.rect[3] - 60)
        self.line_top = pygame.Rect(self.posx - 10, self.posy + 60, self.rect[2] - 20, 1)
        self.line_bottom = pygame.Rect(self.posx - 10, self.posy + self.rect[3], self.rect[2] - 20, 1)
        print(self.rect)

    def update(self):
        self.rect.x = self.posx + cfg.bg_x
        self.rect.y = self.posy + cfg.bg_y
        cfg.screen.fill("red", self.line_left)
        cfg.screen.fill("red", self.line_right)
        cfg.screen.fill("red", self.line_top)
        cfg.screen.fill("red", self.line_bottom)
        # self.line_left.x = self.line_left_x + cfg.bg_x
        # self.line_left.y = self.line_left_y + cfg.bg_y
        # self.line_right.x = self.line_right_x + cfg.bg_x
        # self.line_right.y = self.line_right_y + cfg.bg_y
        self.line_right.x = self.posx + self.rect[2] - 30 + cfg.bg_x
        self.line_right.y = self.posy + 60 + cfg.bg_y
        self.line_left.x = self.posx - 10 + cfg.bg_x
        self.line_left.y = self.posy + 60 + cfg.bg_y
        self.line_top.x = self.posx - 10 + cfg.bg_x
        self.line_top.y = self.posy + 60 + cfg.bg_y
        self.line_bottom.x = self.posx - 10 + cfg.bg_x
        self.line_bottom.y = self.posy + self.rect[3] + cfg.bg_y
        # # self.line_right.y = cfg.bg_y + self.posy
        # # self.line_left.x = cfg.bg_x + self.posx
        # # self.line_left.y = cfg.bg_y +self.posy


house = House(960, 200)
all_sprites.add(house)
