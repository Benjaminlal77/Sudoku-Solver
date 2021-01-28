import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((600, 550))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()  
            
    pygame.display.flip()
