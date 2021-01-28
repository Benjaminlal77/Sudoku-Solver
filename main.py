import sys
import pygame
from settings import Settings

pygame.init()
screen = pygame.display.set_mode((Settings.screen_width, Settings.screen_height))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()  
            
    pygame.display.flip()
