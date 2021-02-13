import sys

import pygame


def game(screen, game_settings, play_button, options_button, change_names_button, menu_exit_button, menu_button,
         reset_score_button):
    """Процесс игры"""
    game_settings.reset_settings()
    restart_game(screen, game_settings, menu_button, reset_score_button)
    menu_button_clicked = False
    while not menu_button_clicked:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                if event.key == pygame.K_r:
                    game_settings.reset_settings()
                    restart_game(screen, game_settings, menu_button, reset_score_button)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                # Проверка нажатия кнопку возврата в меню
                menu_button_clicked = menu_button.check_clicked(mouse_x, mouse_y)
                # Проверка нажатия на кнопку обнуления счёта
                reset_score_button_clicked = reset_score_button.check_clicked(mouse_x, mouse_y)
                if reset_score_button_clicked:
                    game_settings.reset_settings()
                    game_settings.reset_score()
                    restart_game(screen, game_settings, menu_button, reset_score_button)
                if game_settings.game_active and not menu_button_clicked and not reset_score_button_clicked:
                    continue_game(screen, game_settings, mouse_x, mouse_y)
                    if game_settings.result_changed:
                        update_screen(screen, game_settings)
                elif not game_settings.game_active:
                    restart_game(screen, game_settings, menu_button, reset_score_button)
    draw_main_menu(screen, game_settings, play_button, options_button, change_names_button, menu_exit_button)


def check_main_menu_buttons(play_button, options_button, change_names_button, menu_exit_button):
    """Проверяет нажатие кнопок в стартовом меню"""
    play_button_clicked = False
    options_button_clicked = False
    change_names_button_clicked = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            play_button_clicked = play_button.check_clicked(mouse_x, mouse_y)
            options_button_clicked = options_button.check_clicked(mouse_x, mouse_y)
            change_names_button_clicked = change_names_button.check_clicked(mouse_x, mouse_y)
            menu_exit_button_clicked = menu_exit_button.check_clicked(mouse_x, mouse_y)
            if menu_exit_button_clicked:
                sys.exit()
    return play_button_clicked, options_button_clicked, change_names_button_clicked


def check_victory(game_settings):
    """Определяет, есть ли победа"""
    checking_array = []
    if game_settings.move == -1:
        checking_array = game_settings.tic_squares
    elif game_settings.move == 1:
        checking_array = game_settings.tac_squares
    if (1 in checking_array) and (2 in checking_array) and (3 in checking_array):
        game_settings.result_type = - game_settings.move
        game_settings.result_changed = True
    elif (4 in checking_array) and (5 in checking_array) and (6 in checking_array):
        game_settings.result_type = - game_settings.move
        game_settings.result_changed = True
    elif (7 in checking_array) and (8 in checking_array) and (9 in checking_array):
        game_settings.result_type = - game_settings.move
        game_settings.result_changed = True
    elif (1 in checking_array) and (4 in checking_array) and (7 in checking_array):
        game_settings.result_type = - game_settings.move
        game_settings.result_changed = True
    elif (2 in checking_array) and (5 in checking_array) and (8 in checking_array):
        game_settings.result_type = - game_settings.move
        game_settings.result_changed = True
    elif (3 in checking_array) and (6 in checking_array) and (9 in checking_array):
        game_settings.result_type = - game_settings.move
        game_settings.result_changed = True
    elif (1 in checking_array) and (5 in checking_array) and (9 in checking_array):
        game_settings.result_type = - game_settings.move
        game_settings.result_changed = True
    elif (3 in checking_array) and (5 in checking_array) and (7 in checking_array):
        game_settings.result_type = - game_settings.move
        game_settings.result_changed = True


def check_result(game_settings):
    """Проверка результата"""
    check_victory(game_settings)
    if game_settings.result_type == 2 and (len(game_settings.tic_squares) + len(game_settings.tac_squares) == 9):
        game_settings.result_type = 0
        game_settings.result_changed = True


def continue_game(screen, game_settings, mouse_x, mouse_y):
    """Продолжает игру"""
    line = determine_line(game_settings, mouse_y)
    column = determine_column(game_settings, mouse_x)
    square = determine_square(line, column)
    if (square not in game_settings.tic_squares) and (square not in game_settings.tac_squares) and \
            (mouse_y > game_settings.scoreboard_height):
        move(screen, game_settings, square)
        check_result(game_settings)


def determine_line(game_settings, mouse_y):
    """Определение строки сетки"""
    line = (mouse_y - game_settings.scoreboard_height) // (
            game_settings.square_size + game_settings.line_thickness) + 1
    return line


def determine_column(game_settings, mouse_x):
    """Определение столбца сетки"""
    column = mouse_x // (game_settings.square_size + game_settings.line_thickness) + 1
    return column


def determine_square(line, column):
    """Определение квадрата сетки"""
    square = 3 * line + column - 3
    return square


def draw_author(screen, game_settings):
    draw_text(screen, "© 2020 Evgeniy Trofimov", game_settings.mark_font, game_settings.mark_color,
              game_settings.screen_width - 100, game_settings.screen_height - 10)


def draw_grid(screen, game_settings):
    """Рисует сетку"""
    pygame.draw.line(
        screen,
        game_settings.line_color,
        [20, game_settings.square_size + game_settings.scoreboard_height],
        [game_settings.screen_width - 20, game_settings.scoreboard_height + game_settings.square_size],
        game_settings.line_thickness
    )
    pygame.draw.line(
        screen,
        game_settings.line_color,
        [20, game_settings.scoreboard_height + 2 * game_settings.square_size],
        [game_settings.screen_width - 20, game_settings.scoreboard_height + 2 * game_settings.square_size],
        game_settings.line_thickness
    )

    pygame.draw.line(
        screen,
        game_settings.line_color,
        [game_settings.square_size, game_settings.scoreboard_height + 20],
        [game_settings.square_size, game_settings.screen_height - 20],
        game_settings.line_thickness
    )

    pygame.draw.line(
        screen,
        game_settings.line_color,
        [2 * game_settings.square_size, game_settings.scoreboard_height + 20],
        [2 * game_settings.square_size, game_settings.screen_height - 20],
        game_settings.line_thickness
    )


def draw_main_menu(screen, game_settings, play_button, options_button, change_names_button, menu_exit_button):
    """Экран главного меню"""
    screen.fill(game_settings.bg_color)
    draw_author(screen, game_settings)
    draw_text(screen, "Tic-Tac toe!", game_settings.start_font, game_settings.head_color,
              game_settings.screen_width // 2, 100)
    play_button.draw_button(screen)
    options_button.draw_button(screen)
    change_names_button.draw_button(screen)
    menu_exit_button.draw_button(screen)
    pygame.display.flip()


def draw_mark(screen, game_settings, center_x, center_y):
    pygame.draw.line(
        screen,
        game_settings.result_color,
        [center_x, center_y + 10],
        [center_x - 18, center_y - 28],
        5
    )
    pygame.draw.line(
        screen,
        game_settings.result_color,
        [center_x, center_y + 10],
        [center_x + 18, center_y - 28],
        5
    )


def draw_move_sign(screen, game_settings):
    """Рисует указатель хода"""
    left_x = game_settings.screen_width // 2 - 20
    right_x = game_settings.screen_width // 2 + 20
    y = 30
    pygame.draw.rect(
        screen,
        game_settings.scoreboard_bg_color,
        (left_x - 2, y - 20, 44, 32)
    )
    pygame.draw.line(
        screen,
        game_settings.move_sign_color,
        [left_x, y],
        [right_x, y],
        game_settings.move_sign_thickness
    )
    if game_settings.move == 1:
        pygame.draw.line(
            screen,
            game_settings.move_sign_color,
            [left_x, y],
            [left_x + 10, y + 10],
            game_settings.move_sign_thickness
        )
        pygame.draw.line(
            screen,
            game_settings.move_sign_color,
            [left_x, y],
            [left_x + 10, y - 10],
            game_settings.move_sign_thickness
        )
    elif game_settings.move == -1:
        pygame.draw.line(
            screen,
            game_settings.move_sign_color,
            [right_x, y],
            [right_x - 10, y + 10],
            game_settings.move_sign_thickness
        )
        pygame.draw.line(
            screen,
            game_settings.move_sign_color,
            [right_x, y],
            [right_x - 10, y - 10],
            game_settings.move_sign_thickness
        )
    pygame.display.flip()


def draw_names(screen, game_settings):
    """Рисует имена"""
    # Имя игрока, играющего "Крестиками"
    tic_name_image = game_settings.player_font.render(
        game_settings.tic_player_name,
        1,
        game_settings.tic_color
    )
    tic_name_image_rect = tic_name_image.get_rect()
    tic_name_image_rect.center = (
        tic_name_image_rect.width // 2 + 20,
        game_settings.scoreboard_height // 2 + 20
    )
    screen.blit(tic_name_image, tic_name_image_rect)

    # Имя игрока, играющего "Ноликами"
    tac_name_image = game_settings.player_font.render(
        game_settings.tac_player_name,
        1,
        game_settings.tac_color
    )
    tac_name_image_rect = tac_name_image.get_rect()
    tac_name_image_rect.center = (
        game_settings.screen_width - tac_name_image_rect.width // 2 - 20,
        game_settings.scoreboard_height // 2 + 20
    )
    screen.blit(tac_name_image, tac_name_image_rect)


def draw_options_menu(screen, game_settings, back_button, animated_tic_button, animated_tac_button):
    """Рисует экран меню"""
    screen.fill(game_settings.bg_color)
    draw_text(screen, "Options", game_settings.result_font, game_settings.head_color,
              game_settings.screen_width // 2, 100)
    back_button.draw_button(screen)
    draw_author(screen, game_settings)
    draw_text(screen, "Animated tics", game_settings.options_text_font, game_settings.tic_color,
              game_settings.screen_width // 3, game_settings.screen_height // 2)
    draw_text(screen, "Animated tacs", game_settings.options_text_font, game_settings.tac_color,
              game_settings.screen_width // 3, game_settings.screen_height // 2 + 70)
    animated_tic_button.draw_button(screen)
    animated_tac_button.draw_button(screen)
    update_mark(screen, game_settings, game_settings.tic_animated, animated_tic_button, -30)
    update_mark(screen, game_settings, game_settings.tac_animated, animated_tac_button, 40)
    pygame.display.flip()


def draw_result(screen, game_settings, text):
    """Подготовка результата к выводу """
    result_image = game_settings.result_font.render(text, 1, game_settings.result_color)
    result_image_rect = result_image.get_rect()
    result_image_rect.center = (game_settings.screen_width // 2, game_settings.screen_height // 2)
    screen.blit(result_image, result_image_rect)
    game_settings.game_active = False


def draw_score(screen, game_settings):
    """Рисует счёт"""
    # Счёт "крестиков"
    tic_result_image = game_settings.score_font.render(
        str(game_settings.tic_score),
        1,
        game_settings.score_color,
        game_settings.scoreboard_bg_color
    )
    tic_result_image_rect = tic_result_image.get_rect()
    tic_result_image_rect.center = (
        game_settings.screen_width // 2 - tic_result_image_rect.width // 2 - 20,
        game_settings.scoreboard_height // 2 + 20
    )
    screen.blit(tic_result_image, tic_result_image_rect)

    # Счёт "ноликов"
    tac_result_image = game_settings.score_font.render(
        str(game_settings.tac_score),
        1,
        game_settings.score_color,
        game_settings.scoreboard_bg_color
    )
    tac_result_image_rect = tac_result_image.get_rect()
    tac_result_image_rect.center = (
        game_settings.screen_width // 2 + tac_result_image_rect.width // 2 + 20,
        game_settings.scoreboard_height // 2 + 20
    )
    screen.blit(tac_result_image, tac_result_image_rect)

    double_image = game_settings.score_font.render(":", 1, game_settings.score_color)
    double_image_rect = double_image.get_rect()
    double_image_rect.center = (
        game_settings.screen_width // 2,
        game_settings.scoreboard_height // 2 + 20
    )
    screen.blit(double_image, double_image_rect)


def draw_scoreboard(screen, game_settings):
    """Рисует табло"""
    pygame.draw.rect(
        screen,
        game_settings.scoreboard_bg_color,
        (0, 0, game_settings.screen_width, game_settings.scoreboard_height),
    )

    pygame.draw.rect(
        screen,
        game_settings.scoreboard_frame_color,
        (0, 0, game_settings.screen_width, game_settings.scoreboard_height),
        8
    )
    # Имена
    draw_names(screen, game_settings)


def draw_tac(screen, game_settings, square):
    """Рисует "нолики" """
    if game_settings.tac_animated == -1:
        # Без анимации
        pygame.draw.circle(
            screen,
            game_settings.tac_color,
            game_settings.square_centers[square - 1],
            game_settings.outer_radius,
            game_settings.inner_radius
        )
        pygame.display.flip()

    elif game_settings.tac_animated == 1:
        # С анимацией
        pi = 3.15
        center_x = game_settings.square_centers[square - 1][0]
        center_y = game_settings.square_centers[square - 1][1]
        radius = game_settings.outer_radius
        for i in range(2001):
            pygame.draw.arc(
                screen,
                game_settings.tac_color,
                (center_x - radius, center_y - radius, 2 * radius, 2 * radius),
                0,
                (i / 1000) * pi,
                10
            )
            pygame.display.flip()


def draw_tic(screen, game_settings, square):
    """Рисует "крестики" """
    left_x = game_settings.square_centers[square - 1][0] - game_settings.square_size // 3
    right_x = game_settings.square_centers[square - 1][0] + game_settings.square_size // 3
    top_y = game_settings.square_centers[square - 1][1] - game_settings.square_size // 3
    bottom_y = game_settings.square_centers[square - 1][1] + game_settings.square_size // 3

    if game_settings.tic_animated == 1:
        # С анимацией

        for i in range(8 * (right_x - left_x)):
            pygame.draw.line(
                screen,
                game_settings.tic_color,
                [right_x, top_y],
                [right_x - i // 8, top_y + i // 8],
                game_settings.tic_thickness
            )
            pygame.display.flip()

        for i in range(8 * (right_x - left_x)):
            pygame.draw.line(
                screen,
                game_settings.tic_color,
                [left_x, top_y],
                [left_x + i // 8, top_y + i // 8],
                game_settings.tic_thickness
            )
            pygame.display.flip()

    elif game_settings.tic_animated == -1:
        # Без анимации
        pygame.draw.line(
            screen,
            game_settings.tic_color,
            [left_x, top_y],
            [right_x, bottom_y],
            game_settings.tic_thickness
        )
        #
        pygame.draw.line(
            screen,
            game_settings.tic_color,
            [left_x, bottom_y],
            [right_x, top_y],
            game_settings.tic_thickness
        )
        pygame.display.flip()


def draw_text(screen, text, font, color, center_x, center_y):
    """Выводит текст"""
    text_image = font.render(text, 1, color)
    text_image_rect = text_image.get_rect()
    text_image_rect.center = (center_x, center_y)
    screen.blit(text_image, text_image_rect)


def draw_entering_screen(screen, game_settings, continue_button):
    """Экран ввода имён"""
    screen.fill(game_settings.bg_color)
    continue_button.draw_button(screen)
    draw_author(screen, game_settings)

    draw_text(screen, "Enter your names!", game_settings.entering_names_font, game_settings.head_color,
              game_settings.screen_width // 2, game_settings.scoreboard_height // 2)

    draw_text(screen, "Tic player", game_settings.player_font, game_settings.tic_color, game_settings.screen_width // 2,
              game_settings.screen_height // 4)

    draw_text(screen, "Tac player", game_settings.player_font, game_settings.tac_color, game_settings.screen_width // 2,
              game_settings.screen_height // 2)

    pygame.display.flip()


def entering_names(screen, game_settings, play_button, options_button, change_names_button, menu_exit_button,
                   names_back_button, tic_name_pole, tac_name_pole):
    """Ввод имён"""
    draw_entering_screen(screen, game_settings, names_back_button)
    tic_name_pole.update_pole(screen, game_settings, game_settings.tic_player_name, game_settings.tic_color)
    tac_name_pole.update_pole(screen, game_settings, game_settings.tac_player_name, game_settings.tac_color)
    names_back_button_clicked = False
    while not names_back_button_clicked:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                names_back_button_clicked = names_back_button.check_clicked(mouse_x, mouse_y)
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                game_settings.tic_player_name = tic_name_pole.check_events(event, game_settings.tic_player_name)
                if game_settings.tic_player_name == '' and not tic_name_pole.active:
                    # Проверяет, является ли имя пустой строкой
                    game_settings.tic_player_name = 'TicPlayer'
                game_settings.tac_player_name = tac_name_pole.check_events(event, game_settings.tac_player_name)
                if game_settings.tac_player_name == '' and not tac_name_pole.active:
                    game_settings.tac_player_name = 'TacPlayer'
            tic_name_pole.update_pole(screen, game_settings, game_settings.tic_player_name, game_settings.tic_color)
            tac_name_pole.update_pole(screen, game_settings, game_settings.tac_player_name, game_settings.tac_color)
    draw_main_menu(screen, game_settings, play_button, options_button, change_names_button, menu_exit_button)


def main_menu(screen, game_settings, play_button, options_button, change_names_button, menu_exit_button,
              options_back_button, names_back_button, tic_name_pole, tac_name_pole, animated_tic_button,
              animated_tac_button, menu_button, reset_score_button):
    draw_main_menu(screen, game_settings, play_button, options_button, change_names_button, menu_exit_button)
    while True:
        play_button_clicked, options_button_clicked, change_names_button_clicked = check_main_menu_buttons(
            play_button, options_button, change_names_button, menu_exit_button
        )
        if play_button_clicked:
            # Начинает игру
            game(screen, game_settings, play_button, options_button, change_names_button, menu_exit_button, menu_button,
                 reset_score_button)
        elif options_button_clicked:
            # Заходит в опции
            options_menu(screen, game_settings, play_button, options_button, change_names_button, menu_exit_button,
                         options_back_button, animated_tic_button, animated_tac_button)
        elif change_names_button_clicked:
            # Смена имён
            entering_names(screen, game_settings, play_button, options_button, change_names_button, menu_exit_button,
                           names_back_button, tic_name_pole, tac_name_pole)


def move(screen, game_settings, square):
    """Ход"""
    if game_settings.move == 1:
        game_settings.tic_squares.append(square)
        draw_tic(screen, game_settings, square)
    else:
        game_settings.tac_squares.append(square)
        draw_tac(screen, game_settings, square)
    game_settings.move *= -1
    draw_move_sign(screen, game_settings)


def options_menu(screen, game_settings, play_button, options_button, change_names_button, menu_exit_button,
                 options_back_button, animated_tic_button, animated_tac_button):
    """Экран меню"""
    draw_options_menu(screen, game_settings, options_back_button, animated_tic_button, animated_tac_button)
    back_button_clicked = False
    while not back_button_clicked:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                # Проверка нажатия на кнопку "назад"
                back_button_clicked = options_back_button.check_clicked(mouse_x, mouse_y)
                # Проверка нажатий на кнопки настроек
                if animated_tic_button.check_clicked(mouse_x, mouse_y):
                    game_settings.tic_animated = - game_settings.tic_animated
                    update_mark(screen, game_settings, game_settings.tic_animated, animated_tic_button, -30)
                elif animated_tac_button.check_clicked(mouse_x, mouse_y):
                    game_settings.tac_animated = - game_settings.tac_animated
                    update_mark(screen, game_settings, game_settings.tac_animated, animated_tac_button, 40)
    draw_main_menu(screen, game_settings, play_button, options_button, change_names_button, menu_exit_button)


def output_result(screen, game_settings):
    """Вывод результата"""
    if game_settings.result_type == -1:
        draw_result(screen, game_settings, game_settings.tac_player_name + " win!")
        game_settings.tac_score += 1
    elif game_settings.result_type == 1:
        draw_result(screen, game_settings, game_settings.tic_player_name + " win!")
        game_settings.tic_score += 1
    elif game_settings.result_type == 0:
        draw_result(screen, game_settings, "It is draw!")


def restart_game(screen, game_settings, menu_button, reset_score_button):
    """Начало новой партии"""
    game_settings.reset_settings()
    screen.fill(game_settings.bg_color)
    draw_author(screen, game_settings)
    draw_grid(screen, game_settings)
    draw_scoreboard(screen, game_settings)
    draw_move_sign(screen, game_settings)
    menu_button.draw_button(screen)
    reset_score_button.draw_button(screen)
    update_screen(screen, game_settings)


def update_mark(screen, game_settings, setting, button, offset_y):
    """Обновление графического представления настроек"""
    pygame.draw.rect(
        screen,
        game_settings.bg_color,
        (game_settings.screen_width - game_settings.screen_width // 4 - 25,
         game_settings.screen_height // 2 + offset_y, 60, 60))
    button.draw_button(screen)
    if setting == 1:
        draw_mark(screen, game_settings, game_settings.screen_width - game_settings.screen_width // 4,
                  game_settings.screen_height // 2 + offset_y + 30)
    pygame.display.flip()


def update_screen(screen, game_settings):
    """Обновление экрана"""
    output_result(screen, game_settings)
    draw_score(screen, game_settings)
    pygame.display.flip()
