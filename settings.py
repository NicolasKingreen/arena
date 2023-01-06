"""
Settings module contains Settings class.
"""
    

class Settings:

    """
    Settings class contains overall game settings.
    """

    def __init__(self):
        self.screen_size = 1280, 800
        self.screen_width, self.screen_height = self.screen_size
        self.screen_center = self.screen_width // 2, self.screen_height // 2
        self.screen_center_x, self.screen_center_y = self.screen_center
        self.pixel_scale = 10
        self.draw_fps = False