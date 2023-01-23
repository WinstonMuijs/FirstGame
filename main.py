import pygame
import sys


def display_score():
    current_time = pygame.time.get_ticks()//1000 - start_time
    score = text_font.render(f"Score: {current_time}", False, (97, 24, 237))
    score_rect = score.get_rect(center=(WINDOW_WIDTH / 2, 60))
    screen.blit(score, score_rect)
    return current_time


def end_game():
    screen.fill("dodgerblue4")
    text_top = text_font.render(f"PixelArt Game", False, "lightgreen").convert()
    # text_top = pygame.transform.scale2x(text_top)
    text_top_rect = text_top.get_rect(center=(WINDOW_WIDTH/2, 60))
    image_player = pygame.image.load("./characters/character horn girl.png").convert_alpha()
    image_player = pygame.transform.rotozoom(image_player, 0, 1.5)
    image_rect = image_player.get_rect(center=(WINDOW_WIDTH/2, 150))
    text_bottom = text_font.render(f"Press SpaceButton to play!", False, "red").convert()
    # text_bottom = pygame.transform.scale2x(text_bottom)
    text_bottom_rect = text_bottom.get_rect(center=(WINDOW_WIDTH/2, 300))
    end_score = text_font.render(f"Your Score: {score}", False, "lightgreen")
    end_score_rect = end_score.get_rect(center=(WINDOW_WIDTH/2, 350))
    if score >= 5:
        screen.blit(text_bottom, text_bottom_rect)
        # screen.blit(text_top, text_top_rect)
        screen.blit(image_player, image_rect)
        screen.blit(end_score, end_score_rect)
    else:

        screen.blit(text_top, text_top_rect)
        screen.blit(image_player, image_rect)
        screen.blit(text_bottom, text_bottom_rect)


pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 400
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Wonderland")

background_sky = pygame.image.load("./characters/background.png").convert_alpha()
background_ground = pygame.image.load("./characters/ground.png").convert_alpha()

text_font = pygame.font.Font("./font/Pixeltype.ttf", 50)
# text = text_font.render("My firstGame", False, (97, 24, 237))
# text_rect = text.get_rect(center=(WINDOW_WIDTH / 2, 60))

# start time
start_time = 0

# end score
score =0

enemy = pygame.image.load("./characters/1.png").convert_alpha()
enemy_rect = enemy.get_rect(midbottom=(600, 300))
enemy_x_pos = 600

player = pygame.image.load("./characters/plater2.png").convert_alpha()
player_rect = player.get_rect(midbottom=(80, 300))
player_gravity = 0

game_active = True

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                    player_gravity = -20
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_active = True
                    enemy_rect.x = 800
                    start_time = pygame.time.get_ticks()//1000

    if game_active:  # game
        screen.blit(background_sky, (0, 0))
        screen.blit(background_ground, (0, 300))
        # pygame.draw.rect(screen, (226, 24, 135), score_rect.inflate(25, 25), width=8, border_radius=5)
        # screen.blit(text, score_rect)
        score = display_score()

        enemy_rect.right -= 4
        if enemy_rect.right <= 0:
            enemy_rect.left = 800
        screen.blit(enemy, enemy_rect)

        # player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player, player_rect)

        # collision
        if player_rect.colliderect(enemy_rect):
            game_active = False
    else:  # intro
        end_game()

    pygame.display.update()
    clock.tick(60)
