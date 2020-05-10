import sys
from time import sleep

import pygame

from settings import Settings  # Del archivo setting.py importamos la clase Settings
from game_stats import GameStats
from ship import Ship  # Del archivo ship.py importamos la clase Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    """Overall class to manage game assets and behavior
    Clase principal para manejar las acciones y comportamiento del juego"""

    # Contructor of AlienInvasion
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

        # Create an instance to store game statistics.
        self.stats = GameStats(self)

        # Create an instance of the Ship class.
        self.ship = Ship(self)

        # The self argument give to Ship access to the game's resources, like a screen object
        # When you use sprites, you can group related elements in your game and act on all the grouped at once.
        self.bullets = pygame.sprite.Group()  # We create an attribute that it will create a group of bullets like a ArrayList in Java
        self.aliens = pygame.sprite.Group()  # We create an attribute that it will create a group of aliens

        self._create_fleet()

    # ------------------------- Run Game ------------------------------------------------------------------

    def run_game(self):
        """
        Start the main loop for the game
        Empieza el ciclo inicial para el juego
        :return:
        """
        # The while loop contains an event loop and code that manages screen updates
        # event = pressing a key or moving the mouse
        while True:
            self._check_events()  # Check for player input
            self._update_ship()  # Update the position of the ship
            self._update_bullets()  # Update the position of the any bullets that we have been fired.
            self._update_alien()  # Update the position of the fleet of alien.
            self._update_screen()  # We use the update position to draw a new screen

    # ------------------------- Events ------------------------------------------------------------------

    def _check_events(self):
        """Respond to keypress and mouse events"""
        # Watch for keyyboard and mouse events.
        # Muestra los eventos del teclado y el mouse
        # Event loop to listen for events and perform appropriate tasks depending on the kind of events that occur
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # This event gets me access to close the window
                sys.exit()
            elif event.type == pygame.KEYDOWN:  # This events get me access to move el ship
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True  # Move the ship to the right
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True  # Move the ship to the left
        elif (event.key == pygame.K_RIGHT) and (event.key == pygame.K_LEFT):  # Stop the ship
            self.ship.moving_right = False
            self.ship.moving_left = False
        elif event.key == pygame.K_q:  # Pressing Q to quit
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    # -------------------------- Ship ------------------------------------------------------------------

    def _update_ship(self):
        """Update the positions of the ship"""
        self.ship.update()

    # ------------------------- Bullets ------------------------------------------------------------------

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group"""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()

        # Get rid (deshacerse) of bullets that have dissapeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        # print(len(self.bullets))  # We print the quantity of the bullets. We can know whether bullet disappeared
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions."""
        # Check for any bullets that have hit aliens.
        #   If so, get rid of the bullet and the alien.
        # sprite.groupcollide() --> adds a key-value pair to the dictionary it returns
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if not self.aliens:
            # Destroy existing bullets and create a new fleet.
            self.bullets.empty()  # Destroy existing bullets
            self._create_fleet()  # create a new fleet.

    # ------------------------- Aliens ------------------------------------------------------------------

    def _update_alien(self):
        """ Check if the fleet is at an edge,
        then update the positions of all aliens in the fleet"""
        self._check_fleet_edges()
        self.aliens.update()

        # Look for alien-ship collisions.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            # print("Ship hit!!!!!!")
            self._ship_hit()
        
        # Look for aliens hitting the bottom of the screen
        self._check_aliens_bottom()

    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Create an alien and find the number of aliens in a row.
        # Spacing between each alien is equal to one alien width.
        alien = Alien(self)  # Intance of Alien() class
        alien_width, alien_height = alien.rect.size

        # Number of alien in x
        available_space_x = self.settings.screen_width - (1 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # Number of rows of alien that fit on the screen
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (4 * alien_height - ship_height))
        number_rows = available_space_y // (2 * alien_height)

        # Create the full fleet of aliens.
        for row_number in range(number_rows):
            # Create the first row of aliens.
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """Create an alien and place it in the row."""
        # Create an alien and place it in the row.
        alien = Alien(self)  # Intance of Alien() class

        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien_height + 2 * alien_height * row_number
        self.aliens.add(alien)  # Adding alien of the before object created to the aliens group

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():  # Para cada alien en aliens.sprites() --> grupo de aliens
            if alien.check_edges():  # si el alien toca (checkea) los bordes
                self._change_fleet_direction()  # cambiar la direcion de movimiento de la flota
                break  # salir del for

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():  # Para cada alien en aliens.sprites() --> grupo de aliens
            alien.rect.y += self.settings.fleet_drop_speed  #
        self.settings.fleet_direction *= -1
    
    def _check_aliens_bottom(self):
        """Check if any aliens hace reached the bottom of the screen."""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Treat this the same as if the ship got hit.
                self._ship_hit()
                break

    # ------------------------- Ship, Aliens and Bullets -------------------------------------------------

    def _ship_hit(self):
        """Respond to the ship being hit by an alien"""

        if self.stats.ship_left > 0:
            # Decrement ships_left
            self.stats.ships_left -= 1

            # Get rid of any remaining aliens and bullets --> Deshacerse de cualquier de los restos de los aliens y balas
            self.aliens.empty()
            self.bullets.empty()

            # Create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()

            # Pause
            sleep(0.5)
        else:
            self.stats.game_active = False

    # ------------------------- Screen ------------------------------------------------------------------

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen"""
        # Redraw the most recently drawn screen visible from setting.py
        self.screen.fill(self.settings.bg_color)  # Filling the background
        self.ship.blitme()  # After filling the background, we draw the ship on the screen by calling ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        # Make the most recently drawn screen visible
        pygame.display.flip()

    # -------------------------------------------------------------------------------------------


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
