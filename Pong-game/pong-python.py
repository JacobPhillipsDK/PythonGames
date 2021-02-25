import pygame
import sys
import random
from Paddle import paddle
from ball import Ball

pygame.init()

# Used to control the FPS
GAME_FPS = 120

# screen size |  Width and height
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

# Colors
color_white = (255, 255, 255)
color_black = (0, 0, 0)

# Set the display after the screen size # We call the var that holds the display for window
window = pygame.display.set_mode(SCREEN_SIZE)
window.fill(color_black)

# We set the name of the window Pong Game
pygame.display.set_caption("Pong Game written in Python")

CLOCK = pygame.time.Clock()

font_style = pygame.font.SysFont("bit5x3", 50)

paddle_length = 50
paddle_block = 10

# Object of the class Paddle
player1 = paddle(color_white, paddle_block, paddle_length)
player1.rect.x = 5
player1.rect.y = SCREEN_HEIGHT / 2 - 20
# Object of the class Paddle
player2 = paddle(color_white, paddle_block, paddle_length)
player2.rect.x = 685
player2.rect.y = SCREEN_HEIGHT / 2 - 20

# Ball
ball = Ball(color_white, 10, 10)
ball.rect.x = 345
ball.rect.y = 195

all_sprites_list = pygame.sprite.Group()

# Add the paddles to the list of sprites
all_sprites_list.add(player1)
all_sprites_list.add(player2)
all_sprites_list.add(ball)

# Fps counter
FPS = str(int(CLOCK.get_fps()))


def message(msg, xPos, yPos, color):
    msg = font_style.render(msg, True, color)
    window.blit(msg, [xPos, yPos])


def pong_game():
    # Left and right score points holder
    left_score = 0
    right_score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Move with paddle with user arrow keys player1 and PLayer B use W/s        
        key_input = pygame.key.get_pressed()
        if key_input[pygame.K_w]:
            player1.moveUp(5)
        if key_input[pygame.K_s]:
            player1.moveDown(5)
        if key_input[pygame.K_UP]:
            player2.moveUp(5)
        if key_input[pygame.K_DOWN]:
            player2.moveDown(5)

        # --- Game logic should go here
        all_sprites_list.update()

        # Check if the ball is bouncing against any of the 4 walls:
        # Check if the ball is bouncing against any of the 4 walls:
        if ball.rect.x >= 690:
            left_score += 1
            #ball.velocity[0] = -ball.velocity[0]
            ball.rect.x = SCREEN_WIDTH /2
            ball.rect.y = SCREEN_HEIGHT /2
        if ball.rect.x <= 0:
            right_score += 1
            ball.rect.x = SCREEN_WIDTH / 2
            ball.rect.y = SCREEN_HEIGHT / 2
            #ball.velocity[0] = -ball.velocity[0]
        if ball.rect.y > 490:
            ball.velocity[1] = -ball.velocity[1]
        if ball.rect.y < 0:
            ball.velocity[1] = -ball.velocity[1]

        if pygame.sprite.collide_mask(ball, player1) or pygame.sprite.collide_mask(ball, player2):
            ball.bounce()

        window.fill(color_black)

        # All code that draw stuff should be here

        # Draws The line centered in the middle of the screen
        pygame.draw.line(window, color_white, (SCREEN_WIDTH / 2, 0), (SCREEN_WIDTH / 2, 500), 1)

        # Draws the player blocks in each side of the screen

        message(f'{left_score}', SCREEN_WIDTH / 2 - 150, 30, color_white)
        message(f'{right_score}', SCREEN_WIDTH / 2 + 150, 30, color_white)

        # Draw center rect
        all_sprites_list.draw(window)

        # Display score

        pygame.display.flip()
        # FPS of the game - Amount of time the screen updates in
        CLOCK.tick(GAME_FPS)


pong_game()
