from settings import GameSettings, BoardBoxSettings
from text_box import FastSolveTextBox

def update_screen(screen, game_objects):
    def update_boxes():
        for box in sudoku_board.boxes:
            if box.selected:
                box.border_color = BoardBoxSettings.selected_border_color
            else:
                box.border_color = BoardBoxSettings.border_color          
    
    def draw_game_objects():
        sudoku_board.draw_board(screen)
        for strike in strikes:
            strike.draw_strike(screen)
        stop_watch.draw_time_clock(screen)
        
        randomize_button.button.draw_button(screen)
        solve_button.button.draw_button(screen)
    
    sudoku_board = game_objects['sudoku_board']
    strikes = game_objects['strikes']
    stop_watch = game_objects['stop_watch']
    randomize_button = game_objects['randomize_button']
    solve_button = game_objects['solve_button']
    
    update_boxes()
    stop_watch.update()
    
    screen.fill(GameSettings.bg_color)
    
    draw_game_objects()
    
def update_screen_while_solving(screen, game_objects):
    sudoku_board = game_objects['sudoku_board']
    screen.fill(GameSettings.bg_color)
    sudoku_board.draw_board(screen)
    FastSolveTextBox().write_text(screen)