import pygame
from settings import Settings

def update_screen(screen):
    screen.fill(Settings.bg_color)
    pygame.display.flip()
    