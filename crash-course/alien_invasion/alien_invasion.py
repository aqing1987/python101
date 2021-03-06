import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
import game_functions as gf


def run_game():
    # init game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # create play button
    play_button = Button(ai_settings, screen, "Play")

    # create stats object for saving game stats, and create scoreboard
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # create a ship, a bullets group and an alien group
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # create alien fleet
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # background music
    #pygame.mixer.music.load("sounds/111.mp3")
    #pygame.mixer.music.play(loops=-1, start=0.0)
    music1 = pygame.mixer.Sound("sounds/222.wav")

    # start main
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship,
            aliens, bullets, music1)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens,
                bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens,
                bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens,
                        bullets, play_button)


run_game()
