import pygame

from settings import GameSettings, ButtonSettings
from text_class import Text
    
class Button:
    def __init__(self, button_num, text):
        self.image = pygame.image.load('images/button.png')
        self.image = pygame.transform.scale(self.image, ButtonSettings.size)
        
        self.rect = self.image.get_rect()
        self.rect.x = ButtonSettings.width * button_num + ButtonSettings.margin * button_num
        self.rect.x -= ButtonSettings.width
        self.rect.y = GameSettings.screen_height - ButtonSettings.margin
        self.rect.y -= ButtonSettings.height
        self.rect.w = ButtonSettings.width
        self.rect.h = ButtonSettings.height
        
        self.button_text = Text(text, 25, (0,0,0), (self.rect.center))
    
    def draw_button(self, screen):
        screen.blit(self.image, self.rect)
        screen.blit(self.button_text.text_image, self.button_text.text_rect)
    
    def is_clicked(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_x, mouse_y):
            return True
        else:
            return False
        
class RandomizeButton:
    def __init__(self):
        self.button = Button(1, 'Randomize')
    
    def randomize(self, game_objects, stats):
        sudoku_board = game_objects['sudoku_board']
        strikes = game_objects['strikes']
        stop_watch = game_objects['stop_watch']

        strikes.empty()
        stats.strikes = 0
        stop_watch.reset()
        sudoku_board.reset()
        sudoku_board.randomize_board()
        for box in sudoku_board.boxes:
            box.prep_num()
        stats.game_active = True
        