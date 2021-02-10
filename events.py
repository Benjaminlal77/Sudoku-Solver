from strikes import Strike
import pygame
import sys

def check_events(game_objects, stats):
    def check_mouse_click():
        for box in sudoku_board.boxes:
            box.selected = False
            if box.is_clicked():
                if not box.solved:
                    box.selected = True
    
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
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            check_mouse_click()
            
        if event.type == pygame.KEYDOWN:
            check_key_press()
            
def check_button_events():
    pass
