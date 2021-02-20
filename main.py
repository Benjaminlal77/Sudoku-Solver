import pygame
from game_functions.settings import GameSettings
from game_functions.stats import GameStats
from game_functions.events import check_events, check_events_while_creating_board
from game_functions.update import update_screen, update_screen_while_creating_board
from game_functions.game_over import check_if_game_over

from game_objects.sudoku_board import SudokuBoard
from pygame.sprite import Group
from game_objects.stop_watch import StopWatch
from game_objects.buttons import RandomizeButton, SolveButton, CreateBoardButton

pygame.init()
screen = pygame.display.set_mode((GameSettings.screen_width, GameSettings.screen_height))

pygame.display.set_caption('Sudoku Solver')
icon_image = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon_image)

stats = GameStats()

# Define game objects

sudoku_board = SudokuBoard()
strikes = Group()
stop_watch = StopWatch()

# Define buttons

randomize_button = RandomizeButton()
solve_button = SolveButton()
create_board_button = CreateBoardButton()

game_objects = {
    'sudoku_board' : sudoku_board,
    'strikes' : strikes,
    'stop_watch' : stop_watch,
    'randomize_button' : randomize_button,
    'solve_button' : solve_button,
    'create_board_button' : create_board_button
}

while True:
    if stats.creating_board:
        check_events_while_creating_board(screen, game_objects, stats)
        update_screen_while_creating_board(screen, game_objects, stats)
        
        pygame.time.Clock().tick(GameSettings.FPS)
        
    elif stats.game_active:
        check_events(screen, game_objects, stats)
        update_screen(screen, game_objects, stats)
        
        check_if_game_over(screen, game_objects, stats)                               
        
        pygame.time.Clock().tick(GameSettings.FPS)

    elif not stats.game_active:
        check_events(screen, game_objects, stats)            
        
        pygame.time.Clock().tick(GameSettings.FPS)
