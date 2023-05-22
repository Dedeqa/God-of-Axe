import pygame
import pygame.math as m
import config as cfg
import classes as cl


class Monster(cl.Unit, pygame.sprite.Sprite):
    def __init__(self, nm, hp, posx, posy, viewing_range):
        cl.Unit.__init__(self, nm, hp, posx, posy)
        pygame.sprite.Sprite.__init__(self)
        self.image = cfg.minotaur_walk_bottom[0]
        self.rect = self.image.get_rect()
        self.rect.center = (posx, posy)
        self.minimum_distance = 50
        self.maximum_distance = 10000
        self.LERP_FACTOR = 0.05
        self.target_vector = (0, 0)
        self.follower_vector = (0, 0)
        self.i = 0
        self.j = 0
        self.anim_time = 0
        self.side = "right"
        self.wait_side = True
        self.wait_time = 0
        self.anim_wait_time = 0
        self.viewing_range = viewing_range
        self.start_hp = hp

    def update(self):
        self.target_vector = m.Vector2(cl.player.rect.x, cl.player.rect.y)
        self.follower_vector = m.Vector2(self.rect.x, self.rect.y)
        distance = self.follower_vector.distance_to(self.target_vector)
        direction_vector = self.target_vector - self.follower_vector
        min_step = max(0, int(distance - self.maximum_distance))
        max_step = distance - self.minimum_distance
        VELOCITY = 3
        step_distance = min(max_step, max(min_step, VELOCITY))
        direction_vector /= distance

        if distance <= self.viewing_range:
            self.follower_vector = self.follower_vector + direction_vector * step_distance

            if self.follower_vector.x > cl.player.rect.x and self.follower_vector.y > cl.player.rect.y:
                if self.follower_vector.x - cl.player.rect.x > self.follower_vector.y - cl.player.rect.y:
                    self.side = "left"
                else:
                    self.side = "top"
            elif self.follower_vector.x > cl.player.rect.x and self.follower_vector.y < cl.player.rect.y:
                if self.follower_vector.x - cl.player.rect.x > cl.player.rect.y - self.follower_vector.y:
                    self.side = "left"
                else:
                    self.side = "bottom"
            elif self.follower_vector.x < cl.player.rect.x and self.follower_vector.y > cl.player.rect.y:
                if cl.player.rect.x - self.follower_vector.x > self.follower_vector.y - cl.player.rect.y:
                    self.side = "right"
                else:
                    self.side = "top"
            elif self.follower_vector.x < cl.player.rect.x and self.follower_vector.y < cl.player.rect.y:
                if cl.player.rect.x - self.follower_vector.x > cl.player.rect.y - self.follower_vector.y:
                    self.side = "right"
                else:
                    self.side = "bottom"
            if self.i == 3:
                self.i = 0
            if self.side == "right":
                self.image = cfg.minotaur_walk_right[self.i]
            elif self.side == "left":
                self.image = cfg.minotaur_walk_left[self.i]
            elif self.side == "top":
                self.image = cfg.minotaur_walk_top[self.i]
            elif self.side == "bottom":
                self.image = cfg.minotaur_walk_bottom[self.i]
            self.anim_time += 1
            if self.anim_time == 10:
                self.i += 1
                self.anim_time = 0

            self.draw_shield_bar(cfg.screen, self.rect.x, self.rect.y - 10, self.hp, (107, 34, 34), "red", "black",
                                 self.start_hp)
            self.rect.x = round(self.follower_vector.x)
            self.rect.y = round(self.follower_vector.y)

        else:
            if self.j == 3:
                self.j = 0

            if self.wait_side:
                self.image = cfg.minotaur_walk_right[self.j]
                self.rect.x += 1
            else:
                self.image = cfg.minotaur_walk_left[self.j]
                self.rect.x -= 1

            self.anim_wait_time += 1
            self.wait_time += 1

            if self.anim_wait_time == 10:
                self.j += 1
                self.anim_wait_time = 0
            if self.wait_time == 100:
                self.wait_time = 0
                self.wait_side = not self.wait_side

    def take_dmg(self, dmg):

        if self.hp > 0:
            self.hp -= dmg
            cfg.hit_tree.play()
        if self.hp <= 0:
            self.remove(cl.all_sprites)
            self.kill()


min1 = Monster("Jaba", 1000, 1, 1, 500)
cfg.monsterList.append(min1)
cl.all_sprites.add(min1)
