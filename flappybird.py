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
a = 0
d = 500
p = 40
f = 90
b = 0
xc = 1
powerplay = True
pf1 = 1500
pf2 = 720
pf3 = 1500
pf4 = 1500

pipe_group = pygame.sprite.Group()
coin_group = pygame.sprite.Group()
play_space = "main"

# main menu
pygame.display.set_caption('Flappy Bird: Absolute Remixed')
Play = pygame.image.load('Objects/play.png').convert_alpha()
Name = pygame.image.load('Objects/title.png').convert_alpha()
Name = pygame.transform.scale(Name, (670, 550))
Play = pygame.transform.scale(Play, (420, 200))
Play = pygame.transform.rotate(Play, -10)

Bstart = menu.Press(950, 580, Play)
Bname = menu.Press(30, 10, Name)

# game objects
main_player = pygame.image.load('Objects/flappy.png').convert_alpha()
main_player = pygame.transform.scale(main_player, (170, 100))


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

    # menu screen mode
    if play_space == "main":
        y = 0
        Bname.draw(screen)
        if Bstart.draw(screen):
            play_space = "game"

    # game screen mode
    if play_space == "game":
        screen.blit(main_player, (x, y))

        coin_group.update()
        coin_group.draw(screen)
        pipe_group.update()
        pipe_group.draw(screen)

        # point display
        F = pygame.font.SysFont('Arial', 30)
        T = F.render('Points: ' + str(p), True, (220, 46, 191))
        T = pygame.transform.scale(T, (300, 100))
        screen.blit(T, (0, 10))

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

        # spawn top bottom pipe
        if random.randint(1, 60) == 1:
            pipe_x = 1435

            # prevent overlap (only spawn if last pipe is far enough)
            if len(pipe_group) == 0 or pipe_group.sprites()[-1].rect.x < 1000:
                gap = 350
                bottom_y = random.randint(400, 700)

                pipeB = Pipe(pipe_x, bottom_y, flipped=False)
                pipeT = Pipe(pipe_x, bottom_y - gap - pipeB.image.get_height(), flipped=True)

                pipe_group.add(pipeB)
                pipe_group.add(pipeT)

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

    # mov
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        y -= o
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        y += o

    # powerup system

    # extra life (silly billy juice)
    if p >= 10 and b <= 1:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    pf1 -= 1
                    drink = pygame.image.load('Objects/sillyb_juice.png').convert_alpha()
                    drink = pygame.transform.scale(drink, (70, 70))
                    screen.blit(drink, (x+20, y))
                    print(pf1)

                    if xc == 1:
                        play_space = "game"

                    if pf1 <= 0:
                        U = pygame.font.SysFont('Arial', 30)
                        TT = U.render('Power Down! ', True, (46, 220, 128))
                        TT = pygame.transform.scale(TT, (300, 200))
                        screen.blit(TT, (150, 540))
                        b = 0
                        xc = 0
                        pf = 1500

    # double points (cool coin)
    if p >= 40:
        if keys[pygame.K_2]:
            pf2 -= 1
            double = pygame.image.load('Objects/coolcoin.png').convert_alpha()
            double = pygame.transform.scale(double, (70, 70))
            screen.blit(double, (x, y-5))
            print(pf2)

            if xc == 1:
                for point in coin_group:
                    if hit_box.colliderect(point.rect):
                        p += 1

            if pf2 <= 0:
                U = pygame.font.SysFont('Arial', 30)
                TT = U.render('Power Down! ', True, (46, 220, 128))
                TT = pygame.transform.scale(TT, (300, 200))
                screen.blit(TT, (150, 540))
                b = 0
                xc = 0
                pf = 720

    # game over screen
    if play_space == "over":
        a += 10
        d = 500

        fake_player = pygame.image.load('Objects/flappy.png').convert_alpha()
        fake_player = pygame.transform.scale(fake_player, (470, 300))
        fake_player = pygame.transform.rotate(fake_player, 1600)

        Over = pygame.image.load('Objects/over.png').convert_alpha()
        Over = pygame.transform.scale(Over, (1200, 500))

        Retry = pygame.image.load('Objects/retry.png').convert_alpha()

        F = pygame.font.SysFont('Arial', 30)
        T = F.render('Points: ' + str(p), True, (220, 46, 191))
        T = pygame.transform.scale(T, (300, 100))

        screen.blit(T, (0, 500))
        Btry = menu.Press(950, 640, Retry)
        screen.blit(Over, (10, 10))
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
                play_space = "game"

    # quit screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(f)


pygame.quit()
