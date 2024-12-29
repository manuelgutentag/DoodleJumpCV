import pygame, sys

class Doodle():
    def __init__(self):
        self.doodle_left = pygame.image.load('Graphics/doodle_left.png').convert_alpha()
        self.doodle_right = pygame.image.load('Graphics/doodle_right.png').convert_alpha()

    def draw_doodle(self):
        doodle_rect = pygame.Rect(w*48/100, h*6/10, 250, 243)
        screen.blit(self.doodle_left, doodle_rect)

class Entity():
    def __init__(self):
        self.background = pygame.image.load('Graphics/background.png').convert_alpha()

    def draw_background_elements(self):
        border_rect_l = pygame.Rect(0, 0, w/3, h)
        border_rect_r = pygame.Rect(w*2/3, 0, w/3, h)
        background_rect = pygame.Rect(w/3, 0, w/3, h)
        pygame.draw.rect(screen, (0,0,0), border_rect_l)
        pygame.draw.rect(screen, (0,0,0), border_rect_r)
        screen.blit(self.background, background_rect)

class Main():
    def __init__(self):
        self.background = Entity()
        self.doodle = Doodle()


    def draw_elements(self):
        self.background.draw_background_elements()
        self.doodle.draw_doodle()


pygame.init()
screen = pygame.display.set_mode()
w, h = screen.get_size()
print(w, h)
clock = pygame.time.Clock()

maingame = Main()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #draws all our elements
    pygame.display.update()
    screen.fill((250, 250, 250))
    maingame.draw_elements()
    clock.tick(60)
