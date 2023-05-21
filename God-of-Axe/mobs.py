import pygame
import pygame.math as m
import config as cfg
import classes as cl


class Monster(cl.Unit, pygame.sprite.Sprite):
    def __init__(self, nm, hp, posx, posy):
        cl.Unit.__init__(self, nm, hp, posx, posy)
        pygame.sprite.Sprite.__init__(self)
        self.image = cfg.minotaur_walk_bottom[0]
        self.rect = self.image.get_rect()
        self.rect.center = (posx, posy)
        self.speed = 1
        self.speedx = 0
        self.speedy = 0
        self.kx = 0
        self.ky = 0
        self.minimum_distance = 50
        self.maximum_distance = 10000
        self.LERP_FACTOR = 0.05
    def update(self):
        target_vector = m.Vector2(cl.player.rect.x, cl.player.rect.y)
        follower_vector = m.Vector2(self.rect.x, self.rect.y)

        distance = follower_vector.distance_to(target_vector)
        direction_vector = target_vector - follower_vector
            # if distance > 0:
        min_step = max(0, distance - self.maximum_distance)
        max_step = distance - self.minimum_distance
        VELOCITY = 3
        step_distance = min(max_step, max(min_step, VELOCITY))
            # step_distance = min_step + (max_step - min_step) * self.LERP_FACTOR
        direction_vector /= distance
        follower_vector = follower_vector + direction_vector * step_distance
        self.rect.x = round(follower_vector.x)
        self.rect.y = round(follower_vector.y)
min1 = Monster("Jaba", 100, 1, 1)
cfg.monsterList.append(min1)
cl.all_sprites.add(min1)