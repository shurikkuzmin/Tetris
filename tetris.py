import pygame,sys
import pygame.transform
from pygame.locals import *
import numpy

pygame.init()

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

field[12,5]=1
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        #if event.type == KEYDOWN:
            #if event.key == K_RIGHT:
    drawLevel()
                
    pygame.display.update()   
