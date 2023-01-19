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
enemy_rect = enemy.get_rect(midbottom=(600, 300))
enemy_x_pos = 600

player = pygame.image.load("./characters/plater2.png").convert_alpha()
player_rect = player.get_rect(midbottom=(80, 300))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(background_sky, (0, 0))
    screen.blit(background_ground, (0, 300))
    screen.blit(text, (300, 50))
    enemy_rect.right -= 4
    if enemy_rect.right <= 0:
        enemy_rect.left = 800
    screen.blit(enemy, enemy_rect)
    screen.blit(player, player_rect)
    pygame.display.update()
    clock.tick(60)
