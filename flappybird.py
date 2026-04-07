# loaders
import pygame
import random
import menu
random.random()
pygame.init()
screen = pygame.display.set_mode((1435, 1000))


# vars
x = 25
y = 90
o = 10
z = 300
a = 330
pipe_group = pygame.sprite.Group()


# main menu
pygame.display.set_caption('Flappy Bird: Absolute Remixed')
Play = pygame.image.load('Objects/play_N.png').convert_alpha()
Name = pygame.image.load('Objects/title.png').convert_alpha()
Name = pygame.transform.scale(Name, (670, 550))
Play = pygame.transform.rotate(Play, -10)
Bstart = menu.Press(950, 640, Play)
Bname = menu.Press(30, 10, Name)


# game objects
main_player = pygame.image.load('Objects/flappy.png').convert_alpha()
main_player = pygame.transform.scale(main_player, (150, 100))


pipe = pygame.image.load('Objects/pipe.png').convert_alpha()


# pipe math
class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Objects/pipe.png').convert()
        self.rect = self.image.get_rect()
        self.rect.topleft = (z, a)
        self.velocity = -.5

    def update(self):
        self.rect.y += self.velocity


# main game loop
running = True
clock = pygame.time.Clock()
while running:

    # screen base setup
    screen.fill((239, 100, 239))
    if Bstart.draw(screen):
        print("yay")
    Bname.draw(screen)
    screen.blit(main_player, (x, y))

    # displays everything on the window
    pipe_group.update()
    pipe_group.draw(screen)
    pygame.display.flip()

    # hit-box logic & pipe mov
    hit_box = pygame.Rect(x, y, main_player.get_width(), main_player.get_height())
    z -= 1

    # spawn pipe
    for i in range(1):
        if random.randint(1, 100) == 1:
            pipe_group.add(Pipe(1600, random.randint(0, 500)))


    # mov pipe
        pipe = Pipe(400, -20)
        pipe_group.add(pipe)


    # player inputs
    keys = pygame.key.get_pressed()
    y += 4

    if keys[pygame.K_UP]:
        y -= o
    if keys[pygame.K_DOWN]:
        y += o
    if keys[pygame.K_w]:
        y -= o
    if keys[pygame.K_s]:
        y += o

    # allows the play window to be cut
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fps
    clock.tick(90)

pygame.quit()
