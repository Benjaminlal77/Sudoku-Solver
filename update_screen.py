from sudoku_board import SudokuBoard
import pygame
from settings import Settings

def update_screen(screen, game_objects):
    screen.fill(Settings.bg_color)
    sudoku_board = game_objects['sudoku_board']
    
    sudoku_board.draw_board(screen)
    
    pygame.display.flip()
    