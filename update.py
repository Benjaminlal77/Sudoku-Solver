import pygame
from settings import GameSettings

clock = pygame.time.Clock()
def update_screen(screen, game_objects):
    screen.fill(GameSettings.bg_color)
    sudoku_board = game_objects['sudoku_board']
    
    sudoku_board.draw_board(screen)
    
    pygame.display.flip()
    clock.tick(GameSettings.FPS)
    