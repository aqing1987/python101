import sys

import pygame


def run_game():
    # init game and create a screen object
    pygame.init()
    screen = pygame.display.set_mode([1200, 800])
    pygame.display.set_caption("Alien Invasion")

    # set background color
    bg_color = (230, 230, 230)

    # start main
    while True:
        # monitor keyboard and mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # paint the screen each loop
        screen.fill(bg_color)

        # show the screen
        pygame.display.flip()


run_game()
