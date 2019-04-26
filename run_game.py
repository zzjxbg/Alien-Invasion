import pygame
import play as gf
from pygame.sprite import Group
from settings import Settings
from states import States
from record import record
from button import Button
from player import Player


def run_game():
    """ initialize """
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(
        (settings.screen_width, settings.screen_height))
    event = pygame.event.poll()

    # add music
    pygame.mixer.music.load("music.mp3")
    pygame.mixer.music.play(3, 0)
    pygame.mixer.music.set_volume(0.3)
    pygame.display.set_caption("alien_invasion_game")

    play_button = Button(settings, screen, "Play")
    states = States(settings)
    records = record(settings, screen, states)
    background_color = (0, 0, 0)

    player = Player(settings, screen)
    bullets = Group()
    aliens = Group()
    gf.fleet(settings, screen, player, aliens)
    while True:
        gf.incident(settings, screen, states, records, play_button, player, aliens, bullets)
        if states.game_active:
            player.update()
            gf.more_bullets(settings, screen, states, records, player, aliens, bullets)
            gf.new_aliens(settings, screen, states, records, player, aliens, bullets)
        gf.new_screen(settings, screen, states, records, player, aliens, bullets, play_button)
run_game()