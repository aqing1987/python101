import pygame


class Ship():

    def __init__(self, ai_settings, screen):
        """init ship and its start position"""
        self.screen = screen
        self.ai_settings = ai_settings

        # get ship image and its rectangle
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # put new ship at center and bottom
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # store float number in center
        self.center = float(self.rect.centerx)

        # move flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """adjust ship position according the flag"""
        # update ship.center (not rect)
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # update rect according to center
        self.rect.centerx = self.center

    def blitme(self):
        """draw ship at pointed position"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """ceter the ship"""
        self.center = self.screen_rect.centerx
