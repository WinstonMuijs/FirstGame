import random

import pygame
import sys


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_walk1 = pygame.image.load("./characters/frame-1.png").convert_alpha()
        player_walk2 = pygame.image.load("./characters/frame-3.png").convert_alpha()
        self.player_move = [player_walk1, player_walk2]
        self.player_index = 0
        self.player_jump = pygame.image.load("./characters/jump.png").convert_alpha()

        self.image = self.player_move[self.player_index]
        self.rect = self.image.get_rect(midbottom=(200, 300))
        self.gravity = 0

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def animation_state(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_move): self.player_index = 0
            self.image = self.player_move[int(self.player_index)]

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()


def display_score():
    current_time = pygame.time.get_ticks() // 1000 - start_time
    score = text_font.render(f"Score: {current_time}", False, (97, 24, 237))
    score_rect = score.get_rect(center=(WINDOW_WIDTH / 2, 60))
    screen.blit(score, score_rect)
    return current_time


def enemy_movement(enemy_list):
    if enemy_list:
        for enemy_rec in enemy_list:
            enemy_rec.x -= 5
            if enemy_rec.bottom == 300:
                screen.blit(enemy, enemy_rec)
            else:
                screen.blit(flying_enemy, enemy_rec)

            # deleting obstacle when leaving screen.
        enemy_list = [enemie for enemie in enemy_list if enemie.x > -100]
        return enemy_list
    else:
        return []


def collisions(player, enemies):
    if enemies:
        for enemy in enemies:
            if player.colliderect(enemy):
                return False
    return True


def player_animation():
    global player, player_index
    if player_rect.bottom < 300:
        player = player_jump
    else:
        player_index += 0.1
        if player_index >= len(player_move): player_index = 0
        player = player_move[int(player_index)]


def end_game():
    screen.fill("dodgerblue4")
    text_top = text_font.render(f"PixelArt Game", False, "lightgreen").convert()
    # text_top = pygame.transform.scale2x(text_top)
    text_top_rect = text_top.get_rect(center=(WINDOW_WIDTH / 2, 60))
    image_player = pygame.image.load("./characters/character horn girl.png").convert_alpha()
    image_player = pygame.transform.rotozoom(image_player, 0, 1.5)
    image_rect = image_player.get_rect(center=(WINDOW_WIDTH / 2, 150))
    text_bottom = text_font.render(f"Press SpaceButton to play!", False, "red").convert()
    # text_bottom = pygame.transform.scale2x(text_bottom)
    text_bottom_rect = text_bottom.get_rect(center=(WINDOW_WIDTH / 2, 300))
    end_score = text_font.render(f"Your Score: {score}", False, "lightgreen").convert_alpha()
    end_score_rect = end_score.get_rect(center=(WINDOW_WIDTH / 2, 350))
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
score = 0

# timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 900)

# timer enemies
enemy_timer = pygame.USEREVENT + 2
pygame.time.set_timer(enemy_timer, 500)

# crab timer
crab_timer = pygame.USEREVENT + 3
pygame.time.set_timer(crab_timer, 200)

#  enemies
enemies_rect_list = []
enemy_one = pygame.image.load("./characters/1.png").convert_alpha()
enemy_two = pygame.image.load("./characters/4.png").convert_alpha()
enemy_move = [enemy_one, enemy_two]
enemy_index = 0
enemy = enemy_move[enemy_index]

enemy_rect = enemy.get_rect(midbottom=(600, 300))
# enemy_x_pos = 600


# crab enemy
crab_one = pygame.image.load("./characters/crab.png").convert_alpha()
crab_two = pygame.image.load("./characters/Naamloos-1.png").convert_alpha()
crab_move = [crab_one, crab_two]
crab_index = 0
flying_enemy = crab_move[crab_index]

# flying_enemy = pygame.image.load("./characters/frame4.png").convert_alpha()

# player
player1 = pygame.sprite.GroupSingle()
player1.add(Player())

player_walk1 = pygame.image.load("./characters/frame-1.png").convert_alpha()
player_walk2 = player = pygame.image.load("./characters/frame-3.png").convert_alpha()
player_move = [player_walk1, player_walk2]
player_index = 0
player_jump = pygame.image.load("./characters/jump.png").convert_alpha()
player = player_move[player_index]
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

            if event.type == obstacle_timer:
                if random.randint(0, 2):
                    enemies_rect_list.append(enemy.get_rect(midbottom=(random.randint(900, 1100), 300)))
                else:
                    enemies_rect_list.append(flying_enemy.get_rect(midbottom=(random.randint(900, 1100), 210)))

            if event.type == enemy_timer:
                if enemy_index == 0:
                    enemy_index = 1
                else:
                    enemy_index = 0
                enemy = enemy_move[enemy_index]

            if event.type == crab_timer:
                if crab_index == 0:
                    crab_index = 1
                else:
                    crab_index = 0
                flying_enemy = crab_move[crab_index]

        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_active = True
                    enemy_rect.x = 800
                    start_time = pygame.time.get_ticks() // 1000

    if game_active:  # game
        screen.blit(background_sky, (0, 0))
        screen.blit(background_ground, (0, 300))
        # pygame.draw.rect(screen, (226, 24, 135), score_rect.inflate(25, 25), width=8, border_radius=5)
        # screen.blit(text, score_rect)
        score = display_score()

        # enemy_rect.right -= 4
        # if enemy_rect.right <= 0:
        #     enemy_rect.left = 800
        # screen.blit(enemy, enemy_rect)

        # player

        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        player_animation()
        screen.blit(player, player_rect)
        player1.draw(screen)
        player1.update()



        # enemy movement
        enemies_rect_list = enemy_movement(enemies_rect_list)

        # collision
        game_active = collisions(player_rect, enemies_rect_list)

    else:  # intro
        end_game()
        enemies_rect_list.clear()
        player_rect.midbottom = (80, 300)
        player_gravity = 0

    pygame.display.update()
    clock.tick(60)
