import sys
import pygame
from settings import Settings  # Del archivo setting.py importamos la clase Settings
from ship import Ship  # Del archivo ship.py importamos la clase Ship


class AlienInvasion:
    """Overall class to manage game assets and behavior
    Clase principal para manejar las acciones y comportamiento del juego"""

    def __init__(self):
        """
        Constructor of AlienInvasion
        Initialize the game, and create game resources.
        Inicializamos el juego y creamos los recursos del juego
        """
        pygame.init()  # Inicializes the background setting that Pygame needs to work properly
        # Attributes
        self.settings = Settings()  # Definimos un atributo setting que tenga tdo lo que tiene Setting

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # we assign an object named surface (the display window) to the attribute self.screen.
        # We call this function to create a display window
        # In this screen we well draw all the game's graphical elements
        # (self.settings.screen_width, self.settings.screen_height) -> Tuple that define window size
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)  # Instace of the Ship class.
        # The self argument give to Ship access to the game's resources, like a screen object

    def run_game(self):
        """
        Start the main loop for the game
        Empieza el ciclo inicial para el juego
        :return:
        """
        # The while loop contains an event loop and code that manages screen updates
        # event = pressing a key or moving the mouse
        while True:
            # Watch for keyyboard and mouse events.
            # Muestra los eventos del teclado y el mouse
            # Event loop to listen for events and perform appropriate tasks depending on the kind of events that occur
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the most recently drawn screen visible from setting.py
            self.screen.fill(self.settings.bg_color)  # Filling the background
            self.ship.blitme()  # After filling the background, we draw the ship on the screen by calling ship.blitme()

            # Make the most recently drawn screen visible
            pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
