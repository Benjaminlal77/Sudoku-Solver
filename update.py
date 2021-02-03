import pygame
from settings import GameSettings, BoardBoxSettings

clock = pygame.time.Clock()
def update_screen(screen, game_objects):
    def update_boxes():
        for box in sudoku_board.boxes:
            if box.selected:
                box.border_color = BoardBoxSettings.selected_border_color
            else:
                box.border_color = BoardBoxSettings.border_color
    
    sudoku_board = game_objects['sudoku_board']
    
    update_boxes()
    
    screen.fill(GameSettings.bg_color)
    
    sudoku_board.draw_board(screen)
    
    pygame.display.flip()
    clock.tick(GameSettings.FPS)
    