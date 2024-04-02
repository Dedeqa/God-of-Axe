import pygame
import pygame.math as m
import config as cfg
import classes as cl
import sounds
import images as img
import random


class Monster(cl.Unit, pygame.sprite.Sprite):

    def __init__(self, nm, hp, posx, posy, viewing_range, dmg):

        cl.Unit.__init__(self, nm, hp, posx, posy)
        pygame.sprite.Sprite.__init__(self)
        self.image = img.minotaur_walk_bottom[0]
        self.rect = self.image.get_rect()
        self.rect.center = (posx, posy)
        self.minimum_distance = 50
        self.maximum_distance = 10000
        self.LERP_FACTOR = 0.05
        self.target_vector = (0, 0)
        self.follower_vector = (0, 0)
        self.damage = dmg
        self.i = 0
        self.j = 0
        self.anim_time = 0
        self.side = "right"
        self.wait_side = True
        self.wait_timer = 0
        self.anim_wait_time = 0
        self.viewing_range = viewing_range
        self.start_hp = hp
        self.sound_flag = True
        self.attack_flag = False
        self.distance = 0

        self.attack_timer = 0
        self.attack_wait_timer = 0

    def update(self):

        self.target_vector = m.Vector2(cfg.list_all_sprites[0].rect.x, cfg.list_all_sprites[0].rect.y)
        self.follower_vector = m.Vector2(self.rect.x, self.rect.y)

        self.distance = self.follower_vector.distance_to(self.target_vector)
        direction_vector = self.target_vector - self.follower_vector
        min_step = max(0, int(self.distance - self.maximum_distance))
        max_step = self.distance - self.minimum_distance
        VELOCITY = 2

        if self.distance != 0:
            direction_vector /= self.distance

        if not self.attack_flag:
            step_distance = min(max_step, max(min_step, VELOCITY))
        else:
            step_distance = 0

        if self.distance <= self.viewing_range and cfg.list_all_sprites[0].hp > 0:

            if self.sound_flag:
                self.sound_flag = False
                sounds.agr_monster.play()

            self.follower_vector += direction_vector * step_distance

            if self.follower_vector.x > cfg.list_all_sprites[0].rect.x and self.follower_vector.y > \
                    cfg.list_all_sprites[0].rect.y:
                if self.follower_vector.x - cfg.list_all_sprites[0].rect.x > self.follower_vector.y - \
                        cfg.list_all_sprites[0].rect.y:
                    self.side = "left"
                else:
                    self.side = "top"
            elif self.follower_vector.x > cfg.list_all_sprites[0].rect.x and self.follower_vector.y < \
                    cfg.list_all_sprites[0].rect.y:
                if self.follower_vector.x - cfg.list_all_sprites[0].rect.x > cfg.list_all_sprites[
                    0].rect.y - self.follower_vector.y:
                    self.side = "left"
                else:
                    self.side = "bottom"
            elif self.follower_vector.x < cfg.list_all_sprites[0].rect.x and self.follower_vector.y > \
                    cfg.list_all_sprites[0].rect.y:
                if cfg.list_all_sprites[0].rect.x - self.follower_vector.x > self.follower_vector.y - \
                        cfg.list_all_sprites[0].rect.y:
                    self.side = "right"
                else:
                    self.side = "top"
            elif self.follower_vector.x < cfg.list_all_sprites[0].rect.x and self.follower_vector.y < \
                    cfg.list_all_sprites[0].rect.y:
                if cfg.list_all_sprites[0].rect.x - self.follower_vector.x > cfg.list_all_sprites[
                    0].rect.y - self.follower_vector.y:
                    self.side = "right"
                else:
                    self.side = "bottom"

            if self.i == 3:
                self.i = 0
            if self.side == "right":
                self.image = img.minotaur_walk_right[self.i]
            elif self.side == "left":
                self.image = img.minotaur_walk_left[self.i]
            elif self.side == "top":
                self.image = img.minotaur_walk_top[self.i]
            elif self.side == "bottom":
                self.image = img.minotaur_walk_bottom[self.i]
            self.anim_time += 1
            if self.anim_time == 10:
                self.i += 1
                self.anim_time = 0

            self.draw_info_bar(cfg.screen, self.rect.x, self.rect.y - 10, self.hp, (107, 34, 34), "red", "black",
                               self.start_hp, 50, 10)
            self.rect.x = round(self.follower_vector.x)
            self.rect.y = round(self.follower_vector.y)

            if self.attack_wait_timer == 100:
                self.attack_wait_timer = 0
                self.attack_flag = False
            else:
                self.attack_wait_timer += 1

            if self.distance <= self.minimum_distance + 1:

                if not self.attack_flag:
                    if self.side == "right":
                        if (cfg.list_all_sprites[0].hitbox.collidelist(cfg.trees_rects_left)) == -1 and (
                                not cfg.list_all_sprites[0].hitbox.colliderect(
                                    cl.cfg.all_sprites.sprites()[1].line_left) and not cfg.list_all_sprites[
                            0].hitbox.collidelist(
                            cfg.trees_rects_right) and not cfg.list_all_sprites[0].hitbox.collidelist(
                            cfg.trees_rects_top) and not cfg.list_all_sprites[0].hitbox.collidelist(
                            cfg.trees_rects_bottom)):

                            if cfg.bg_x > -1920:
                                cfg.bg_x -= 1
                    elif self.side == "left":
                        if (cfg.list_all_sprites[0].hitbox.collidelist(cfg.trees_rects_right)) == -1 and (
                                not cfg.list_all_sprites[0].hitbox.colliderect(
                                    cl.cfg.all_sprites.sprites()[1].line_left) and not cfg.list_all_sprites[
                            0].hitbox.collidelist(
                            cfg.trees_rects_right) and not cfg.list_all_sprites[0].hitbox.collidelist(
                            cfg.trees_rects_top) and not cfg.list_all_sprites[0].hitbox.collidelist(
                            cfg.trees_rects_bottom)):
                            if cfg.bg_x < 1920:
                                cfg.bg_x += 1
                    elif self.side == "top":
                        if (cfg.list_all_sprites[0].hitbox.collidelist(cfg.trees_rects_bottom)) == -1 and (
                                not cfg.list_all_sprites[0].hitbox.colliderect(
                                    cl.cfg.all_sprites.sprites()[1].line_left) and not cfg.list_all_sprites[
                            0].hitbox.collidelist(
                            cfg.trees_rects_right) and not cfg.list_all_sprites[0].hitbox.collidelist(
                            cfg.trees_rects_top) and not cfg.list_all_sprites[0].hitbox.collidelist(
                            cfg.trees_rects_bottom)):
                            if cfg.bg_y < 1080:
                                cfg.bg_y += 1
                    elif self.side == "bottom":
                        if (cfg.list_all_sprites[0].hitbox.collidelist(cfg.trees_rects_top)) == -1 and (
                                not cfg.list_all_sprites[0].hitbox.colliderect(
                                    cl.cfg.all_sprites.sprites()[1].line_left) and not cfg.list_all_sprites[
                            0].hitbox.collidelist(
                            cfg.trees_rects_right) and not cfg.list_all_sprites[0].hitbox.collidelist(
                            cfg.trees_rects_top) and not cfg.list_all_sprites[0].hitbox.collidelist(
                            cfg.trees_rects_bottom)):
                            if cfg.bg_y > -1080:
                                cfg.bg_y -= 1

                self.attack()

            else:
                self.attack_timer = 100
                cfg.list_all_sprites[0].flag_take_dmg = False

        else:

            self.attack_wait_timer = 0
            self.sound_flag = True

            if self.j == 3:
                self.j = 0

            if self.wait_side:
                self.image = img.minotaur_walk_right[self.j]
                self.rect.x += 1
            else:
                self.image = img.minotaur_walk_left[self.j]
                self.rect.x -= 1

            self.anim_wait_time += 1
            self.wait_timer += 1

            if self.anim_wait_time == 10:
                self.j += 1
                self.anim_wait_time = 0
            if self.wait_timer == 100:
                self.wait_timer = 0
                self.wait_side = not self.wait_side

    def take_dmg(self, dmg):

        if self.hp > 0:
            self.hp -= dmg
            sounds.hit_monster.play()
            # sounds.hit_monster.stop()
        if self.hp <= 0:
            cfg.list_all_sprites[0].kills += 1
            cfg.list_all_sprites[0].coins += random.randint(3, 10)
            sounds.take_coin.play()
            cfg.all_sprites.remove(self)
            cfg.monsterList.remove(self)

    def attack(self):

        if self.attack_timer == 100:
            self.attack_flag = True
            cfg.list_all_sprites[0].take_dmg(self.damage)
            self.attack_timer = 0
        if self.side == "left":
            if self.attack_timer == 5:
                cfg.list_all_sprites[0].image = img.woodcutter_hurt_right[0]
            if self.attack_timer == 10:
                cfg.list_all_sprites[0].image = img.woodcutter_hurt_right[1]
            if self.attack_timer == 15:
                cfg.list_all_sprites[0].image = img.woodcutter_hurt_right[2]
        elif self.side == "right":
            if self.attack_timer == 5:
                cfg.list_all_sprites[0].image = img.woodcutter_hurt_left[0]
            if self.attack_timer == 10:
                cfg.list_all_sprites[0].image = img.woodcutter_hurt_left[1]
            if self.attack_timer == 15:
                cfg.list_all_sprites[0].image = img.woodcutter_hurt_left[2]
        self.attack_timer += 1
