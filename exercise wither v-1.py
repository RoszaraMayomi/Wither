import pygame
import time
import random

#Wither- adding a block that shortens the snake. if 0 you die

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

clock = pygame.time.Clock()

block_size = 10
FPS = 30

font = pygame.font.SysFont(None, 25)
#functions
def snake(block_size, snakeList):
    for XnY in snakeList:
        pygame.draw.rect(gameDisplay, green, [XnY[0], XnY[1], block_size, block_size])

def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color, black)
    gameDisplay.blit(screen_text, [display_width / 2, display_height / 2])
#gameLoop
def gameLoop():
    #main variables
    gameExit = False
    gameOver = False

    lead_x = display_width / 2
    lead_y = display_height / 2

    lead_x_change = 0
    lead_y_change = 0

    snakeList = []
    snakeLength = 1

    randAppleX = round(random.randrange(0, display_width - block_size)/10.0)*10.0
    randAppleY = round(random.randrange(0, display_height - block_size)/10.0)*10.0

    randPoisonX = round(random.randrange(0, display_width - block_size)/10.0)*10.0
    randPoisonY = round(random.randrange(0, display_height - block_size)/10.0)*10.0
    
#main gameLoop
    while not gameExit:
    #game Over screen
        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen('Game Over; Press C to play again or Q to Quit!' ,red)
            pygame.display.update()


            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False

                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                if event.key == pygame.K_RIGHT:
                    lead_x_change = block_size 
                    lead_y_change = 0
                if event.key == pygame.K_UP:
                    lead_y_change = -block_size 
                    lead_x_change = 0
                if event.key == pygame.K_DOWN:
                    lead_y_change = block_size 
                    lead_x_change = 0

        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            gameOver = True

        lead_x += lead_x_change
        lead_y += lead_y_change
       
        gameDisplay.fill(white)
        pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, block_size, block_size])
        pygame.draw.rect(gameDisplay, black, [randPoisonX, randPoisonY, block_size, block_size])
        
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]
        if snakeLength <= 0:
            gameOver = True

#less jank but working fine 
        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True

        if lead_x == randAppleX and lead_y == randAppleY:
            randAppleX = round(random.randrange(0, display_width - block_size)/10.0)*10.0
            randAppleY = round(random.randrange(0, display_height - block_size)/10.0)*10.0
            snakeLength += 1

        if lead_x == randPoisonX and lead_y == randPoisonY:
            randPoisonX = round(random.randrange(0, display_width - block_size)/10.0)*10.0
            randPoisonY = round(random.randrange(0, display_height - block_size)/10.0)*10.0
            snakeLength += -1
            del snakeList[:-1]

        snake(block_size, snakeList)

        pygame.display.update()     

        clock.tick(FPS)

    pygame.quit()
    quit()

gameDisplay.fill(black)
message_to_screen("Black is poison Red is food Life is about attitude", green)
pygame.display.update()
time.sleep(2)
message_to_screen('Press a to go please...', white)
pygame.display.update()
gameExit2 = False
while not gameExit2:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                gameLoop()
