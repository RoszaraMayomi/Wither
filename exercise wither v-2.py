import pygame
import time
import random

#

pygame.init()
#global variables
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 0)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Wither')

#icon =
#pygame.set_icon(icon)

#snakeHeadIMG =
#appleimg =

clock = pygame.time.Clock()

AppleThickness = 30
block_size = 20
FPS = 15

direction = 'right'

smallfont = pygame.font.SysFont('comicsansms', 25)
medfont = pygame.font.SysFont('comicsansms', 50)
largefont = pygame.font.SysFont('comicsansms', 80)

#functions
def game_start():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        gameDisplay.fill(white)
        message_to_screen('Welcome to Wither', green, -100, size='large')
        message_to_screen('Objective: EAT APPLES', black, -30)
        message_to_screen('Objective: GET LONG', black, 10)
        message_to_screen('Objective: TOUCH NOTHING', black, 50)

        message_to_screen('Press C to play or Q to quit', black, 180)

        pygame.display.update()
        clock.tick(15)

def snake(block_size, snakeList):

    for XnY in snakeList:
        pygame.draw.rect(gameDisplay, green, [XnY[0], XnY[1], block_size, block_size])

def text_objects(text, color, size):
    if size == 'small':
        textSurface = smallfont.render(text, True, color)
    elif size == 'medium':
        textSurface = medfont.render(text, True, color)
    elif size == 'large':
        textSurface = largefont.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_to_screen(msg, color, y_displace=0, size='small'):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (display_width / 2), (display_height / 2) + y_displace
    gameDisplay.blit(textSurf, textRect)

def randAppleGen():
    randAppleX = round(random.randrange(0, display_width - AppleThickness))
    randAppleY = round(random.randrange(0, display_height - AppleThickness))
    return randAppleX, randAppleY

def randPoisonGen():
    randPoisonX = round(random.randrange(0, display_width - AppleThickness))
    randPoisonY = round(random.randrange(0, display_height - AppleThickness))
    return randPoisonX, randPoisonY
    
def gameLoop():
    global direction

    direction = 'right'
    gameExit = False
    gameOver = False

    lead_x = display_width / 2
    lead_y = display_height / 2

    lead_x_change = 10
    lead_y_change = 0

    snakeList = []
    snakeLength = 1

    randAppleX, randAppleY = randAppleGen()
    randPoisonX, randPoisonY = randPoisonGen()
#mainLoop
    while not gameExit:

        while gameOver == True:

            gameDisplay.fill(white)
            message_to_screen("Game OVER", red, y_displace=-50, size='large')
            message_to_screen('Press C to play again to Q to Quit', black, 50, size='medium')
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameOver = False
                        gameExit = True

                    if event.key == pygame.K_c:
                        gameLoop()
                
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = - block_size
                    lead_y_change = 0
                    direction = 'left'
                if event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                    direction = 'right'
                if event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                    direction = 'up'
                if event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0
                    direction = 'down'

        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            gameOver = True

        lead_x += lead_x_change
        lead_y += lead_y_change

        gameDisplay.fill(white)

        pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, AppleThickness, AppleThickness])
        pygame.draw.rect(gameDisplay, black, [randPoisonX, randPoisonY, AppleThickness, AppleThickness])

        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]
        if snakeLength <= 0:
            gameOver = True

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True

#fixing finite collision for both apple and poison variables instead of only top left trigger
        if lead_x > randAppleX and lead_x < randAppleX + AppleThickness or lead_x + block_size > randAppleX and lead_x + block_size < randAppleX + AppleThickness:
            if lead_y > randAppleY and lead_y < randAppleY + AppleThickness or lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + AppleThickness:
                randAppleX, randAppleY = randAppleGen()
                snakeLength += 1

        if lead_x > randPoisonX and lead_x < randPoisonX + AppleThickness or lead_x + block_size > randPoisonX and lead_x + block_size < randPoisonX + AppleThickness:
            if lead_y > randPoisonY and lead_y < randPoisonY + AppleThickness or lead_y + block_size > randPoisonY and lead_y + block_size < randPoisonY + AppleThickness:
                randPoisonX, randPoisonY = randPoisonGen()
                snakeLength += -1
                del snakeList[:-1]

        snake(block_size, snakeList)

        pygame.display.update()

        clock.tick(FPS)

    pygame.quit()
    quit()
#will redo collision

game_start()
gameLoop()
