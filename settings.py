class Settings:
    """
    A class to store all settings for Alien Invasion.
    Una clase para guardar todas las configuracion para Alien Invasion
    """

    def __init__(self):
        """
        Constructor of Settings
        Initialize the game's settings.
        """
        # Attibutes of the screen settings
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (250, 250, 250)  # Set the background color. Seteamos el color de fondo

        # Ship settings
        self.ship_speed = 1.5
