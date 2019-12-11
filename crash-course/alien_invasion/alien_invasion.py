import sys

import pygame

from settings import Settings


def run_game():
    # init game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # start main
    while True:
        # monitor keyboard and mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # paint the screen each loop
        screen.fill(ai_settings.bg_color)

        # show the screen
        pygame.display.flip()


run_game()
