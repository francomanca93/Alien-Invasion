import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):  # The Bullet class inherits from Sprite that we import from pygame.sprite module
    # When you use sprites, you can group related elements in your game and act on all the grouped elements at once.
    """A class to manage bullets fired from the ship"""

    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position."""
        super().__init__()  # We call super() to inherit properly from Sprite
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect attribute at (0, 0) with pygame.Rect() class and the set correct position.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop  # This will make the bullet emerge from the top of the ship

        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen"""
        # Update the decimal position of the bullet.
        self.y -= self.settings.bullet_speed
        #Update the rect position.
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)