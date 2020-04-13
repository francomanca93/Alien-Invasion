import pygame


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
        self.screen_height = 700
        self.bg_color = (170, 180, 170)  # Set the background color. Seteamos el color de fondo

        # Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3  # How many ship do I have when I'm playing?

        # Bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (50, 50, 50)
        self.bullet_allowed = 5  # Only we can stored 3 bullet

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 5
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

