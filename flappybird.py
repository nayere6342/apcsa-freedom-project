import pygame
pygame.init()
screen = pygame.display.set_mode((650, 650))

main_player = pygame.image.load('obj.png').convert()
main_player = pygame.transform.scale(main_player,
                                     (main_player.get_width() - 100,
                                     main_player.get_height() - 80))

running = True

x = 0
y = 90
o = 5
z = 300
clock = pygame.time.Clock()
while running:
    screen.fill((255, 255, 255))
    screen.blit(main_player, (x, y))

    hitbox = pygame.Rect(x, y, main_player.get_width(), main_player.get_height())
    z -= 1
    target = pygame.Rect(z, 0, 160, 180)
    collision = hitbox.colliderect(target)
    pygame.draw.rect(screen, (255 * collision, 255, 0), target)

    keys = pygame.key.get_pressed()
    y += 2
    if keys[pygame.K_UP]:
        y -= o
    if keys[pygame.K_DOWN]:
        y += o

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
    clock.tick(90)

pygame.quit()
