import pygame
import sys

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 400
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Wonderland")

background_sky = pygame.image.load("./characters/arcadeV2.png").convert_alpha()
background_ground = pygame.image.load("./characters/ground.png").convert_alpha()

text_font = pygame.font.Font("./font/Pixeltype.ttf", 50)
text = text_font.render("My firstGame", False, "dodgerblue4")

enemy = pygame.image.load("./characters/1.png").convert_alpha()
enemy_x_pos = 600

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(background_sky, (0, 0))
    screen.blit(background_ground, (0, 300))
    screen.blit(text, (300, 50))
    enemy_x_pos -= 4
    if enemy_x_pos < -100:
        enemy_x_pos = 800
    screen.blit(enemy, (enemy_x_pos, 250))
    pygame.display.update()
    clock.tick(60)
