import pygame


class Ship:
    """
    A class to manage the ship.
    Una clase que maneja/gestiona/administra la nave
    """

    def __init__(self, ai_game):  # Take two parameters. 1-The self reference. 2-Instace of AlienInvasion class
        """
        Constructor of Ship
        Initialize the ship and set its starting position.
        """
        self.screen = ai_game.screen  # Assign the screen to the attribute self.screen.
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()  # Access to the screen with the method get_rect()

        # Load the ship image and get its rect.
        SHIP = pygame.image.load("/home/franco/PycharmProjects/Alien-Invasion/images/ship.png")
        SHIP_SCALING = pygame.transform.scale(SHIP, (70, 60))

        self.image = SHIP_SCALING
        self.rect = self.image.get_rect()  # With the method get_rect() we can access the ship surface's rect attribute
        # With a rect object we can use the x- and y- coordinates.
        # There are 4 principal attributes to work with the screen --> top, buttom, left, right
        # There are some attributes the combine these attributes like midtop, midbottom, midleft, midright

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)

        # Movement flag to give the ship continous movement
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """
        Update the ship's position based on the movement flag.
        :return:
        """
        # Update the ship's x value, not the rect.
        if self.moving_right and (self.rect.right < self.screen_rect.right):
            self.x += self.settings.ship_speed
        if self.moving_left and (self.rect.left > 0):
            self.x -= self.settings.ship_speed

        # Update rect object from self.x.
        self.rect.x = self.x

    def blitme(self):
        """
        Draw the ship at its current location.
        Dibuja a la nave en su localizacion normalizada.
        :return:
        """
        self.screen.blit(self.image, self.rect)
