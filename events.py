import pygame
import sys

from game_objects.strikes import Strike

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

    def check_for_board_click():
        sudoku_board = game_objects['sudoku_board']
        sudoku_board.check_for_box_select(stats)
        
    if stats.game_active:
        check_for_board_click()
        
    check_for_button_click()
    
def check_events(screen, game_objects, stats):
    def check_key_press():
        def check_if_correct_input(num):
            sudoku_board = game_objects['sudoku_board']
            strikes = game_objects['strikes']
            
            for box in sudoku_board.boxes:
                if box.selected:
                    if box.is_solved(num):
                        box.solved = True
                        box.selected = False
                        
                    else:
                        stats.strikes += 1
                        new_strike = Strike(stats.strikes)
                        strikes.add(new_strike)
                    
                    break
            
        if event.key == pygame.K_1:                        
            check_if_correct_input(1)
                        
        elif event.key == pygame.K_2:
            check_if_correct_input(2)
                    
        elif event.key == pygame.K_3:
            check_if_correct_input(3)
                    
        elif event.key == pygame.K_4:
            check_if_correct_input(4)
                    
        elif event.key == pygame.K_5:
            check_if_correct_input(5)
                    
        elif event.key == pygame.K_6:
            check_if_correct_input(6)
                    
        elif event.key == pygame.K_7:
            check_if_correct_input(7)
                    
        elif event.key == pygame.K_8:
            check_if_correct_input(8)
                    
        elif event.key == pygame.K_9:
            check_if_correct_input(9)
        
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
        def check_to_input_num(num):
            for box in sudoku_board.boxes:
                if box.selected:
                    if sudoku_board.num_is_valid(box, num):
                        box.correct_num = num
                        box.solved = True
                        box.prep_num()
                        break
        
        def remove_num():
            for box in sudoku_board.boxes:
                if box.selected:
                    box.correct_num = None
                    box.solved = False
                    break
            
        sudoku_board = game_objects['sudoku_board']
        if event.key == pygame.K_0:
            remove_num()
                        
        elif event.key == pygame.K_1:
            check_to_input_num(1)
                        
        elif event.key == pygame.K_2:
            check_to_input_num(2)
                    
        elif event.key == pygame.K_3:
            check_to_input_num(3)
                    
        elif event.key == pygame.K_4:
            check_to_input_num(4)
                    
        elif event.key == pygame.K_5:
            check_to_input_num(5)
                    
        elif event.key == pygame.K_6:
            check_to_input_num(6)
                    
        elif event.key == pygame.K_7:
            check_to_input_num(7)
                    
        elif event.key == pygame.K_8:
            check_to_input_num(8)
                    
        elif event.key == pygame.K_9:
            check_to_input_num(9)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            check_mouse_click(screen, game_objects, stats)
        
        elif event.type == pygame.KEYDOWN:
            check_key_press()
            