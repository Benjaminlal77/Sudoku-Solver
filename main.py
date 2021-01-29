import pygame
from settings import Settings
from check_events import check_events
from update_screen import update_screen

from sudoku_board import SudokuBoard

pygame.init()
screen = pygame.display.set_mode((Settings.screen_width, Settings.screen_height))

sudoku_board = SudokuBoard()

game_objects = {
    'sudoku_board' : sudoku_board
}

while True:
    check_events()
    update_screen(screen, game_objects)
