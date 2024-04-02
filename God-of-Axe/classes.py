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

    def __del__(self):
        pass

    def draw_text(self, surf, text, size, x, y, font, color):
        font = pygame.font.Font(font, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        surf.blit(text_surface, text_rect)

    def draw_info_bar(self, surf, x, y, cur_value, bg_color, bar_color, outline_color, max_value, bar_length,
                      bar_height):
        if cur_value < 0:
            cur_value = 0
        BAR_LENGTH = bar_length
        BAR_HEIGHT = bar_height
        fill = (cur_value / max_value) * BAR_LENGTH
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
        self.rect.center = (posx / 2, posy / 2)  # место спавна героя
        self.weapon = Weapon(100, 1000)
        self.speed_x = 0
        self.speed_y = 0

        self.bg_x = cfg.bg_x
        self.bg_y = cfg.bg_y

        self.anim_counter_x = 0
        self.anim_counter_y = 0  # счетчики для анимации движения, атаки и смерти героя
        self.anim_counter_attack = 0
        self.anim_counter_death = 0

        self.death_delay = cfg.in_game_time + 100  # задержка после смерти для анимации

        self.flag_attack = False
        self.flag_take_dmg = False

        self.move_anim_delay = 0
        self.attack_anim_delay = 0

        self.wood_amount = 0
        self.oak_amount = 0
        self.fir_amount = 0
        self.palm_amount = 0

        self.progress = 0

        self.coins = 0

        self.apple_eat_time = cfg.in_game_time + 1000
        self.shishka_eat_time = cfg.in_game_time + 1000  # время приема пищи
        self.coconut_eat_time = cfg.in_game_time + 1000

        self.coconut_boost_time = self.coconut_eat_time + 7000  # время действия эффекта кокоса

        self.kills = 0

        self.utilities = [3, 0, 0]

        self.rect_attack = pygame.Rect(self.rect[0] + self.rect[2] / 2 + 10, self.rect[1] + self.rect[3] / 3,
                                       self.rect[2] / 3 * 2, self.rect[3] / 3)
        self.hitbox = pygame.Rect(self.rect[0] + self.rect[2] / 3, self.rect[1] + self.rect[3] / 6 - 5,
                                  self.rect[2] / 3,
                                  self.rect[3] / 6 * 5)

    def update(self):
        if self.coconut_boost_time < cfg.in_game_time:
            self.stamina_recovery = 0.5
        self.progress = self.wood_amount * 100 / cfg.goal
        self.speed_x = 0
        self.speed_y = 0
        keystate = pygame.key.get_pressed()
        if self.stamina < 100 and not keystate[pygame.K_LSHIFT]:
            self.stamina += self.stamina_recovery
        elif self.stamina > 100:
            self.stamina = 100
        if self.hp > 0:
            if not (keystate[pygame.K_a] and keystate[pygame.K_d]):

                if keystate[pygame.K_a]:
                    cfg.vector = "left"

                    if (self.hitbox.collidelist(cfg.trees_rects_right)) == -1 and not self.hitbox.colliderect(
                            cfg.all_sprites.sprites()[1].line_right):
                        if keystate[pygame.K_LSHIFT] and self.stamina > 0:

                            if self.anim_counter_x == 6:
                                self.anim_counter_x = 0

                            self.image = img.woodcutter_run_left[self.anim_counter_x]
                            self.move_anim_delay += 1

                            if self.move_anim_delay == 5:
                                self.anim_counter_x += 1
                                self.move_anim_delay = 0
                            sx = 4
                            self.stamina -= 0.5

                        else:

                            if self.anim_counter_x == 6:
                                self.anim_counter_x = 0

                            self.image = img.woodcutter_walk_left[self.anim_counter_x]
                            self.move_anim_delay += 1

                            if self.move_anim_delay == 5:
                                self.anim_counter_x += 1
                                self.move_anim_delay = 0

                            sx = 2
                        if self.rect.x >= 500:
                            self.speed_x = -sx
                        elif self.bg_x < 2220:
                            self.bg_x += sx
                            func.update_monsters_x(cfg.monsterList, sx, flag_direction=True)
                if keystate[pygame.K_d]:
                    cfg.vector = "right"
                    if (self.hitbox.collidelist(cfg.trees_rects_left)) == -1 and not self.hitbox.colliderect(
                            cfg.all_sprites.sprites()[1].line_left):
                        if keystate[pygame.K_LSHIFT] and self.stamina > 0:

                            if self.anim_counter_x == 6:
                                self.anim_counter_x = 0

                            self.image = img.woodcutter_run_right[self.anim_counter_x]
                            self.move_anim_delay += 1

                            if self.move_anim_delay == 5:
                                self.anim_counter_x += 1
                                self.move_anim_delay = 0

                            sx = 4
                            self.stamina -= 0.5
                        else:

                            if self.anim_counter_x == 6:
                                self.anim_counter_x = 0

                            self.image = img.woodcutter_walk_right[self.anim_counter_x]
                            self.move_anim_delay += 1

                            if self.move_anim_delay == 5:
                                self.anim_counter_x += 1
                                self.move_anim_delay = 0

                            sx = 2
                        if self.rect.x <= 1320:
                            self.speed_x = sx
                        elif self.bg_x > -2460:
                            self.bg_x -= sx
                            func.update_monsters_x(cfg.monsterList, sx, flag_direction=False)
            if not (keystate[pygame.K_w] and keystate[pygame.K_s]):
                if keystate[pygame.K_w]:
                    if (self.hitbox.collidelist(cfg.trees_rects_bottom)) == -1 and not self.hitbox.colliderect(
                            cfg.all_sprites.sprites()[1].line_bottom):
                        if keystate[pygame.K_LSHIFT] and self.stamina > 0:

                            if self.anim_counter_y == 6:
                                self.anim_counter_y = 0

                            if cfg.vector == "right":
                                self.image = img.woodcutter_run_right[self.anim_counter_y]
                            else:
                                self.image = img.woodcutter_run_left[self.anim_counter_y]
                            self.move_anim_delay += 1

                            if self.move_anim_delay == 5:
                                self.anim_counter_y += 1
                                self.move_anim_delay = 0

                            sy = 4
                            self.stamina -= 0.5
                        else:

                            if self.anim_counter_y == 6:
                                self.anim_counter_y = 0

                            if cfg.vector == "right":
                                self.image = img.woodcutter_walk_right[self.anim_counter_y]
                            else:
                                self.image = img.woodcutter_walk_left[self.anim_counter_y]
                            self.move_anim_delay += 1

                            if self.move_anim_delay == 5:
                                self.anim_counter_y += 1
                                self.move_anim_delay = 0

                            sy = 2
                        if self.rect.y >= 300:
                            self.speed_y = -sy
                        elif self.bg_y < 1380:
                            self.bg_y += sy
                            func.update_monsters_y(cfg.monsterList, sy, flag_direction=True)
                if keystate[pygame.K_s]:
                    if (self.hitbox.collidelist(cfg.trees_rects_top)) == -1 and not self.hitbox.colliderect(
                            cfg.all_sprites.sprites()[1].line_top):
                        if keystate[pygame.K_LSHIFT] and self.stamina > 0:

                            if self.anim_counter_y == 6:
                                self.anim_counter_y = 0

                            if cfg.vector == "right":
                                self.image = img.woodcutter_run_right[self.anim_counter_y]
                            else:
                                self.image = img.woodcutter_run_left[self.anim_counter_y]
                            self.move_anim_delay += 1

                            if self.move_anim_delay == 5:
                                self.anim_counter_y += 1
                                self.move_anim_delay = 0

                            sy = 4
                            self.stamina -= 0.5
                        else:

                            if self.anim_counter_y == 6:
                                self.anim_counter_y = 0

                            if cfg.vector == "right":
                                self.image = img.woodcutter_walk_right[self.anim_counter_y]
                            else:
                                self.image = img.woodcutter_walk_left[self.anim_counter_y]
                            self.move_anim_delay += 1

                            if self.move_anim_delay == 5:
                                self.anim_counter_y += 1
                                self.move_anim_delay = 0

                            sy = 2
                        if self.rect.y <= 680:
                            self.speed_y = sy
                        elif self.bg_y > -1350:
                            self.bg_y -= sy
                            func.update_monsters_y(cfg.monsterList, sy, flag_direction=False)
            if keystate[pygame.K_c]:
                self.eat_apple()

            if keystate[pygame.K_z]:
                self.eat_coconut()

            if keystate[pygame.K_x]:
                self.eat_shishka()

            if keystate[pygame.K_e] and (
                    self.hitbox.colliderect(cfg.all_sprites.sprites()[1].line_left) or self.hitbox.colliderect(
                cfg.all_sprites.sprites()[1].line_right) or
                    self.hitbox.colliderect(cfg.all_sprites.sprites()[1].line_bottom) or self.hitbox.colliderect(
                cfg.all_sprites.sprites()[1].line_top)):
                cfg.workshop_active_flag = True
            elif not (self.hitbox.colliderect(cfg.all_sprites.sprites()[1].line_left) or self.hitbox.colliderect(
                    cfg.all_sprites.sprites()[1].line_right) or
                      self.hitbox.colliderect(cfg.all_sprites.sprites()[1].line_bottom) or self.hitbox.colliderect(
                        cfg.all_sprites.sprites()[1].line_top)):
                cfg.workshop_active_flag = False

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
                if self.anim_counter_death < 7 and self.death_delay < cfg.in_game_time:

                    if self.anim_counter_death <= 5:
                        self.image = img.woodcutter_death_right[self.anim_counter_death]
                        self.death_delay = cfg.in_game_time + 100
                    else:
                        self.death_delay = cfg.in_game_time + 1000
                    self.anim_counter_death += 1
                elif self.anim_counter_death == 7 and self.death_delay < cfg.in_game_time:
                    self.remove(cfg.all_sprites)
                    self.kill()
                    cfg.lose_flag = True
            elif cfg.vector == "left":
                if self.anim_counter_death < 7 and self.death_delay < cfg.in_game_time:

                    if self.anim_counter_death <= 5:
                        self.image = img.woodcutter_death_left[self.anim_counter_death]
                        self.death_delay = cfg.in_game_time + 100
                    else:
                        self.death_delay = cfg.in_game_time + 1000
                    self.anim_counter_death += 1
                elif self.anim_counter_death == 7 and self.death_delay < cfg.in_game_time:
                    self.remove(cfg.all_sprites)
                    self.kill()
                    cfg.lose_flag = True

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        self.hitbox[0] += self.speed_x
        self.hitbox[1] += self.speed_y

        # cfg.screen.fill("red", self.hitbox)

        # cfg.screen.fill("red", self.rect)
        # cfg.screen.fill("orange", self.rect_attack)
        # cfg.screen.fill("orange", self.hitbox)
        # for elem in cfg.trees1:
        #     cfg.screen.fill("blue", elem.line_right)
        #     cfg.screen.fill("blue", elem.line_left)
        #     cfg.screen.fill("blue", elem.line_top)
        #     cfg.screen.fill("blue", elem.line_bottom)
        # for elem in cfg.trees2:
        #     cfg.screen.fill("blue", elem.line_right)
        #     cfg.screen.fill("blue", elem.line_left)
        #     cfg.screen.fill("blue", elem.line_top)
        #     cfg.screen.fill("blue", elem.line_bottom)
        # for elem in cfg.trees3:
        #     cfg.screen.fill("blue", elem.line_right)
        #     cfg.screen.fill("blue", elem.line_left)
        #     cfg.screen.fill("blue", elem.line_top)
        #     cfg.screen.fill("blue", elem.line_bottom)

    def attack(self):
        if self.flag_attack:
            self.stamina -= 1
            if self.anim_counter_attack == 0:
                sounds.wave.stop()
                sounds.wave.play()

            if cfg.vector == "right":
                self.image = img.woodcutter_attack_right[self.anim_counter_attack]
                self.attack_anim_delay += 1

                if self.attack_anim_delay == 5:
                    self.anim_counter_attack += 1
                    self.attack_anim_delay = 0

                if self.anim_counter_attack == 6:
                    self.anim_counter_attack = 0
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

                self.image = img.woodcutter_attack_left[self.anim_counter_attack]
                self.attack_anim_delay += 1

                if self.attack_anim_delay == 5:
                    self.anim_counter_attack += 1
                    self.attack_anim_delay = 0

                if self.anim_counter_attack == 6:
                    self.anim_counter_attack = 0
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

    def eat_apple(self):
        if self.apple_eat_time < cfg.in_game_time:
            if self.utilities[0] > 0 and self.hp < 100:
                if self.hp + 10 <= 100:
                    self.hp += 10
                elif self.hp + 10 > 100:
                    self.hp = 100
                self.utilities[0] -= 1
                sounds.eat_apple.play()
                self.apple_eat_time = cfg.in_game_time + 1000

    def eat_shishka(self):
        if self.shishka_eat_time < cfg.in_game_time:
            if self.utilities[1] > 0 and self.armor < 100:
                if self.armor + 25 <= 100:
                    self.armor += 25
                elif self.armor + 25 > 100:
                    self.armor = 100
                self.utilities[1] -= 1
                sounds.falling_tree.play()
                self.shishka_eat_time = cfg.in_game_time + 1000
        elif self.armor > 100:
            self.armor = 100

    def eat_coconut(self):

        if self.coconut_eat_time < cfg.in_game_time:
            if self.utilities[2] > 0:
                self.utilities[2] -= 1
                self.stamina_recovery = 1.5
                sounds.drink_coconut.play()
                self.coconut_eat_time = cfg.in_game_time + 5100
                self.coconut_boost_time = self.coconut_eat_time


class Weapon:
    def __init__(self, dmg, attack_speed):
        self.name = "Axe"
        self.damage = dmg
        self.attack_speed = attack_speed

    def dmg_up(self):
        self.damage += 5


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

        self.player_vector = pm.Vector2(cfg.list_all_sprites[0].rect.x, cfg.list_all_sprites[0].rect.y)
        self.tree_vector = pm.Vector2(self.rect.centerx, self.rect.y + 70)
        distance = self.tree_vector.distance_to(self.player_vector)

        self.rect.x = cfg.list_all_sprites[0].bg_x + self.posx
        self.rect.y = cfg.list_all_sprites[0].bg_y + self.posy
        self.line_left[0] = cfg.list_all_sprites[0].bg_x + self.line_left_x
        self.line_left[1] = cfg.list_all_sprites[0].bg_y + self.line_left_y
        self.line_right[0] = cfg.list_all_sprites[0].bg_x + self.line_right_x
        self.line_right[1] = cfg.list_all_sprites[0].bg_y + self.line_right_y
        self.line_top[0] = cfg.list_all_sprites[0].bg_x + self.line_top_x
        self.line_top[1] = cfg.list_all_sprites[0].bg_y + self.line_top_y
        self.line_bottom[0] = cfg.list_all_sprites[0].bg_x + self.line_bottom_x
        self.line_bottom[1] = cfg.list_all_sprites[0].bg_y + self.line_bottom_y

        if distance <= 110:
            self.draw_info_bar(cfg.screen, self.rect.x + 25, self.rect.y - 10, self.hp, (92, 69, 10), (140, 104, 13),
                               "black", self.start_hp, 50, 10)

    def take_dmg(self, dmg):

        if self.hp > 0:
            self.status = True
            self.hp -= dmg
            sounds.hit_tree.play()
        if self.hp <= 0:
            if self.status:
                sounds.falling_tree.play()

            self.remove(cfg.all_sprites)
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
            cfg.list_all_sprites[0].wood_amount += self.bonus
            if self.bonus == 10:
                cfg.list_all_sprites[0].fir_amount += 1
            elif self.bonus == 5:
                cfg.list_all_sprites[0].oak_amount += 1
            elif self.bonus == 25:
                cfg.list_all_sprites[0].palm_amount += 1
            self.bonus = 0

    def give_drop(self):

        if self.status:

            chance = random.randint(1, 100)

            if 0 <= chance <= cfg.temp_random_list[self.random_index]:
                cfg.list_all_sprites[0].utilities[self.drop] += 1
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
        self.rect.x = self.posx + cfg.list_all_sprites[0].bg_x
        self.rect.y = self.posy + cfg.list_all_sprites[0].bg_y
        cfg.screen.fill("red", self.line_left)
        cfg.screen.fill("red", self.line_right)
        cfg.screen.fill("red", self.line_top)
        cfg.screen.fill("red", self.line_bottom)
        # self.line_left.x = self.line_left_x + cfg.bg_x
        # self.line_left.y = self.line_left_y + cfg.bg_y
        # self.line_right.x = self.line_right_x + cfg.bg_x
        # self.line_right.y = self.line_right_y + cfg.bg_y
        self.line_right.x = self.posx + self.rect[2] - 30 + cfg.list_all_sprites[0].bg_x
        self.line_right.y = self.posy + 60 + cfg.list_all_sprites[0].bg_y
        self.line_left.x = self.posx - 10 + cfg.list_all_sprites[0].bg_x
        self.line_left.y = self.posy + 60 + cfg.list_all_sprites[0].bg_y
        self.line_top.x = self.posx - 10 + cfg.list_all_sprites[0].bg_x
        self.line_top.y = self.posy + 60 + cfg.list_all_sprites[0].bg_y
        self.line_bottom.x = self.posx - 10 + cfg.list_all_sprites[0].bg_x
        self.line_bottom.y = self.posy + self.rect[3] + cfg.list_all_sprites[0].bg_y
        # # self.line_right.y = cfg.bg_y + self.posy
        # # self.line_left.x = cfg.bg_x + self.posx
        # # self.line_left.y = cfg.bg_y +self.posy


def initit_units():
    # Экземпляр класса Player() -----------------------------------------------------------------------
    player = Player("Albert", 100, cfg.WIDTH, cfg.HEIGHT)
    cfg.all_sprites.add(player)
    # --------------------------------------------------------------------------------------------------
    house = House(960, 200)
    cfg.all_sprites.add(house)
    # print(cfg.all_sprites.sprites())


def del_units():
    for obj in cfg.all_sprites:
        del obj
    cfg.all_sprites.empty()
    cfg.tree_list_x.clear()
    cfg.tree_list_y.clear()
    cfg.monster_list_x.clear()
    cfg.monster_list_y.clear()
    cfg.trees_rects_bottom.clear()
    cfg.trees_rects_top.clear()
    cfg.trees_rects_left.clear()
    cfg.trees_rects_right.clear()
