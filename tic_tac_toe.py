import pygame

import game_functions as gf
import settings
from button import Button
from entry_pole import EntryPole


def run_game():
    pygame.init()
    game_settings = settings.Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Tic-Tac-Toe by Evgeniy Trofimov")

    # Создание кнопкок
    play_button = Button(screen, game_settings.screen_width // 2, game_settings.screen_height // 2 - 50,
                         "Play")
    options_button = Button(screen, game_settings.screen_width // 2, game_settings.screen_height // 2 + 35,
                            "Options")
    change_names_button = Button(screen, game_settings.screen_width // 2, game_settings.screen_height // 2 + 120,
                                 "Change names", font_size=24)
    menu_exit_button = Button(screen, game_settings.screen_width // 2, game_settings.screen_height // 2 + 205,
                              "Exit")
    names_back_button = Button(screen, game_settings.screen_width // 2, game_settings.screen_height - 50,
                               "Back")
    options_back_button = Button(screen, game_settings.screen_width // 2, game_settings.screen_height - 50, "Back",
                                 100,
                                 38, 32)

    animated_tic_button = Button(screen, game_settings.screen_width - game_settings.screen_width // 4,
                                 game_settings.screen_height // 2, "", 38, 38, 0, game_settings.scoreboard_bg_color)
    animated_tac_button = Button(screen, game_settings.screen_width - game_settings.screen_width // 4,
                                 game_settings.screen_height // 2 + 70, "", 38, 38, 0,
                                 game_settings.scoreboard_bg_color
                                 )
    menu_button = Button(screen, 85, 30, "Menu", 130, 30, 20)
    reset_score_button = Button(screen, game_settings.screen_width - 85, 30, "Reset score", 130, 30, 20)
    # Создание полей ввода имён
    tic_name_pole = EntryPole(game_settings.screen_width // 2, game_settings.screen_height // 4 + 50)
    tac_name_pole = EntryPole(game_settings.screen_width // 2, game_settings.screen_height // 2 + 50)

    # Главное меню
    gf.main_menu(screen, game_settings, play_button, options_button, change_names_button, menu_exit_button,
                 options_back_button, names_back_button, tic_name_pole, tac_name_pole, animated_tic_button,
                 animated_tac_button, menu_button, reset_score_button)


run_game()
