import sys

import pygame


def run_game():
    # init game and create a screen object
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")

    # start main
    while True:
        # monitor keyboard and mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # show the screen
        pygame.display.flip()

run_game()
