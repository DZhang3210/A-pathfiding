import pygame
from pygame.locals import *


pygame.init()
display_width = 603
display_height = 700
dif = display_width//9
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Sudoku")
game_display.fill((194,194,214))
font = pygame.font.Font('freesansbold.ttf', 32)
font1 = pygame.font.Font('freesansbold.ttf', 16)
currentX = 0
currentY = 0
flag = (0,0)