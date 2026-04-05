# loaders
import pygame
import random
random.random()
pygame.init()
screen = pygame.display.set_mode((1600, 1000))

# vars
x = 0
y = 90
o = 10
z = 300
a = 330
d = 230
pipe_group = pygame.sprite.Group()
pipe_group2 = pygame.sprite.Group()

# game objects
main_player = pygame.image.load('Objects/obj.png').convert()
main_player = pygame.transform.scale(main_player,
                                     (main_player.get_width() - 100,
                                      main_player.get_height() - 80))

pipe = pygame.image.load('Objects/pipe.png').convert()
pipe = pygame.transform.scale(pipe,
                                     (pipe.get_width() - 100,
                                      pipe.get_height() - 80))


# loop logic
running = True
clock = pygame.time.Clock()
while running:
    screen.fill((239, 100, 239))
    screen.blit(main_player, (x, y))

    # hit-box logic & pipe mov
    hit_box = pygame.Rect(x, y, main_player.get_width(), main_player.get_height())
    z -= 1



    # pipe bot
    class Pipe(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('Objects/pipe.png').convert()
            self.rect = self.image.get_rect()
            self.rect.topleft = (z, a)
            self.velocity = random.randint(1, 1)

        def update(self):
            self.rect.y += self.velocity

    sillynum = random.randint(1, 5)

    # mov loop
    for i in range(1):
        if (sillynum == 2):
            pipe_group.add(pipe)
        pipe = Pipe(i + 400, -20)






    pipe_group.update()
    pipe_group.draw(screen)



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

    # displays everything on the window
    pygame.display.flip()

    # fps
    clock.tick(90)


pygame.quit()
