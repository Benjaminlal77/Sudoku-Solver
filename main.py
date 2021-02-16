import pygame
from settings import GameSettings
from stats import GameStats
from events import check_events
from update import update_screen
from game_over import check_if_game_over

from sudoku_board import SudokuBoard
from pygame.sprite import Group
from stop_watch import StopWatch
from buttons import RandomizeButton, SolveButton

pygame.init()
screen = pygame.display.set_mode((GameSettings.screen_width, GameSettings.screen_height))
stats = GameStats()

sudoku_board = SudokuBoard()
strikes = Group()
stop_watch = StopWatch()

randomize_button = RandomizeButton()
solve_button = SolveButton()

game_objects = {
    'sudoku_board' : sudoku_board,
    'strikes' : strikes,
    'stop_watch' : stop_watch,
    'randomize_button' : randomize_button,
    'solve_button' : solve_button
}

while True:
    if not stats.game_active:
        check_events(screen, game_objects, stats)
        pygame.time.Clock().tick(GameSettings.FPS)
        
    elif stats.game_active:
        check_events(screen, game_objects, stats)
        
        update_screen(screen, game_objects)

        check_if_game_over(screen, game_objects, stats)
        pygame.display.flip()
        pygame.time.Clock().tick(GameSettings.FPS)
