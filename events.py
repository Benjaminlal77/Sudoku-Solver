from strikes import Strike
import pygame
import sys

def check_mouse_click(screen, game_objects, stats):
    def check_for_button_click():
        randomize_button = game_objects['randomize_button']
        solve_button = game_objects['solve_button']
        
        if randomize_button.button.is_clicked():
            randomize_button.randomize(game_objects, stats)
        elif solve_button.button.is_clicked():
            solve_button.solve(screen, game_objects, stats)

    def check_for_box_select():
        sudoku_board = game_objects['sudoku_board']
        for box in sudoku_board.boxes:
            box.selected = False
            if box.is_clicked():
                if not box.solved:
                    box.selected = True
        
    if stats.game_active:
        check_for_box_select()
    check_for_button_click()
    
def check_events(screen, game_objects, stats):
    def check_key_press():
        if event.key == pygame.K_1:
            for box in sudoku_board.boxes:
                if box.selected:
                    if box.is_solved(1):
                        box.solved = True
                        box.selected = False
                        
                    else:
                        stats.strikes += 1
                        new_strike = Strike(stats.strikes)
                        strikes.add(new_strike)
                        
        elif event.key == pygame.K_2:
            for box in sudoku_board.boxes:
                if box.selected:
                    if box.is_solved(2):
                        box.solved = True
                        box.selected = False
                        
                    else:
                        stats.strikes += 1
                        new_strike = Strike(stats.strikes)
                        strikes.add(new_strike)
                    
        elif event.key == pygame.K_3:
            for box in sudoku_board.boxes:
                if box.selected:
                    if box.is_solved(3):
                        box.solved = True
                        box.selected = False
                        
                    else:
                        stats.strikes += 1
                        new_strike = Strike(stats.strikes)
                        strikes.add(new_strike)
                    
        elif event.key == pygame.K_4:
            for box in sudoku_board.boxes:
                if box.selected:
                    if box.is_solved(4):
                        box.solved = True
                        box.selected = False
                        
                    else:
                        stats.strikes += 1
                        new_strike = Strike(stats.strikes)
                        strikes.add(new_strike)
                    
        elif event.key == pygame.K_5:
            for box in sudoku_board.boxes:
                if box.selected:
                    if box.is_solved(5):
                        box.solved = True
                        box.selected = False
                        
                    else:
                        stats.strikes += 1
                        new_strike = Strike(stats.strikes)
                        strikes.add(new_strike)
                    
        elif event.key == pygame.K_6:
            for box in sudoku_board.boxes:
                if box.selected:
                    if box.is_solved(6):
                        box.solved = True
                        box.selected = False
                        
                    else:
                        stats.strikes += 1
                        new_strike = Strike(stats.strikes)
                        strikes.add(new_strike)
                    
        elif event.key == pygame.K_7:
            for box in sudoku_board.boxes:
                if box.selected:
                    if box.is_solved(7):
                        box.solved = True
                        box.selected = False
                        
                    else:
                        stats.strikes += 1
                        new_strike = Strike(stats.strikes)
                        strikes.add(new_strike)
                    
        elif event.key == pygame.K_8:
            for box in sudoku_board.boxes:
                if box.selected:
                    if box.is_solved(8):
                        box.solved = True
                        box.selected = False
                        
                    else:
                        stats.strikes += 1
                        new_strike = Strike(stats.strikes)
                        strikes.add(new_strike)
                    
        elif event.key == pygame.K_9:
            for box in sudoku_board.boxes:
                if box.selected:
                    if box.is_solved(9):
                        box.solved = True
                        box.selected = False
                        
                    else:
                        stats.strikes += 1
                        new_strike = Strike(stats.strikes)
                        strikes.add(new_strike)
        
    sudoku_board = game_objects['sudoku_board']
    strikes = game_objects['strikes']
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()  
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            check_mouse_click(screen, game_objects, stats)
            
        elif stats.game_active:
            if event.type == pygame.KEYDOWN:
                check_key_press()
