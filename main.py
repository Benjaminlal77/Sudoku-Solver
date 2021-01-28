import pygame
from settings import Settings
from check_events import check_events

pygame.init()
screen = pygame.display.set_mode((Settings.screen_width, Settings.screen_height))

while True:
    check_events()
    pygame.display.flip()
