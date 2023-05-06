import pygame
import random

tl, tr, bl, br = 0, 0, 0, 0
color_list = [int(i) for i in range(0, 256)]
WIDTH = 300
HEIGHT = 700
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)

    flag_hor = True
    flag_ver = True

    def update(self):
        global tl, tr, bl, br
        if Player.flag_hor:
            self.rect.x += 50
        else:
            self.rect.x -= 50

        if Player.flag_ver:
            self.rect.y -= 50
        else:
            self.rect.y += 50

        # if self.rect.right < 0:
        #     self.rect.left = WIDTH
        # if self.rect.left > WIDTH:
        #     self.rect.right = 0
        #
        # if self.rect.top < -50:
        #     self.rect.bottom = HEIGHT + 50
        # if self.rect.bottom > HEIGHT + 50:
        #     self.rect.top = -50

        if self.rect.left >= WIDTH - 50:
            self.rect.left = WIDTH - 50
            Player.flag_hor = False
        if self.rect.right <= 50:
            self.rect.right = 50
            Player.flag_hor = True
        if self.rect.top <= 0:
            self.rect.top = 0
            Player.flag_ver = False
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT
            Player.flag_ver = True
        if (self.rect.bottomleft == (0, WIDTH)) or (self.rect.bottomright == (WIDTH, HEIGHT)) \
                or (self.rect.topright == (WIDTH, 0)) or (self.rect.topleft == (0, 0)):
            # if self.rect.bottomleft == (0, WIDTH):
            #     bl += 1
            # if self.rect.bottomright == (WIDTH, HEIGHT):
            #     br += 1
            # if self.rect.topright == (WIDTH, 0):
            #     tr += 1
            # if self.rect.topleft == (0, 0):
            #     tl += 1
            color = (random.sample(color_list, 3))
            self.image.fill(color)


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(RED)
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(tl, tr, bl, br, end=' ')
            running = False
    all_sprites.update()
    screen.fill(WHITE)

    all_sprites.draw(screen)
    pygame.display.flip()
