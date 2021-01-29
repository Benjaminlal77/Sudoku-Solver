import pygame
from settings import GameSettings
from events import check_events
from update import update_screen

from sudoku_board import SudokuBoard

pygame.init()
screen = pygame.display.set_mode((GameSettings.screen_width, GameSettings.screen_height))

sudoku_board = SudokuBoard()

game_objects = {
    'sudoku_board' : sudoku_board
}

while True:
    check_events()
    update_screen(screen, game_objects)
