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
def putFigure(figure,figureRow,figureColumn,check=True):
    
    if figure == 1:
        if figureRow == rowSize:
            return False
        if numpy.sum(field[figureRow-1:figureRow+1,figureColumn-1:figureColumn+1]) > 0:
            return False
        if figureColumn-1 < 0:
            return False
        if figureColumn > columnSize - 1:
            return False
        if check == False:
            field[figureRow-1:figureRow+1,figureColumn-1:figureColumn+1]=1
    elif figure == 2:
        if figureRow+1 == rowSize:
            return False
        if figureColumn-1 < 0:
            return False
        if figureColumn+1 > columnSize - 1:
            return False
        if numpy.sum(field[figureRow,figureColumn-1:figureColumn+2]) > 0:
            return False
        if numpy.sum(field[figureRow:figureRow+2,figureColumn]) > 0:
            return False
        if check == False:
            field[figureRow,figureColumn-1:figureColumn+2]=2
            field[figureRow:figureRow+2,figureColumn]=2
    elif figure == 3:
        if figureRow == rowSize:
            return False
        if figureColumn-1 < 0:
            return False
        if figureColumn+2 > columnSize - 1:
            return False
        if numpy.sum(field[figureRow,figureColumn-1:figureColumn+3]) > 0:
            return False
        if check == False:
            field[figureRow,figureColumn-1:figureColumn+3]=3
    elif figure == 4:
        if figureRow+1 == rowSize:
            return False
        if figureColumn < 0:
            return False
        if figureColumn+1 > columnSize-1:
            return False
        if numpy.sum(field[figureRow-1:figureRow+2,figureColumn]) > 0:
            return False
        if numpy.sum(field[figureRow+1,figureColumn:figureColumn+2]) > 0:
            return False
        if check == False:
            field[figureRow-1:figureRow+2,figureColumn]=4
            field[figureRow+1,figureColumn:figureColumn+2]=4
    elif figure == 5: 
        if figureRow+1 == rowSize:
            return False
        if figureColumn-1 < 0:
            return False
        if figureColumn > columnSize - 1:
            return False
        if numpy.sum(field[figureRow-1:figureRow+2,figureColumn]) > 0:
            return False
        if numpy.sum(field[figureRow+1,figureColumn-1:figureColumn+1]) > 0:
            return False
        if check == False:
            field[figureRow-1:figureRow+2,figureColumn]=5
            field[figureRow+1,figureColumn-1:figureColumn+1]=5
    elif figure == 6:
        if figureRow == rowSize:
            return False
        if figureColumn-1 < 0:
            return False
        if figureColumn+1 > columnSize -1:
            return False
        if numpy.sum(field[figureRow-1,figureColumn:figureColumn+2]) > 0:
            return False
        if numpy.sum(field[figureRow,figureColumn-1:figureColumn+1]) > 0:
            return False
        if check == False:
            field[figureRow-1,figureColumn:figureColumn+2]=6
            field[figureRow,figureColumn-1:figureColumn+1]=6
    elif figure == 7:
        if figureRow == rowSize:
            return False
        if figureColumn-1 < 0:
            return False
        if figureColumn+1 > columnSize - 1:
            return False
        if numpy.sum(field[figureRow-1,figureColumn-1:figureColumn+1]) > 0:
            return False
        if numpy.sum(field[figureRow,figureColumn:figureColumn+2]) > 0:
            return False
        if check == False:
            field[figureRow-1,figureColumn-1:figureColumn+1]=7
            field[figureRow,figureColumn:figureColumn+2]=7
    return True

def removeFigure(figure,figureRow,figureColumn):
    
    if figure == 1:
        field[figureRow-1:figureRow+1,figureColumn-1:figureColumn+1]=0
    elif figure == 2:
        field[figureRow,figureColumn-1:figureColumn+2]=0
        field[figureRow:figureRow+2,figureColumn]=0
    elif figure == 3:
        field[figureRow,figureColumn-1:figureColumn+3]=0
    elif figure == 4:
        field[figureRow-1:figureRow+2,figureColumn]=0
        field[figureRow+1,figureColumn:figureColumn+2]=0
    elif figure == 5: 
        field[figureRow-1:figureRow+2,figureColumn]=0
        field[figureRow+1,figureColumn-1:figureColumn+1]=0
    elif figure == 6:
        field[figureRow-1,figureColumn:figureColumn+2]=0
        field[figureRow,figureColumn-1:figureColumn+1]=0
    elif figure == 7:
        field[figureRow-1,figureColumn-1:figureColumn+1]=0
        field[figureRow,figureColumn:figureColumn+2]=0
        
def EndGame():
    basicFont = pygame.font.SysFont(None, 30)
    text = basicFont.render('Game Over!', True, RED)
    textRect = text.get_rect()
    textRect.centerx = WINDOWWIDTH/2
    textRect.centery = WINDOWHEIGHT/2
    SURFACE.blit(text,textRect)
    pygame.display.update()
    
gameOver = False
figureRow=1
figureColumn=int(columnSize/2)-1
putFigure(figure,figureRow,figureColumn)

SPEED = 60
downSpeed = SPEED/5
counter = 0

while True:
    removeFigure(figure, figureRow, figureColumn)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if gameOver == True:
            continue
        if event.type == KEYDOWN:
            figureNewRow = figureRow
            figureNewColumn = figureColumn
            if event.key == K_RIGHT:
                figureNewColumn = figureColumn+1
            if event.key == K_LEFT:
                figureNewColumn = figureColumn-1
            if event.key == K_DOWN:
                figureNewRow = figureRow+1
            if putFigure(figure,figureNewRow,figureNewColumn) == True:
                figureRow = figureNewRow
                figureColumn = figureNewColumn
    if gameOver == True:
        continue
    
    counter = counter + 1
    if counter % downSpeed == 0:
        if putFigure(figure,figureRow+1,figureColumn) == True:
            figureRow = figureRow+1
        else:
            putFigure(figure,figureRow,figureColumn,False)
            figure=random.randint(1,7)
            figureRow=1
            figureColumn=int(columnSize/2)-1
            if putFigure(figure,figureRow, figureColumn) == False:
                EndGame()
                gameOver = True
                continue
            
    putFigure(figure,figureRow,figureColumn,False)
        
        
    drawLevel()
    clock.tick(SPEED)            
    pygame.display.update()   