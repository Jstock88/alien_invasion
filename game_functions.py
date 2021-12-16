import sys

import pygame

def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def check_keydown_events(event, ship):
    if event.key == pygame.K_d:
        ship.moving_right = True
    elif event.key == pygame.K_a:
        ship.moving_left = True

def check_keyup_events(event, ship):
        if event.key == pygame.K_d:
            ship.moving_right = False
        elif event.key == pygame.K_a:
            ship.moving_left = False


def update_screen(ai_settings, screen, ship):
    #Updates images on the screen and flip to the new screen.
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    #Make the most recently drawn screen visible
    pygame.display.flip()
