from strikes import Strike
import pygame
import sys

def check_mouse_click(screen, game_objects, stats):
    def check_for_button_click():
        randomize_button = game_objects['randomize_button']
        solve_button = game_objects['solve_button']
        create_board_button = game_objects['create_board_button']
        
        if randomize_button.button.is_clicked():
            randomize_button.randomize(game_objects, stats)
        elif solve_button.button.is_clicked():
            solve_button.solve(screen, game_objects, stats)
        elif create_board_button.button.is_clicked():
            create_board_button.create_board(game_objects,stats)

    def check_for_box_select():
        sudoku_board = game_objects['sudoku_board']
        for box in sudoku_board.boxes:
            box.selected = False
            if box.is_clicked():
                if not box.solved:
                    box.selected = True
                elif stats.creating_board:
                    box.selected = True
        
    if stats.game_active:
        check_for_box_select()
    check_for_button_click()
    
def check_events(screen, game_objects, stats):
    def check_key_press():
        sudoku_board = game_objects['sudoku_board']
        strikes = game_objects['strikes']
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
                    
                    break                        
                        
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

                    break
                    
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

                    break
                    
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

                    break
                    
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

                    break
                    
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

                    break
                    
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

                    break
                    
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

                    break
                    
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

                    break
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()  
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            check_mouse_click(screen, game_objects, stats)
            
        elif stats.game_active:
            if event.type == pygame.KEYDOWN:
                check_key_press()

def check_events_while_solving(stats):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                stats.fast_solve = True
                
def check_events_while_creating_board(screen, game_objects, stats):
    def check_key_press():
        sudoku_board = game_objects['sudoku_board']
        if event.key == pygame.K_0:
            for box in sudoku_board.boxes:
                if box.selected:
                    box.correct_num = None
                    box.solved = False
                    break
        
        if event.key == pygame.K_1:
            for box in sudoku_board.boxes:
                if box.selected:
                    if sudoku_board.num_is_valid(box, 1):
                        box.correct_num = 1
                        box.solved = True
                        box.prep_num()
                        break
                        
        elif event.key == pygame.K_2:
            for box in sudoku_board.boxes:
                if box.selected:
                    if sudoku_board.num_is_valid(box, 2):
                        box.correct_num = 2
                        box.solved = True
                        box.prep_num()
                        break
                    
        elif event.key == pygame.K_3:
            for box in sudoku_board.boxes:
                if box.selected:
                    if sudoku_board.num_is_valid(box, 3):
                        box.correct_num = 3
                        box.solved = True
                        box.prep_num()
                        break
                    
        elif event.key == pygame.K_4:
            for box in sudoku_board.boxes:
                if box.selected:
                    if sudoku_board.num_is_valid(box, 4):
                        box.correct_num = 4
                        box.solved = True
                        box.prep_num()
                        break
                    
        elif event.key == pygame.K_5:
            for box in sudoku_board.boxes:
                if box.selected:
                    if sudoku_board.num_is_valid(box, 5):
                        box.correct_num = 5
                        box.solved = True
                        box.prep_num()
                        break
                    
        elif event.key == pygame.K_6:
            for box in sudoku_board.boxes:
                if box.selected:
                    if sudoku_board.num_is_valid(box, 6):
                        box.correct_num = 6
                        box.solved = True
                        box.prep_num()
                        break
                    
        elif event.key == pygame.K_7:
            for box in sudoku_board.boxes:
                if box.selected:
                    if sudoku_board.num_is_valid(box, 7):
                        box.correct_num = 7
                        box.solved = True
                        box.prep_num()
                        break
                    
        elif event.key == pygame.K_8:
            for box in sudoku_board.boxes:
                if box.selected:
                    if sudoku_board.num_is_valid(box, 8):
                        box.correct_num = 8
                        box.solved = True
                        box.prep_num()
                        break
                    
        elif event.key == pygame.K_9:
            for box in sudoku_board.boxes:
                if box.selected:
                    if sudoku_board.num_is_valid(box, 9):
                        box.correct_num = 9
                        box.solved = True
                        box.prep_num()
                        break
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            check_mouse_click(screen, game_objects, stats)
        
        elif event.type == pygame.KEYDOWN:
            check_key_press()