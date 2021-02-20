import pygame
from pygame.sprite import Sprite
from settings import BoardSettings

class Strike(Sprite):
    def __init__(self, strike_num):
        
        # Define properties
        
        super().__init__()
        self.strike_num = strike_num
        self.margin = 10
        self.size = 50
        self.width = self.height = self.size
        
        # Define cords
        
        self.rect = pygame.Rect(0, 0, 0, 0)
        self.rect.x = ((self.strike_num * self.size) - self.size) + self.margin
        self.rect.y = BoardSettings.size + self.margin
        
        self.image = pygame.image.load('images/strike.png')
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        
    def draw_strike(self, screen):
        screen.blit(self.image, self.rect)
    