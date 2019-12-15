import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """a bullet management class"""

    def __init__(self, ai_settings, screen, ship):
        """create a bullet object at ship position"""
        super().__init__()

        self.screen = screen

        # create bullet shape at (0, 0) position, and set the right position
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # store bullet y position
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """move bullet upwards"""

        # update y position
        self.y -= self.speed_factor
        # update bullet position
        self.rect.y = self.y

    def draw_bullet(self):
        """draw bullet"""
        pygame.draw.rect(self.screen, self.color, self.rect)
