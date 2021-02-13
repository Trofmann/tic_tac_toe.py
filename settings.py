import pygame.font


class Settings:
    def __init__(self):
        """Инициализирует всевозможные параметры игры"""
        # Параметры табло
        self.scoreboard_height = 100
        self.scoreboard_bg_color = (204, 204, 204)
        self.scoreboard_frame_color = (255, 215, 0)

        self.score_font = pygame.font.SysFont('verdana', 40)
        self.score_color = (0, 0, 0)

        # Параметры экрана
        self.screen_width = 504
        self.screen_height = self.screen_width + self.scoreboard_height
        self.bg_color = (150, 150, 230)
        self.head_color = (255, 215, 0)

        # Если кнопка Play нажата - True, иначе - нет
        self.play_button_clicked = False

        # Параметры сетки
        self.square_size = self.screen_width // 3
        self.line_thickness = 5
        self.line_color = (0, 0, 0)

        # Параметры "нолика"
        self.tac_color = (0, 0, 139)
        self.outer_radius = self.square_size // 3
        self.inner_radius = 10

        # Параметры "крестика"
        self.tic_color = (169, 32, 62)
        self.tic_thickness = 15

        # Параметры текста результата
        self.result_font = pygame.font.SysFont('verdana', 60)
        self.result_color = (255, 153, 0)

        # Центры квадратов
        self.square_centers = [
            (self.square_size // 2, self.scoreboard_height + self.square_size // 2),
            (3 * self.square_size // 2, self.scoreboard_height + self.square_size // 2),
            (5 * self.square_size // 2, self.scoreboard_height + self.square_size // 2),
            (self.square_size // 2, self.scoreboard_height + 3 * self.square_size // 2),
            (3 * self.square_size // 2, self.scoreboard_height + 3 * self.square_size // 2),
            (5 * self.square_size // 2, self.scoreboard_height + 3 * self.square_size // 2),
            (self.square_size // 2, self.scoreboard_height + 5 * self.square_size // 2),
            (3 * self.square_size // 2, self.scoreboard_height + 5 * self.square_size // 2),
            (5 * self.square_size // 2, self.scoreboard_height + 5 * self.square_size // 2)
        ]

        # Счёт
        self.tic_score = 0
        self.tac_score = 0

        # Имена игроков
        self.tic_player_name = "TicPlayer"
        self.tac_player_name = "TacPlayer"
        self.player_font = pygame.font.SysFont('verdana', 30)

        # Параметры значка
        self.mark_font = pygame.font.SysFont('verdana', 15)
        self.mark_color = (100, 100, 100)

        self.names_entered = False

        # Парметры анимации фигур. 1 - есть анимация, -1 - нет
        self.tic_animated = 1
        self.tac_animated = 1

        # Для экрана опций
        self.options_button_clicked = False
        self.back_button_clicked = True
        self.options_text_font = pygame.font.SysFont('verdana', 40)

        # Параметры указателя хода
        self.move_sign_thickness = 5
        self.move_sign_color = (0, 200, 100)

        self.game_active = True

        # Изменение результата
        self.result_changed = False

        # Если 1, то ходят "крестики", если -1 - "нолики"
        self.move = 1

        # Квадраты, в которых "крестики"
        self.tic_squares = []

        # Квадраты, в которых "нолики"
        self.tac_squares = []

        # -1 - победили "нолики", 0 - ничья, 1 - победили "крестики", 2 - ничьи нет, игра продолжается
        self.result_type = 2

        self.entering_names_font = pygame.font.SysFont('verdana', 50)
        self.start_font = pygame.font.SysFont('verdana', 70)

    def reset_settings(self):
        """Возвращение к настройкам по умолчанию"""
        # Если True - игра работает, иначе - нет
        self.game_active = True

        # Изменение результата
        self.result_changed = False

        # Если 1, то ходят "крестики", если -1 - "нолики"
        self.move = 1

        # Квадраты, в которых "крестики"
        self.tic_squares = []

        # Квадраты, в которых "нолики"
        self.tac_squares = []

        # -1 - победили "нолики", 0 - ничья, 1 - победили "крестики", 2 - ничьи нет, игра продолжается
        self.result_type = 2

    def reset_score(self):
        """Обнуление счёта"""
        self.tic_score = 0
        self.tac_score = 0
