import pygame

class Text:
    def __init__(self, text, text_size, text_color, center_cords, background_color = None):
        self.text_color = text_color
        font = pygame.font.SysFont(None, text_size)
        
        self.text_image = font.render(str(text), True, text_color, background_color)
        self.text_rect = self.text_image.get_rect()
        self.text_rect.center = center_cords
    
    