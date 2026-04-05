# pipe top
target = pygame.Rect(z, 0, 120, 190)
collision = hit_box.colliderect(target)
pygame.draw.rect(screen, (255 * collision, 255, 0), target)

# pipe bottem
target = pygame.Rect(z, 500, 120, 190)
collision = hit_box.colliderect(target)
pygame.draw.rect(screen, (255 * collision, 255, 0), target)