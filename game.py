import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

player = pygame.Rect(WIDTH//2 - 20, HEIGHT-60, 40, 40)
vel_y = 0
on_ground = True
speed = 5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= speed
    if keys[pygame.K_RIGHT]:
        player.x += speed
    if keys[pygame.K_SPACE] and on_ground:
        vel_y = -12
        on_ground = False

    vel_y += 0.5
    player.y += int(vel_y)
    if player.y >= HEIGHT - 60:
        player.y = HEIGHT - 60
        vel_y = 0
        on_ground = True

    screen.fill((30, 30, 30))
    pygame.draw.rect(screen, (200, 60, 80), player)
    pygame.display.flip()
    clock.tick(60)
