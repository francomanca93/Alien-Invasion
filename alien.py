import pygame
from pygame.sprite import Sprite


class Alien(Sprite):  # Alien inherit from Sprite
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen

        # Load the ship image and get its rect.
        ALIEN = pygame.image.load("/home/franco/PycharmProjects/Alien-Invasion/images/AlienShip3.png")
        ALIEN_SCALING = pygame.transform.scale(ALIEN, (50, 50))

        # Load the alien image and set its rect attribute.
        self.image = ALIEN_SCALING
        self.rect = self.image.get_rect()  # Pygame lets you treat all game elements like RECTANGLES with .get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)