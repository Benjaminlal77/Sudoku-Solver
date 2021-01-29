import pygame 
from settings import Settings
        
class BoardOutline:
    def __init__(self):
        self.rect = pygame.Rect(0, 0, 0, 0)
        self.rect.width = Settings.board_width
        self.rect.height = Settings.board_height
        
        self.color = Settings.board_outline_color
        
    def draw_outline(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        
class SudokuBoard:
    num_of_large_boxes = 9
    def __init__(self):
        self.outline = BoardOutline()
        
    def draw_board(self, screen):
        self.outline.draw_outline(screen)
    