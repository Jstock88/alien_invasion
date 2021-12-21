import sys
import pygame

from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf

#Initialize game and creaate a screen object.
def run_game():

    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #Make a ship
    ship = Ship(ai_settings, screen)

    #Make a group to store bullets and aliens.
    bullets = Group()
    aliens = Group()

    #Make an Alien
    gf.create_fleet(ai_settings, screen, aliens)

    #Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

        #Redraws the screen with each loop
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        #Make the most recently drawn screen visible
        pygame.display.flip()


run_game()
