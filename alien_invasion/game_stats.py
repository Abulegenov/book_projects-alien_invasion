class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self,ai_game):
        """Initialize statistics"""

        self.settings = ai_game.settings
        self.high_score = 0
        
        self.reset_stats()
    
    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.aliens_destroyed = 0
        self.level = 1
    
    def update_alien_destroyed(self,alien_num):
        self.aliens_destroyed += 1*(alien_num)+self.settings.alien_points

