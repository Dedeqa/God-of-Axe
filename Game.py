import pygame

pygame.init()

WIDTH = 700
HEIGHT = 500
FPS = 10

info = pygame.display.Info()

FULLSCREEN_SIZE = (info.current_w, info.current_h)
is_fullscreen = False

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
current_size = screen.get_size()
last_size = current_size

pygame.display.set_caption("God of Axe")
clock = pygame.time.Clock()
icon = pygame.image.load('images/icon_axe.png').convert_alpha()
bg = pygame.image.load('images/bg-5.jpg').convert_alpha()
my_font = pygame.font.Font('fonts/Jfwildwood-ldYZ.ttf', 90)

pygame.display.set_icon(icon)

menu_title = my_font.render("God of Axe", True, (71, 153, 34))

class Button:
    def __init__(self, width, height, inactive_color, active_color):
        self.width = width
        self.height = height
        self.inactive_color = (0, 0, 0)
        self.active_color = (103, 30, 130)
    def draw(self, x, y, message, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if (x < mouse[0] < x + self.width) and (y < mouse[1] < y + self.width):
            pygame.draw.rect(screen, self.active_color, (x, y, self.width, self.height))
        else:
            pygame.draw.rect(screen, self.inactive_color, (x, y, self.width, self.height))



running = True
is_menu = True

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            quit()
        elif event.type == pygame.VIDEORESIZE:
            current_size = event.size
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F10:
                is_fullscreen = not is_fullscreen
                if is_fullscreen:
                    last_size = current_size
                    current_size = FULLSCREEN_SIZE
                    screen = pygame.display.set_mode(current_size, pygame.FULLSCREEN)
                else:
                    current_size = last_size
                    screen = pygame.display.set_mode(current_size, pygame.RESIZABLE)

    if is_menu:
        screen.blit(bg, (0, 0))
        screen.blit(menu_title, (440, 20))

    pygame.display.flip()
