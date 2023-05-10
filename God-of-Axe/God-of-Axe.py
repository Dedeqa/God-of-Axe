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

my_font = pygame.font.Font('fonts/Jfwildwood-ldYZ.ttf', 90)

# ------------- Меню -------------
play = pygame.image.load('images/play.jpg').convert_alpha()
active_play = pygame.image.load('images/play_active.jpg').convert_alpha()
options = pygame.image.load('images/options.jpg').convert_alpha()
active_options = pygame.image.load('images/options_active.jpg').convert_alpha()
quite = pygame.image.load('images/quite.jpg').convert_alpha()
active_quite = pygame.image.load('images/quite_active.jpg').convert_alpha()

menu_bg = pygame.image.load('images/bg_6.jpg').convert_alpha()
menu_title = my_font.render("God of Axe", True, (224, 153, 9))
# --------------------------------

pygame.display.set_icon(icon)


class Button:
    flag = False
    """класс кнопок меню"""

    def __init__(self, screen, y, btn_type):
        """инициализация кнопки"""
        self.screen = screen
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if (current_size[0] // 2 - 111 <= mouse[0] <= current_size[0] // 2 + 111) and (y <= mouse[1] <= y + 96) and (
                click[0] == True):
            file = f"images/{btn_type}_active.jpg"
            self.flag = True
            y += 12
        else:
            file = f"images/{btn_type}.jpg"

        self.image = pygame.image.load(file)

        self.screen_rect = screen.get_rect()
        self.rect = self.image.get_rect()
        self.rect.centerx = FULLSCREEN_SIZE[0] // 2
        self.rect.top = y

    def draw(self):
        if self.flag:
            screen.blit(self.image, self.rect)
            self.music = pygame.mixer.Sound('Music/tick.mp3')
        else:
            screen.blit(self.image, self.rect)


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
        screen.blit(menu_bg, (0, 0))
        screen.blit(menu_title, (440, 20))
        Play = Button(screen, 200, "play")

        Play.draw()
        Options = Button(screen, 320, "options")
        Options.draw()
        Quite = Button(screen, 440, "quite")
        Quite.draw()

    pygame.display.flip()
