import sys

import pygame
from bullet import Bullet
from alien import Alien

def check_events(ai_settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_d:
        ship.moving_right = True
    elif event.key == pygame.K_a:
        ship.moving_left = True
    elif event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_SPACE:
        #Creates a bullet and adds it to the bullets group.
        if len(bullets) < ai_settings.bullets_allowed:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)

def check_keyup_events(event, ship):
        if event.key == pygame.K_d:
            ship.moving_right = False
        elif event.key == pygame.K_a:
            ship.moving_left = False


def update_screen(ai_settings, screen, ship, aliens, bullets):
    #Updates images on the screen and flip to the new screen.
    screen.fill(ai_settings.bg_color)
    #Redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    #Make the most recently drawn screen visible
    pygame.display.flip()

def update_bullets(bullets):
    #Updates bullet positions
    bullets.update()

    #Get rid of bullets that have disappeared
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def create_fleet(ai_settings, screen, aliens):
    #Creates a full fleet of aliens
    #Create an alien and find the number of aliens in a row
    #Spacing between each alien is equal to one alien screen_width
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    availiable_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(availiable_space_x / (2 * alien_width))

    #Create the first row of aliens
    for alien_number in range(number_aliens_x):
        #Create an alien and place it in t he row
        alien = Alien(ai_settings, screen)
        alien.x = alien_width + 2 * alien_width * alien_number
        aliens.add(alien)
