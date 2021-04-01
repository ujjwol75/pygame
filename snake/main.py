import pygame
import random

#initialize the pygame
pygame.init()

#screen of device
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((600, 600))  

# snake variables
snake_x = 280
snake_y = 280
snake_size = 10
vel_x = 0
vel_y = 0

#food for snake variables
food_x = random.randint(0,screen_width)
food_y = random.randint(0,screen_width)
food_size = 10

#snake head
snake_list = []
score = 0
snake_length = 1 
font = pygame.font.Font('freesansbold.ttf', 20)

def scoreBoard():
    text = font.render("Score : " + str(score), True, (255, 255, 255))
    screen.blit(text, (5,5))

def gameOver():
    text = font.render("Game Over ", True, (255, 255, 255))
    screen.blit(text, (280,280))


def snakeCreate():
    for x,y in snake_list:
        pygame.draw.rect(screen, (187,187,187), (x, y, snake_size, snake_size))



running = True
while running:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    vel_x = -0.1
                    vel_y = 0
                elif event.key == pygame.K_RIGHT:
                    vel_x = 0.1
                    vel_y = 0
                elif event.key == pygame.K_UP:
                    vel_x = 0
                    vel_y = -0.1
                elif event.key == pygame.K_DOWN:
                    vel_x = 0
                    vel_y = 0.1

    snake_x = snake_x + vel_x
    snake_y = snake_y + vel_y

# food eating code
    if (abs(snake_x - food_x) <= 7) and (abs(snake_y - food_y) <= 7): 
        food_x = random.randint(0,screen_width)
        food_y = random.randint(0,screen_width)
        score += 100
        snake_length = snake_length + 100

# length of snake
    snake_head = []
    snake_head.append(snake_x)
    snake_head.append(snake_y)
    snake_list.append(snake_head)       

    if len(snake_list) > snake_length:
        del snake_list[0]

    screen.fill((0,0,0)) 
    snakeCreate()

    #collision text in boundries
    if snake_x <= 0 or snake_x >= 600:
        running = False
    elif snake_y <= 0 or snake_y >= 600:
        running = False
    
    
    scoreBoard()
    
    
    pygame.draw.rect(screen, (255,0,0), (food_x, food_y, food_size, food_size))

    pygame.display.update()
