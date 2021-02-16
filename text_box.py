from stats import GameStats
import pygame
from settings import GameSettings

class Text:
    def __init__(self, text, text_size, text_color, center_cords, background_color = None):
        self.text_color = text_color
        font = pygame.font.SysFont(None, text_size)
        
        self.text_image = font.render(str(text), True, text_color, background_color)
        self.text_rect = self.text_image.get_rect()
        self.text_rect.center = center_cords
    
class FastSolveTextBox:
    def __init__(self):
        self.text = Text('SPACE - Fast solve', 30, (0, 0, 0), (0, 0))
        self.text.text_rect.centerx = GameSettings.screen_width/2
        self.text.text_rect.centery = GameSettings.screen_height - 60
        
    def write_text(self,screen):
        screen.blit(self.text.text_image, self.text.text_rect)
    