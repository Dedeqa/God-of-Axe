import pygame

pygame.init()
screen = pygame.display.set_mode((600, 300))  # , flags=pygame.NOFRAME)
pygame.display.set_caption("Hero of Axe")
icon = pygame.image.load('images\icon_axe.png')
pygame.display.set_icon(icon)

running = True
square = pygame.Surface((50, 170))
square.fill('Blue')

myfont = pygame.font.Font('fonts/Pacifico-Regular.ttf', 40)
text_surface = myfont.render('Hero of Axe', False, 'Red')

player = pygame.image.load('images/New Piskel.png')

while running:

    screen.blit(text_surface, (200, 100))
    screen.blit(player, (50, 50))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
