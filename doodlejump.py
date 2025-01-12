import pygame, sys, random
from pygame.math import Vector2

class Doodle:
    def __init__(self):
        self.x_doodle = w * 48/100
        self.y_doodle= h * 2/5

        self.x_doodle_prev = 0
        self.y_doodle_prev = 0

        self.y_doodle_speed = 0

        self.falling = False
        self.ascending = False
        self.jump = False
        self.heightincrease = False
        self.scrolling = False

        self.gravity_const = 0.7
        self.gravity_speed = 0

        self.x_cam = 0
        self.y_cam = 0

        self.camera_rect = pygame.Rect(self.x_cam, self.y_cam, w, h)

        self.list = [Vector2(w * 0.48, h * 4/5)] #create list for platforms including the starting platform
        self.list_copy = [0,0,0,0,0,0] #copy of y values from the list-array
        self.scrolldistance = 0
        self.goal = 0
        self.goalscrolloff = [Vector2(0,0), Vector2(0,0), Vector2(0,0), Vector2(0,0)]
        self.platform_rect = []

        self.base_height = h * 4/5
        self.new_height = 0

        self.doodle_left = pygame.image.load('Graphics/doodle_left.png').convert_alpha()
        #self.doodle_right = pygame.image.load('Graphics/doodle_right.png').convert_alpha()
        self.yellow_platform = pygame.image.load('Graphics/yellow_platform.png').convert_alpha()

        for i in range(5):
            #create initial set of platforms
            self.list.append(Vector2(w * random.uniform(0.33, 0.6), h * (1 - (i+2)/5)))
        for i in range(6):
            #create platform rects
            self.platform_rect.append(pygame.Rect(self.list[i].x, self.list[i].y, 225, 65))


    def check_jump(self):
        self.jump = False
        #checks when doodle should jump the other platforms
        for i in range(6):
            if (self.y_doodle + 243 <= self.list[i].y + 70 and self.y_doodle + 243 >= self.list[i].y and
                (self.x_doodle + 200 >= self.list[i].x and self.x_doodle + 50 <= self.list[i].x + 225) and self.falling):
                self.jump = True

                #successful height increase
                if self.list[i].y < h * 4/5:
                    self.heightincrease = True
                    self.new_height = self.list[i].y
                    self.scrolldistance = self.base_height - self.new_height  # set scroll distance
                # list copy
                for i in range(6):
                    self.list_copy[i] = self.list[i].y
                break

        return self.jump

    def scroll(self):

        if self.heightincrease:

            self.camera_update()



            if not self.ascending:
                self.heightincrease = False












            #self.list_y_speed = 50
            #self.cam_gravity_speed = 0

            #scroll functionality
            #self.cam_gravity_speed += self.gravity_const
            for j in range(6):
                '''
                if self.list[j].y < self.list_copy[j] + self.scrolldistance:
                    self.list[j].y += self.list_y_speed - self.cam_gravity_speed
                elif self.list[j].y > self.list_copy[j] + self.scrolldistance:
                    self.cam_gravity_speed = 0
                    self.list_y_speed = 0
                    self.heightincrease = False
                '''

                #print platforms
                self.platform_rect[j] = pygame.Rect(self.list[j].x, self.list[j].y, 225, 65)
                self.draw_platform()

                if self.list[j].y > h:
                    # moves platforms back up, if they are out of frame after jumping
                    self.list[j].y -= h + h/5
                    self.list[j].x = w * random.uniform(0.4, 0.6)

    def camera_update(self):
        self.x_cam = int(w / 2)
        self.y_cam = self.y_doodle

        self.camera_rect = pygame.Rect(self.x_cam, self.y_cam, w, h)

    def vertical_movement(self):
        self.y_doodle_prev = self.y_doodle
        self.gravity_speed += self.gravity_const
        self.y_doodle += self.y_doodle_speed + self.gravity_speed
        if self.check_jump():
            print("jumped")
            self.y_doodle_speed = -35
            self.gravity_speed = 0

        #check if ascending or falling
        if self.y_doodle_prev <= self.y_doodle:
            self.falling = True
            self.ascending = False
        else:
            self.ascending = True
            self.falling = False
        print(self.ascending)


    def move_left(self):
        self.x_doodle -= 2

    def move_right(self):
        self.x_doodle += 2

    def draw_doodle(self):
        doodle_rect = pygame.Rect(self.x_doodle, self.y_doodle, 250, 243)
        screen.blit(self.doodle_left, doodle_rect)

    def draw_platform(self):
        for i in range(6):
            screen.blit(self.yellow_platform, self.platform_rect[i])





class Entity:

    def __init__(self):
        self.background = pygame.image.load('Graphics/background.png').convert_alpha()

    def draw_background_elements(self):
        border_rect_l = pygame.Rect(0, 0, w / 3, h)
        border_rect_r = pygame.Rect(w * 2 / 3, 0, w / 3, h)
        background_rect = pygame.Rect(w / 3, 0, w / 3, h)
        pygame.draw.rect(screen, (0, 0, 0), border_rect_l)
        pygame.draw.rect(screen, (0, 0, 0), border_rect_r)
        screen.blit(self.background, background_rect)


class Main:
    def __init__(self):
        self.doodle = Doodle()
        self.background = Entity()

    def update(self):
        self.doodle.vertical_movement()
        self.doodle.check_jump()
        self.doodle.scroll()

    def draw_elements(self):
        self.background.draw_background_elements()
        self.doodle.draw_doodle()
        self.doodle.draw_platform()

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
