import pygame, sys

class Doodle():
    def __init__(self):
        self.x_doodle = w*48/100
        #self.y_doodle= h*3/5
        self.y_doodle = 0

        self.x_doodle_prev = 0
        self.y_doodle_prev = 0

        self.y_doodle_speed = 0

        self.falling = False
        self.ascending = False

        self.gravity_const = 0.7
        self.gravity_speed = 0

        self.doodle_left = pygame.image.load('Graphics/doodle_left.png').convert_alpha()
        self.doodle_right = pygame.image.load('Graphics/doodle_right.png').convert_alpha()

    def check_jump(self):
        #checks when doodle should jump the first platform
        if self.y_doodle + 243 <= Entity.first_platform_y + 45 and self.y_doodle + 243 >= Entity.first_platform_y and (
            self.x_doodle + 200 >= Entity.first_platform_x  and self.x_doodle + 50 <= Entity.first_platform_x + 225) and self.falling:
            return True

    def vertical_movement(self):
        self.y_doodle_prev = self.y_doodle
        self.gravity_speed += self.gravity_const
        self.y_doodle += self.y_doodle_speed + self.gravity_speed
        if self.y_doodle_prev <= self.y_doodle:
            self.falling = True
        if self.check_jump():
            self.y_doodle_speed = -35
            self.gravity_speed = 0


    def move_left(self):
        self.x_doodle -= 2

    def move_right(self):
        self.x_doodle += 2

    def draw_doodle(self):
        doodle_rect = pygame.Rect(self.x_doodle, self.y_doodle, 250, 243)
        screen.blit(self.doodle_left, doodle_rect)

class Entity():
    screen = pygame.display.set_mode()
    w, h = screen.get_size()

    first_platform_x = w * 48 / 100
    first_platform_y = h * 4 / 5

    def __init__(self):
        self.background = pygame.image.load('Graphics/background.png').convert_alpha()
        self.yellow_platform = pygame.image.load('Graphics/yellow_platform.png').convert_alpha()

    def draw_foreground_elements(self):
        #TODO: Change Entity.first_platform to platform[i] etc.
        yellow_platform_rect = pygame.Rect(Entity.first_platform_x, Entity.first_platform_y, 225, 65)
        screen.blit(self.yellow_platform, yellow_platform_rect)

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
        self.platform = Entity()
        self.doodle = Doodle()

    def update(self):
        self.doodle.vertical_movement()
        self.doodle.check_jump()

    def draw_elements(self):
        self.background.draw_background_elements()
        self.doodle.draw_doodle()
        self.platform.draw_foreground_elements()


pygame.init()
screen = pygame.display.set_mode()
w, h = screen.get_size()
print(w, h)
clock = pygame.time.Clock()
pygame.key.set_repeat(1, 1) # for keeping button pressed

maingame = Main()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                maingame.doodle.move_left()
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                maingame.doodle.move_right()

    #draws all our elements
    pygame.display.update()
    screen.fill((250, 250, 250))
    maingame.update()
    maingame.draw_elements()
    clock.tick(60)
