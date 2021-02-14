from settings import GameSettings, BoardBoxSettings

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
    
    sudoku_board = game_objects['sudoku_board']
    strikes = game_objects['strikes']
    stop_watch = game_objects['stop_watch']
    
    update_boxes()
    stop_watch.update()
    
    screen.fill(GameSettings.bg_color)
    
    draw_game_objects()
    
def draw_buttons(screen, game_objects):
    randomize_button = game_objects['randomize_button']
    solve_button = game_objects['solve_button']
    
    randomize_button.button.draw_button(screen)
    solve_button.button.draw_button(screen)
    