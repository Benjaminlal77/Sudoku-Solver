class GameStats:
    def __init__(self):
        self.strikes = 0
        self.game_active = True
        
    def reset_stats(self):
        self.strikes = 0
    