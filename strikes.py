import pygame
from pygame.sprite import Sprite
from settings import BoardSettings, StrikeSettings

class Strike(Sprite):
    def __init__(self, strike_num):
        super().__init__()
        self.strike_num = strike_num
        self.margin = StrikeSettings.margin
        
        self.rect = pygame.Rect(0, 0, 0, 0)
        self.rect.x = ((self.strike_num * StrikeSettings.size) - StrikeSettings.size) + self.margin
        self.rect.y = BoardSettings.size + self.margin
        
        self.image = pygame.image.load('images/strike.png')
        self.image = pygame.transform.scale(self.image, (StrikeSettings.width, StrikeSettings.height))
        
    def draw_strike(self, screen):
        screen.blit(self.image, self.rect)
    