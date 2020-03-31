import sys
import pygame


class AlienInvasion:
    """Overall class to manage game assets and behavior
    Clase principal para manejar las acciones y comportamiento del juego"""

    def __init__(self):
        """
        Initialize the game, and create game resources.
        Inicializamos el juego y creamos los recursos del juego
        """
        pygame.init()  # Inicializes the background setting that Pygame needs to work properly

        # Attribute
        self.screen = pygame.display.set_mode((1200, 800))
        # we assign an object named surface (the display window) to the attribute self.screen.
        # We call this function to create a display window
        # In this screen we well draw all the game's graphical elements
        # (1200, 800) -> Tuple that define window size
        pygame.display.set_caption("Alien Invasion")

        # Set the background color. Seteamos el color de fondo
        self.bg_color = (230, 230, 230)

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

            # Redraw the most recently drawn screen visible.
            self.screen.fill(self.bg_color)

            # Make the most recently drawn screen visible
            pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
