import pygame


class Ship():

    def __init__(self, screen):
        """init ship and its start position"""
        self.screen = screen

        # get ship image and its rectangle
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # put new ship at center and bottom
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # move right flag
        self.moving_right = False

    def update(self):
        """adjust ship position according the flag"""
        if self.moving_right:
            self.rect.centerx += 1

    def blitme(self):
        """draw ship at pointed position"""
        self.screen.blit(self.image, self.rect)