# loaders
import pygame
import random
import menu
pygame.init()
screen = pygame.display.set_mode((1435, 1000))

# vars
x = 25
y = 0
o = 10
a = 10
d = 10
pipe_group = pygame.sprite.Group()
play_space = "main"

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
main_player = pygame.transform.scale(main_player, (170, 100))
point = pygame.image.load('Objects/coin.png').convert_alpha()
point = pygame.transform.scale(point, (70, 10))
point2 = pygame.image.load('Objects/coolcoin.png').convert_alpha()
point2 = pygame.transform.scale(point2, (70, 10))


# pipe class
class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, flipped=False):
        super().__init__()
        self.image = pygame.image.load('Objects/pipe.png').convert_alpha()
        if flipped:
            self.image = pygame.transform.flip(self.image, False, True)

        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.velocity = -5

    def update(self):
        self.rect.x += self.velocity


# main game loop
running = True
clock = pygame.time.Clock()

while running:

    screen.fill((239, 239, 239))

    # menu screen mode
    if play_space == "main":
        Bname.draw(screen)
        y-= 30
        if Bstart.draw(screen):
            play_space = "game"

    # game screen mode
    if play_space == "game":
        screen.blit(main_player, (x, y))
        screen.blit(point, (a, d))
        pipe_group.update()
        pipe_group.draw(screen)

        # hit_box logic
        hit_box = pygame.Rect(x, y, main_player.get_width(), main_player.get_height())
        for pipe in pipe_group:
            if hit_box.colliderect(pipe.rect):
                play_space = "over"
                print("yahoo")

        # spawn top bottom pipe
        if random.randint(1, 60) == 1:
            pipe_x = 1435
            gap = 250
            bottom_y = random.randint(400, 700)

            pipeB = Pipe(pipe_x, bottom_y, flipped=False)
            pipeT = Pipe(pipe_x, bottom_y - gap - pipeB.image.get_height(), flipped=True)

            pipe_group.add(pipeB)
            pipe_group.add(pipeT)

    # player movement
    keys = pygame.key.get_pressed()
    y += 4

    if keys[pygame.K_UP] or keys[pygame.K_w]:
        y -= o
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        y += o

    # if play_space == "over":

    # quit screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(90)

pygame.quit()
