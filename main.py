import pygame
from settings import GameSettings
from stats import GameStats
from events import check_events
from update import update_screen

from sudoku_board import SudokuBoard
from pygame.sprite import Group

pygame.init()
screen = pygame.display.set_mode((GameSettings.screen_width, GameSettings.screen_height))
stats = GameStats()

sudoku_board = SudokuBoard()
strikes = Group()

game_objects = {
    'sudoku_board' : sudoku_board,
    'strikes' : strikes
}

while True:
    check_events(game_objects, stats)
    update_screen(screen, game_objects)
