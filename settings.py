class Settings:
    """A class to store all settings for alien invasion"""

    def __init__(self):
        """Initialize the game's settings."""
        #screen settings
        self.screen_width = 600
        self.screen_height = 400
        self.bg_color = (230,230,230)

        #Ship settings
        self.ship_speed = 1.5
