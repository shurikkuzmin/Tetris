import pygame,sys
import pygame.transform
from pygame.locals import *
import numpy
import random

pygame.init()

clock = pygame.time.Clock()

tileWidth = 16
tileHeight = 16

rowSize = 24
columnSize = 10

WINDOWHEIGHT=tileHeight*rowSize
WINDOWWIDTH=tileWidth*columnSize

SURFACE = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))

pygame.display.set_caption('Tetris New Version')

AQUA      = (0, 255, 255)
BLUE      = (0, 0, 255)
BLACK     = (0, 0, 0)
# Fuchsia   = (255, 0,255)
# Gray      = (128, 128, 128)
GREEN     = (0, 205, 0)
# Maroon    = (128, 0, 0)
# Navy Blue = (0, 0, 128)
# Olive     = (128, 128, 0)
PURPLE    = (153, 50, 204)
#RED       = (255, 0, 0)
# Silver    = (192, 192, 192)
# Teal      = (0, 128, 128)
WHITE     = (255, 255, 255)
RED       = (255, 0, 0)
YELLOW    = (255, 255, 0)
ORANGE    = (255, 140, 0)

field = numpy.zeros((rowSize, columnSize),dtype=numpy.int)

def drawLevel():
    SURFACE.fill(BLACK)
    #Draw the level
    for row in range(rowSize):
        for column in range(columnSize):
            if field[row,column] == 1:
                pygame.draw.rect(SURFACE,YELLOW,(tileWidth*column,row*tileHeight,tileWidth,tileHeight))
            elif field[row,column] == 2:
                pygame.draw.rect(SURFACE,PURPLE,(tileWidth*column,row*tileHeight,tileWidth,tileHeight))
            elif field[row,column] == 3:
                pygame.draw.rect(SURFACE,AQUA,(tileWidth*column,row*tileHeight,tileWidth,tileHeight))
            elif field[row,column] == 4:
                pygame.draw.rect(SURFACE,BLUE,(tileWidth*column,row*tileHeight,tileWidth,tileHeight))
            elif field[row,column] == 5:
                pygame.draw.rect(SURFACE,ORANGE,(tileWidth*column,row*tileHeight,tileWidth,tileHeight))
            elif field[row,column] == 6:
                pygame.draw.rect(SURFACE,GREEN,(tileWidth*column,row*tileHeight,tileWidth,tileHeight))
            elif field[row,column] == 7:
                pygame.draw.rect(SURFACE,RED,(tileWidth*column,row*tileHeight,tileWidth,tileHeight))
            

figure=random.randint(1,7)

def createFigure(figure):
    startRow=1
    startColumn=int(columnSize/2)-1
    if figure == 1:
        field[startRow-1:startRow+1,startColumn-1:startColumn+1]=1
    elif figure == 2:
        field[startRow,startColumn-1:startColumn+2]=2
        field[startRow:startRow+2,startColumn]=2
    elif figure == 3:
        field[startRow,startColumn-1:startColumn+3]=3
    elif figure == 4:
        field[startRow-1:startRow+2,startColumn]=4
        field[startRow+1,startColumn:startColumn+2]=4
    elif figure == 5: 
        field[startRow-1:startRow+2,startColumn]=5
        field[startRow+1,startColumn-1:startColumn+1]=5
    elif figure == 6:
        field[startRow-1,startColumn:startColumn+2]=6
        field[startRow,startColumn-1:startColumn+1]=6
    elif figure == 7:
        field[startRow-1,startColumn-1:startColumn+1]=7
        field[startRow,startColumn:startColumn+2]=7
    
createFigure(7)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        #if event.type == KEYDOWN:
            #if event.key == K_RIGHT:
    drawLevel()
    clock.tick(60)            
    pygame.display.update()   
