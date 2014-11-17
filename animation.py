import pygame, sys, time
from pygame.locals import *

# setup pygame
pygame.init()

# set up the window
WINDOWWIDTH = 500
WINDOWHEIGHT = 500
windowSurface = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Animation')

# set up direction variables
DOWNLEFT = 1
DOWNRIGHT = 3
UPLEFT = 7
UPRIGHT = 9
MOVESPEED = 4

# set up the colors
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
PINK = (255,20,147)

# set up the block data structure
b1 = {'rect':pygame.Rect(300,80,75,50), 'color':RED, 'dir':UPRIGHT}
b2 = {'rect':pygame.Rect(200,200,60,40), 'color':GREEN, 'dir':UPLEFT}
b3 = {'rect':pygame.Rect(300,350,80,80), 'color':BLUE, 'dir':DOWNLEFT}
b4 = {'rect':pygame.Rect(600,500,100,70), 'color':PINK, 'dir':DOWNRIGHT}
blocks = [b1,b2,b3,b4]

# create a background image
background_image = pygame.image.load("spaceBackground2.jpg").convert()

# run the game loop
while True:
    # check for the QUIT event
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    # draw the black background onto the surface
    windowSurface.blit(background_image, [0, 0])
#    windowSurface.fill(BLACK)
    
    for b in blocks:
        #move the block data structure
        if b['dir'] == DOWNLEFT:
            b['rect'].left -= MOVESPEED
            b['rect'].top += MOVESPEED
        if b['dir'] == DOWNRIGHT:
            b['rect'].left += MOVESPEED
            b['rect'].top += MOVESPEED
        if b['dir'] == UPLEFT:
            b['rect'].left -= MOVESPEED
            b['rect'].top -= MOVESPEED
        if b['dir'] == UPRIGHT:
            b['rect'].left += MOVESPEED
            b['rect'].top -= MOVESPEED
        # check if the block has moved out of the window
        if b['rect'].top < 0:
            # block has moved past the top
            if b['dir'] == UPLEFT:
                b['dir'] = DOWNLEFT
            if b['dir'] == UPRIGHT:
                b['dir'] = DOWNRIGHT
        if b['rect'].bottom > WINDOWHEIGHT:
            # block has moved past the bottom
            if b['dir'] == DOWNLEFT:
                b['dir'] = UPLEFT
            if b['dir'] == DOWNRIGHT:
                b['dir'] = UPRIGHT
        if b['rect'].left < 0:
            # block has moved past the left side
            if b['dir'] == DOWNLEFT:
                b['dir'] = DOWNRIGHT
            if b['dir'] == UPLEFT:
                b['dir'] = UPRIGHT
        if b['rect'].right > WINDOWWIDTH:
            # block has moved past the right side
            if b['dir'] == DOWNRIGHT:
                b['dir'] = DOWNLEFT
            if b['dir'] == UPRIGHT:
                b['dir'] = UPLEFT
        
        # draw the bock onto the surface
        pygame.draw.rect(windowSurface, b['color'], b['rect'])
    # draw the window onto the screen
    pygame.display.update()
    time.sleep(0.02)

