import sys

import pygame

from settings import Settings
from ship import Ship


def run_game():
    # init game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # create a ship
    ship = Ship(screen)

    # start main
    while True:
        # monitor keyboard and mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # paint the screen each loop
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        # show the screen
        pygame.display.flip()


run_game()
