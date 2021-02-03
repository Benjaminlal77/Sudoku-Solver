import pygame
import sys

def check_events(game_objects):
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
                    box.check_if_solved(1)
                        
        elif event.key == pygame.K_2:
            for box in sudoku_board.boxes:
                if box.selected:
                    box.check_if_solved(2)
                    
        elif event.key == pygame.K_3:
            for box in sudoku_board.boxes:
                if box.selected:
                    box.check_if_solved(3)
                    
        elif event.key == pygame.K_4:
            for box in sudoku_board.boxes:
                if box.selected:
                    box.check_if_solved(4)
                    
        elif event.key == pygame.K_5:
            for box in sudoku_board.boxes:
                if box.selected:
                    box.check_if_solved(5)
                    
        elif event.key == pygame.K_6:
            for box in sudoku_board.boxes:
                if box.selected:
                    box.check_if_solved(6)
                    
        elif event.key == pygame.K_7:
            for box in sudoku_board.boxes:
                if box.selected:
                    box.check_if_solved(7)
                    
        elif event.key == pygame.K_8:
            for box in sudoku_board.boxes:
                if box.selected:
                    box.check_if_solved(8)
                    
        elif event.key == pygame.K_9:
            for box in sudoku_board.boxes:
                if box.selected:
                    box.check_if_solved(9)
        
    sudoku_board = game_objects['sudoku_board']
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()  
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            check_mouse_click()
            
        if event.type == pygame.KEYDOWN:
            check_key_press()
            