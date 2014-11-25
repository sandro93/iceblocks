#!/bin/env python

import pygame, sys
from pygame.locals import *

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

WINDOW_POS_X = 0
WINDOW_POS_Y = 0

# set up pygame
pygame.init()

# set up the window
windowSurface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT),
        WINDOW_POS_X, WINDOW_POS_Y)

pygame.display.set_caption('IceBlocks')


