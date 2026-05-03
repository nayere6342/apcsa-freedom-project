# loaders
import pygame
import random
import menu
pygame.init()
screen = pygame.display.set_mode((1435, 1000))

# starter vars
x = 25
y = 0
o = 10
a = 0
d = 500
p = 0
f = 90

# powerup timers
pf1 = 1500
pf2 = 40
pf3 = 2200
ref = 3000

# powerup vars
powerplay = 1
xc = 1
b = 0
xf = 0
sx = 170
sy = 100

# object array
pipe_group = pygame.sprite.Group()
coin_group = pygame.sprite.Group()

# main menu
play_space = "main"

pygame.display.set_caption('Flappy Bird: Absolute Remixed')
Play = pygame.image.load('Objects/play.png').convert_alpha()
Name = pygame.image.load('Objects/title.png').convert_alpha()
fake_player = pygame.image.load('Objects/flappy.png').convert_alpha()
fake_player2 = pygame.image.load('Objects/flappy.png').convert_alpha()
fake_player3 = pygame.image.load('Objects/flappy.png').convert_alpha()
fake_pipe = pygame.image.load('Objects/pipe.png').convert_alpha()
fake_pipe2 = pygame.image.load('Objects/pipe.png').convert_alpha()
fake_juice = pygame.image.load('Objects/sillyb_juice.png').convert_alpha()

fake_player = pygame.transform.scale(fake_player, (170, 120))
fake_player = pygame.transform.rotate(fake_player, -90)
fake_player2 = pygame.transform.scale(fake_player2, (170, 120))
fake_player2 = pygame.transform.rotate(fake_player2, -90)
fake_player3 = pygame.transform.scale(fake_player3, (170, 120))
fake_player3 = pygame.transform.rotate(fake_player3, -90)
fake_pipe = pygame.transform.rotate(fake_pipe, 90)
fake_pipe2 = pygame.transform.rotate(fake_pipe2, 90)
fake_juice = pygame.transform.rotate(fake_juice, 30)
fake_juice = pygame.transform.scale(fake_juice, (170, 150))
Name = pygame.transform.scale(Name, (670, 550))
Play = pygame.transform.scale(Play, (420, 200))
Play = pygame.transform.rotate(Play, -10)

Bstart = menu.Press(950, 580, Play)
Bname = menu.Press(150, 20, Name)
Fplay = menu.Press(20, 700, fake_player)
Fplay2 = menu.Press(20, -60, fake_player2)
Fplay3 = menu.Press(20, 200, fake_player3)
Fpipe = menu.Press(1100, 10, fake_pipe)
Fpipe2 = menu.Press(1250, 300, fake_pipe2)
FJ = menu.Press(780, 120, fake_juice)

# game objects
main_player = pygame.image.load('Objects/flappy.png').convert_alpha()
main_player = pygame.transform.scale(main_player, (sx, sy))


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


# coin class
class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('Objects/coin.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 90))
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
    powerplay = 0
    # menu screen mode
    if play_space == "main":
        y = 0
        Bname.draw(screen)
        Fplay.draw(screen)
        Fplay2.draw(screen)
        Fplay3.draw(screen)
        Fpipe.draw(screen)
        Fpipe2.draw(screen)
        FJ.draw(screen)
        if Bstart.draw(screen):
            play_space = "game"

    # game screen mode
    if play_space == "game":
        screen.blit(main_player, (x, y))

        # object mov + update
        coin_group.update()
        coin_group.draw(screen)
        pipe_group.update()
        pipe_group.draw(screen)

        # point display
        F = pygame.font.SysFont('Arial', 30)
        T = F.render('Points: ' + str(p), True, (220, 46, 191))
        T = pygame.transform.scale(T, (300, 100))
        screen.blit(T, (0, 10))

        # fps speed up
        xr = random.randint(1, 300)
        if xr == 300 or xr <= 50:
            if p >= 20 and xf == 1:
                f += 10
                print(f)
                xf = 0
            if p >= 40 and xr >= 100:
                xf = 1

        # hit_box logic
        hit_box = pygame.Rect(x, y, main_player.get_width(), main_player.get_height())

        for pipe in pipe_group:
            if hit_box.colliderect(pipe.rect):
                b = 1
                play_space = "over"
                print("yahoo")

        for point in coin_group:
            if hit_box.colliderect(point.rect):
                p += 1
                point.kill()
                print(p)
                print("money")

        # spawn top + bottom pipe
        if random.randint(1, 60) == 1:
            pipe_x = 1435

            # pipe surface
            if len(pipe_group) == 0 or pipe_group.sprites()[-1].rect.x < 1000:
                gap = 350
                bottom_y = random.randint(400, 700)
                # bottom_x = random.randint(300, 100)
                # bottom_y2 = random.randint(-400, -700)

                pipeB = Pipe(pipe_x, bottom_y, flipped=False)
                pipeT = Pipe(pipe_x, bottom_y - gap - pipeB.image.get_height(), flipped=True)

                pipe_group.add(pipeB)
                pipe_group.add(pipeT)

        # coin spawn randomness
        if random.randint(1, 100) == 1:
            coin_group.add(Coin(1435, random.randint(200, 800)))

    # player controls
    keys = pygame.key.get_pressed()
    y += 4

    # pause/play/quit
    if keys[pygame.K_ESCAPE]:
        play_space = "main"

    if keys[pygame.K_q]:
        running = False

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB and play_space == "game":
                A = pygame.font.SysFont('Arial', 30)
                ZZ = A.render('Paused! ', True, (220, 215, 46))
                ZZ = pygame.transform.scale(ZZ, (600, 300))
                screen.blit(ZZ, (500, 300))
                pygame.display.flip()
                clock.tick(.1)

    # player mov
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        y -= o
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        y += o

    # powerup system
    ref -= 50

    # becomes invincible (silly billy juice)
    if p >= 20 and b <= 1 and powerplay == 0 and ref <= 0:
        if keys[pygame.K_1]:
            pf1 -= 1

            drink = pygame.image.load('Objects/sillyb_juice.png').convert_alpha()
            drink = pygame.transform.scale(drink, (70, 70))
            screen.blit(drink, (x+20, y))
            print(pf1)

            if xc == 1:
                play_space = "game"

            if pf1 <= 0:
                U = pygame.font.SysFont('Arial', 30)
                TT = U.render('!!! ', True, (46, 220, 128))
                TT = pygame.transform.scale(TT, (300, 200))
                screen.blit(TT, (300, 350))
                b = 0
                xc = 0
                pf1 = 1500
                ref = 3000
    if powerplay == 0 and play_space == "game":
        SBJ = pygame.image.load('Objects/J_locked.png').convert_alpha()
        SBJ = pygame.transform.scale(SBJ, (174, 148))
        screen.blit(SBJ, (0, 700))
    if p >= 20 and play_space == "game":
        SBJ = pygame.image.load('Objects/J_unlocked.png').convert_alpha()
        SBJ = pygame.transform.scale(SBJ, (174, 148))
        screen.blit(SBJ, (2, 700))

    # point boost (cool coin)
    if p >= 90 and powerplay == 0 and ref <= 0:
        if keys[pygame.K_2]:
            pf2 -= 1

            double = pygame.image.load('Objects/coolcoin.png').convert_alpha()
            double = pygame.transform.scale(double, (70, 70))
            screen.blit(double, (x, y-5))
            print(pf2)

            if xc == 1:
                p += 1

            if pf2 <= 0:
                U = pygame.font.SysFont('Arial', 30)
                TT = U.render('!!! ', True, (46, 220, 128))
                TT = pygame.transform.scale(TT, (300, 200))
                screen.blit(TT, (300, 350))
                b = 0
                xc = 0
                pf2 = 40
                ref = 3000
    if powerplay == 0 and play_space == "game":
        CC = pygame.image.load('Objects/C_locked.png').convert_alpha()
        CC = pygame.transform.scale(CC, (174, 148))
        screen.blit(CC, (140, 700))
    if p >= 90 and play_space == "game":
        CC = pygame.image.load('Objects/C_unlocked.png').convert_alpha()
        CC = pygame.transform.scale(CC, (174, 148))
        screen.blit(CC, (142, 700))

    # smaller size (cool coin)
    if p >= 140 and powerplay == 0 and ref <= 0:
        if keys[pygame.K_3]:
            pf3 -= 1

            double = pygame.image.load('Objects/orb.png').convert_alpha()
            double = pygame.transform.scale(double, (70, 70))
            screen.blit(double, (x, y-5))
            print(pf3)

            if xc == 1:
                sx = 70
                sy = 70
                main_player = pygame.transform.scale(main_player, (sx, sy))

            if pf3 <= 0:
                U = pygame.font.SysFont('Arial', 30)
                TT = U.render('!!! ', True, (46, 220, 128))
                TT = pygame.transform.scale(TT, (300, 200))
                screen.blit(TT, (300, 350))
                b = 0
                xc = 0
                pf3 = 2200
                ref = 3000
                sx = 170
                sy = 100
    if powerplay == 0 and play_space == "game":
        OB = pygame.image.load('Objects/O_locked.png').convert_alpha()
        OB = pygame.transform.scale(OB, (174, 148))
        screen.blit(OB, (300, 700))
    if p >= 140 and play_space == "game":
        OB = pygame.image.load('Objects/O_unlocked.png').convert_alpha()
        OB = pygame.transform.scale(OB, (174, 148))
        screen.blit(OB, (302, 700))

    # game over screen
    if play_space == "over":
        powerplay = 1
        a += 10
        d = 470

        fake_player = pygame.image.load('Objects/flappy.png').convert_alpha()
        fake_player = pygame.transform.scale(fake_player, (470, 300))
        fake_player = pygame.transform.rotate(fake_player, 1600)

        Over = pygame.image.load('Objects/over.png').convert_alpha()
        Over = pygame.transform.scale(Over, (1200, 500))

        Retry = pygame.image.load('Objects/retry.png').convert_alpha()

        F = pygame.font.SysFont('Arial', 30)
        T = F.render('Points: ' + str(p), True, (220, 46, 191))
        T = pygame.transform.scale(T, (300, 100))

        screen.blit(T, (0, 700))
        Btry = menu.Press(500, 540, Retry)
        screen.blit(Over, (100, 10))
        screen.blit(fake_player, (d, a))

        for pipe in pipe_group:
            pipe.kill()
        for point in coin_group:
            point.kill()

        if play_space == "over":
            if Btry.draw(screen):
                y = 0
                a = 0
                p = 0
                b = 0
                xc = 1
                pf1 = 1500
                pf2 = 20
                pf3 = 1500
                pf4 = 1500
                powerplay = 0
                f = 90
                sx = 170
                sy = 100
                play_space = "game"

    # quit screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fps
    pygame.display.flip()
    clock.tick(f)


pygame.quit()

