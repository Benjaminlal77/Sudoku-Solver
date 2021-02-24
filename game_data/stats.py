class GameStats:
    def __init__(self):
        self.game_active = True
        self.strikes = 0
        
        self.fast_solve = False
        self.end_by_solve_button = False
    
        self.creating_board = False
    
    def reset(self):
        self.game_active = True
        self.strikes = 0
        
        self.fast_solve = False
        self.end_by_solve_button = False
        
        self.creating_board = False
        