import pygame
from settings import GameSettings
from text_box import Text

def write_result(screen, result):
    
    # Define text properties
    
    text = result
    text_size = 100
    
    if result == 'You win!':
        text_color = (0, 255, 0)
    elif result == 'You lose!':
        text_color = (255, 0, 0)
        
    text_cords = GameSettings.screen_center
    text_bg = (0, 0, 0)
    
    # Write text
    
    result_text = Text(text, text_size, text_color, text_cords, text_bg)
    
    screen.blit(result_text.text_image, result_text.text_rect)
    pygame.display.flip()
    
def check_if_game_over(screen, game_objects, stats):
    sudoku_board = game_objects['sudoku_board']
    strikes = game_objects['strikes']
    
    sudoku_board.check_if_solved()
    
    if sudoku_board.solved:
        stats.game_active = False
        if not stats.end_by_solve_button:
            write_result(screen, 'You win!')
        else:
            stats.end_by_solve_button = False
        
    elif len(strikes) == GameSettings.max_strikes:
        stats.game_active = False
        write_result(screen, 'You lose!')
