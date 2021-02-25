import pygame
import random
import sys

from pygame.time import get_ticks

pygame.init()

# screen size
# Width and height
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
DEBUG = False
# Colors
color_white = (255, 255, 255)
color_black = (0, 0, 0)
color_red = (255, 0, 0)
color_green = (0, 255, 0)
color_blue = (0, 0, 255)
background_color = (194, 178, 128)
snake_block = 10

global snake_player
global snake_list

# Set the display after the screen size
# We call the var that holds the display for window
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# We set the name of the window SnakePython
# We set the name of the window SnakePython
pygame.display.set_caption("SnakePython")

CLOCK = pygame.time.Clock()

font_style = pygame.font.SysFont("Helvetica", 30)
fps = str(int(CLOCK.get_fps()))


def message(msg, xPos, yPos, color):
    msg = font_style.render(msg, True, color)
    window.blit(msg, [xPos, yPos])


def update_snake(snake_block, snake_list):
    for x in snake_list:
        global snake_player
        # snake_player = pygame.draw.rect(window, color_green, [xPos, yPos, snake_size, snake_size])
        snake_player = pygame.draw.rect(window, color_green, [x[0], x[1], snake_block, snake_block])


def snake():
    food_size = 10
    snake_size = 10
    snake_speed = 5
    snake_block = 10
    snake_length = 1

    xPos = SCREEN_WIDTH / 2
    yPos = SCREEN_HEIGHT / 2

    # Position for the food
    food_xPos = round(random.randrange(0, SCREEN_WIDTH - snake_block) / 10.0) * 10.0
    food_yPos = round(random.randrange(0, SCREEN_HEIGHT - snake_block) / 10.0) * 10.0

    update_xPos = 0
    update_yPos = 0

    snake_List = []
    Length_of_snake = 1
    FPS = str(int(CLOCK.get_fps()))

    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    update_xPos = 0
                    update_yPos = snake_speed
                elif event.key == pygame.K_UP:
                    update_xPos = 0
                    update_yPos = -snake_speed
                elif event.key == pygame.K_LEFT:
                    update_xPos = -snake_speed
                    update_yPos = 0
                elif event.key == pygame.K_RIGHT:
                    update_xPos = snake_speed
                    update_yPos = 0

        if xPos >= SCREEN_WIDTH or xPos < 0 or yPos >= SCREEN_HEIGHT or yPos < 0:
            snake()

        xPos += update_xPos
        yPos += update_yPos
        window.fill(background_color)
        # rect(display/screen, (color), (left,top,width,height, filled)
        # Draw snake
        # snake_player = pygame.draw.rect(window, color_green, [xPos, yPos, snake_size, snake_size])
        # Shows fps
        # message(f'FPS : {FPS}', 400, 20, color_black)
        message(f"SCORE : {score}", SCREEN_WIDTH/2-50, 20, color_black)
        # Draw food
        food = pygame.draw.rect(window, color_red, [food_xPos, food_yPos, food_size, food_size])

        snake_head = []
        snake_head.append(xPos)
        snake_head.append(yPos)
        snake_List.append(snake_head)

        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_head:
                snake()

        update_snake(snake_block, snake_List)

        if DEBUG == True:
            print(f'Snake position: x:{xPos}, y : {yPos}')
            print(f'Food position: x:{food_xPos}, y: {food_yPos}')

        collide = snake_player.colliderect(food)

        if collide:
            score += 1
            food_xPos = round(random.randrange(0, SCREEN_WIDTH - snake_block) / 10.0) * 10.0
            food_yPos = round(random.randrange(0, SCREEN_HEIGHT - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
        CLOCK.tick(65)
        pygame.display.update()


snake()
