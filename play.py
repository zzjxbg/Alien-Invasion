import sys
from time import sleep
import pygame
from bullet import bullet
from alien import Alien

def playbutton(settings, screen, states, records, play_button, player,
               aliens, bullets, mouse_x, mouse_y):
    # start the game when player clicks the play button
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not states.game_active:
        settings.new_settings()
        pygame.mouse.set_visible(False)
        states.renew()
        states.game_active = True

        records.update_record()
        records.record()
        records.level()
        records.left_player()

        aliens.empty()
        bullets.empty()

        fleet(settings, screen, player, aliens)
        player.set_center()


def shoot(settings, screen, player, bullets):
    # shoot bullets
    if len(bullets) < settings.bullets_allowed:
        new_bullet = bullet(settings, screen, player)
        bullets.add(new_bullet)


def new_screen(settings, screen, states, records, player, aliens, bullets,
               play_button):
    # update screen during the game
    screen.fill(settings.background_color)

    for bullet in bullets.sprites():
        bullet.bullet()
    player.current()
    aliens.draw(screen)

    records.display_grade()

    if not states.game_active:
        play_button.button()
    pygame.display.flip()


def more_bullets(settings, screen, states, records, player, aliens, bullets):
    # add more bullets during the game
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    collision(settings, screen, states, records, player, aliens, bullets)


def high_grade(states, records):
    # update new high grade
    if states.grade > states.high_grade:
        states.high_grade = states.grade
        records.record()


def collision(settings, screen, states, records, player,
              aliens, bullets):
    # update states when bullets and aliens have a collision 
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if collisions:
        for aliens in collisions.values():
            states.grade += settings.points * len(aliens)
            records.update_record()
        high_grade(states, records)

    if len(aliens) == 0:
        bullets.empty()
        settings.speedup()

        states.level += 1
        records.level()

        fleet(settings, screen, player, aliens)


def margin(settings, aliens):
    for alien in aliens.sprites():
        if alien.endRow():
            move(settings, aliens)
            break


def move(settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += settings.fleet_drop_speed
    settings.direction *= -1


def player_hit(settings, screen, states, records, player, aliens, bullets):
    # update states when player hit by alien
    if states.player_left > 0:
        states.player_left -= 1
        records.left_player()
    else:
        states.game_active = False
        pygame.mouse.set_visible(True)
    aliens.empty()
    bullets.empty()
    fleet(settings, screen, player, aliens)
    player.set_center()
    sleep(0.5)


def alien_at_x(settings, alien_width):
    # how many aliens in a row
    available_space_x = settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def rows(settings, player_height, alien_height):
    # how many rows of aliens
    available_space_y = (settings.screen_height - (3 * alien_height) - player_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def new_alien(settings, screen, aliens, alien_number, row_number):
    alien = Alien(settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def fleet(settings, screen, player, aliens):
    # create a fleet
    alien = Alien(settings, screen)
    number_aliens_x = alien_at_x(settings, alien.rect.width)
    number_rows = rows(settings, player.rect.height,
                       alien.rect.height)

    # Create the fleet of aliens.
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            new_alien(settings, screen, aliens, alien_number,
                      row_number)



def keydown(event, settings, screen, player, bullets):
    # respond to player's input
    if event.key == pygame.K_RIGHT:
        player.moving_right = True
    elif event.key == pygame.K_LEFT:
        player.moving_left = True
    elif event.key == pygame.K_SPACE:
        shoot(settings, screen, player, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def keyup(event, player):
    # respond to player's input
    if event.key == pygame.K_RIGHT:
        player.moving_right = False
    elif event.key == pygame.K_LEFT:
        player.moving_left = False


def incident(settings, screen, states, records, play_button, player, aliens,
             bullets):
    # respond to player's input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            keydown(event, settings, screen, player, bullets)
        elif event.type == pygame.KEYUP:
            keyup(event, player)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            playbutton(settings, screen, states, records, play_button,
                       player, aliens, bullets, mouse_x, mouse_y)

def over(settings, screen, states, records, player, aliens,
         bullets):
    # game over when aliens down to the bottom of screen
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            player_hit(settings, screen, states, records, player, aliens, bullets)
            break


def new_aliens(settings, screen, states, records, player, aliens, bullets):
    # update aliens position in fleet
    margin(settings, aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(player, aliens):
        player_hit(settings, screen, states, records, player, aliens, bullets)
    over(settings, screen, states, records, player, aliens, bullets)