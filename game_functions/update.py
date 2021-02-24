import pygame
from game_data.settings import GameSettings, BoardBoxSettings
from game_objects.text_box import CreateBoardControlsTextBox, FastSolveTextBox, ImpossibleBoardTextBox

def update_screen(screen, game_objects, stats):         
    def draw_game_objects():
        strikes = game_objects['strikes']
        randomize_button = game_objects['randomize_button']
        solve_button = game_objects['solve_button']
        create_board_button = game_objects['create_board_button']
        
        sudoku_board.draw_board(screen)
        for strike in strikes:
            strike.draw_strike(screen)
        stop_watch.draw_stop_watch(screen)
        
        # Draw buttons
        
        randomize_button.button.draw_button(screen)
        solve_button.button.draw_button(screen)
        create_board_button.button.draw_button(screen)
    
    sudoku_board = game_objects['sudoku_board']
    stop_watch = game_objects['stop_watch']
    
    update_boxes(game_objects)
    if not stats.end_by_solve_button:
        stop_watch.update()
    
    screen.fill(GameSettings.bg_color)
    
    draw_game_objects()
    
    pygame.display.flip()
    
def update_boxes(game_objects):
    sudoku_board = game_objects['sudoku_board']
    
    for box in sudoku_board.boxes:
        if box.selected:
            box.border_color = BoardBoxSettings.selected_border_color
        else:
            box.border_color = BoardBoxSettings.border_color 

def update_screen_while_solving(screen, game_objects):
    sudoku_board = game_objects['sudoku_board']

    screen.fill(GameSettings.bg_color)

    sudoku_board.draw_board(screen)
    FastSolveTextBox().write_text(screen)
    
    pygame.display.flip()
    
def update_screen_while_creating_board(screen, game_objects, stats):
    def draw_game_objects():
        sudoku_board = game_objects['sudoku_board']
        sudoku_board.draw_board(screen)
        
        if stats.end_by_solve_button:
            if not sudoku_board.solved:
                ImpossibleBoardTextBox().write_text(screen)

        else:
            CreateBoardControlsTextBox().write_text(screen)
        
        randomize_button = game_objects['randomize_button']
        solve_button = game_objects['solve_button']
        create_board_button = game_objects['create_board_button']
        
        randomize_button.button.draw_button(screen)
        solve_button.button.draw_button(screen)
        create_board_button.button.draw_button(screen)
    
    update_boxes(game_objects)
    
    screen.fill(GameSettings.bg_color)
    
    draw_game_objects()
    pygame.display.flip()
    