import pygame
from pygame.time import Clock
from settings import GameSettings
from stats import GameStats
from events import check_events, check_button_events
from update import update_screen
from game_over import check_if_game_over

from sudoku_board import SudokuBoard
from pygame.sprite import Group
from stop_watch import StopWatch

pygame.init()
screen = pygame.display.set_mode((GameSettings.screen_width, GameSettings.screen_height))
stats = GameStats()

clock = pygame.time.Clock()

sudoku_board = SudokuBoard()
strikes = Group()
stop_watch = StopWatch()

game_objects = {
    'sudoku_board' : sudoku_board,
    'strikes' : strikes,
    'stop_watch': stop_watch
}

while True:
    if not stats.game_active:
        check_button_events()
        break
        
    elif stats.game_active:
        check_events(game_objects, stats)
        update_screen(screen, game_objects)
        check_if_game_over(screen, game_objects, stats)
        clock.tick(GameSettings.FPS)
