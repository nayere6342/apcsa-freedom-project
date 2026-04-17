# Entry #5: _PyGame Aftermath_
## Flappy Bird: Absolute Remixed
## Nayer Ebraheim
## 4/13/26

### Intro:

The aftermath of my project is was good. I got through all of my MVP deadlines and was able to put that into my project and get it to work. The main thing I wanted to try and fix first was the logic for the pipe movement so that the main loop of the game could work. Another one I had to solve was the lag because the pipe logic wasn't made in the best way so it would run slowly. Which was the only other thing I had to do then, so that my game could run smoothly and work well.   

### Code Presentation:

Moving on, the game can be broken down into three part: First the main menu is shown to the player. Which if done, will render everything to the player, the pipe, etc. After that is the main game loop, how it works is simple it handles everything in the game to the gravity to the collision detection system with the player and the pipe.   
    
**Preview:**
```py
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
p = 0
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

        # hit_box logic
        hit_box = pygame.Rect(x, y, main_player.get_width(), main_player.get_height())

        for pipe in pipe_group:
            if hit_box.colliderect(pipe.rect):
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

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and p >= 10:
                play_space = "game"
                print("booyah")

    # mov
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        y -= o
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        y += o

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
                play_space = "game"

    # quit screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(90)

pygame.quit()
```

### Design Process:

  

### Skills / Reflation: 



### Challenges & Takeaways:

* A challenge I had while working on this was that it was hard to read the code examples online because I thought that pygame was a one to one copy of python but there are a ton of differences to it even though it's just a library.

    * I know that pygame is meant to be for smaller projects but when going into it I didn't know how to be able to read just because it was in Python. But I was able to go through it by first learning the Python syntax

* Another challenge that was a real issue was I couldn't find the things I wanted to do like for example a player sprite being able to walk off screen and back. 

* Another takeaway was that I needed a clear plan of what this game was going to be about since I didn't have one. By having one I would be able to know how I should start the game.
  
    * Since, without a clear plan I wouldn't be able to know what to do with the game or even the MVP. Just because flappy bird is a simple game doesn't mean I should have a plan on what I should do. 

* The last takeaway from this was that I needed to tinker with `pygame` to help me to understand how to use it.
  
    * In order to truly understand it since a lot of the code I know how to write is just JS. So being able to learn Python is important for me. 
 

---
### Links:

* [Pygame Docs](https://www.pygame.org/docs/)
  
    * [Pygame Full Repo](https://github.com/pygame)

    * [Pygame Examples](https://github.com/pygame/pygame/tree/main/examples)

* [Pygame Wiki](https://www.pygame.org/wiki/)

* [APCSA Notes](https://docs.google.com/document/d/1T4-EjM0x1HFrLtcUZF7B3Krb1lLYcnjwKDmR2nVX4wE/edit?tab=t.0#heading=h.g70gkuk13014)
---

[Previous](entry03.md) | [Next](entry05.md)

[Home](../README.md)

dddd
