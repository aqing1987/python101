import sys

import pygame


def check_events(ship):
    """respond to keyboard and mouse"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # shift ship to right
                ship.rect.centerx += 1


def update_screen(ai_settings, screen, ship):
    """update images in screen, switch to new screen"""

    # repaint screen
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # show the latest screen content
    pygame.display.flip()
