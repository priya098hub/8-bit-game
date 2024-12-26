import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 720, 720
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
COLORS = [RED, GREEN, BLUE, (255, 165, 0), (75, 0, 130)]  # Added more colors

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge the Enemy")

# Set up the font
font = pygame.font.SysFont('Corbel', 35)

# Set up the clock
clock = pygame.time.Clock()

# Set up the player
player_size = 40
player_pos = [100, HEIGHT / 2]
player_speed = 5

# Set up the enemy
enemy_size = 50
enemy_pos = [WIDTH, random.randint(50, HEIGHT - 50)]
enemy_speed = 3
enemy_color = random.choice(COLORS)  # Assign a random color to the enemy

# Set up the score and high score
score = 0
high_score = 0

# Set up the game over flag
game_over = False

# Function to draw text
def draw_text(text, x, y):
    text_surface = font.render(text, True, WHITE)
    screen.blit(text_surface, (x, y))

# Function to draw the player
def draw_player():
    pygame.draw.rect(screen, RED, (player_pos[0], player_pos[1], player_size, player_size))

# Function to draw the enemy
def draw_enemy():
    pygame.draw.rect(screen, enemy_color, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get the current key presses
    keys = pygame.key.get_pressed()

    # Move the player
    if keys[pygame.K_UP]:
        player_pos[1] -= player_speed
    if keys[pygame.K_DOWN]:
        player_pos[1] += player_speed

    # Move the enemy
    enemy_pos[0] -= enemy_speed
    if enemy_pos[0] < 0:
        enemy_pos[0] = WIDTH
        enemy_pos[1] = random.randint(50, HEIGHT - 50)
        enemy_speed += 0.5  # Increase speed as the game progresses
        enemy_color = random.choice(COLORS)  # Change enemy color randomly

    # Check for collisions
    if (player_pos[0] < enemy_pos[0] + enemy_size and
        player_pos[0] + player_size > enemy_pos[0] and
        player_pos[1] < enemy_pos[1] + enemy_size and
        player_pos[1] + player_size > enemy_pos[1]):
        game_over = True
        high_score = max(high_score, score)  # Update high score if the current score is higher

    # Draw everything
    screen.fill((65, 25, 64))
    draw_player()
    draw_enemy()
    draw_text('Score: ' + str(score), 10, 10)
    draw_text('High Score: ' + str(high_score), 10, 50)

    # Update the score
    if not game_over:
        score += 1

    # Check for game over
    if game_over:
        screen.fill((65, 25, 64))
        draw_text('Game Over', WIDTH / 2 - 100, HEIGHT / 2 - 50)
        draw_text('Press any key to restart', WIDTH / 2 - 150, HEIGHT / 2 + 10)
        draw_text('High Score: ' + str(high_score), WIDTH / 2 - 120, HEIGHT / 2 + 60)
        pygame.display.flip()
        
        # Wait for player to restart the game
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    # Reset the game
                    player_pos = [100, HEIGHT / 2]
                    enemy_pos = [WIDTH, random.randint(50, HEIGHT - 50)]
                    enemy_speed = 3
                    enemy_color = random.choice(COLORS)
                    score = 0
                    game_over = False
                    waiting = False

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)
