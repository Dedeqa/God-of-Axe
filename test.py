import pygame


pygame.init()

HEIGHT = 960
WIDTH = 1280
FPS = 2


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40, 40))
        self.image.fill('green')
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.speedx = 0
        self.speedy = 0

    def update(self):
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a]:
            self.speedx = -1
        if keystate[pygame.K_d]:
            self.speedx = 1
        if keystate[pygame.K_w]:
            self.speedy = -1
        if keystate[pygame.K_s]:
            self.speedy = 1

        self.rect.x += self.speedx
        self.rect.y += self.speedy



all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# Окно
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("God of Axe")
icon = pygame.image.load('images\icon_axe.png')
pygame.display.set_icon(icon)
myfont = pygame.font.Font('fonts/Pacifico-Regular.ttf', 70)
text_surface = myfont.render('God of Axe', False, 'Red')
woodcutter_fg = pygame.image.load('images/New Piskel.png')

bg = pygame.image.load('images/menu_bg.jpg')
screen.blit(text_surface, (440, 400))
screen.blit(woodcutter_fg, (300, 390))

clock = pygame.time.Clock()

flag_switch = True
running = True

while running:
    pygame.display.update()

    # clock.tick(FPS)
    while flag_switch:
        pygame.time.wait(2000)
        screen.blit(bg, (0, 0))
        flag_switch = False
    screen.blit(bg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.flip()
