import sys

import pygame


def check_events(ship):
    """respond to keyboard and mouse"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False


def update_screen(ai_settings, screen, ship):
    """update images in screen, switch to new screen"""

    # repaint screen
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # show the latest screen content
    pygame.display.flip()
