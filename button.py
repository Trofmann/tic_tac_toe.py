import pygame.font


class Button:
    """Класс кнопки"""

    def __init__(self, screen, center_x, center_y, text, width=200, height=50, font_size=40, button_color=(0, 200, 100),
                 text_color=(255, 255, 255)):
        """Инициализирует атрибуты кнопки"""
        self.screen = screen
        # Параметры кнопки
        self.width = width
        self.height = height
        self.button_color = button_color
        self.text_color = text_color
        self.button_frame_color = (0, 0, 0)

        self.font = pygame.font.SysFont('verdana', font_size)

        # Построение прямоугольника кнопки
        self.button_rect = pygame.Rect(0, 0, self.width, self.height)
        self.button_rect.center = (center_x, center_y)

        # Создание текста кнопки
        self.prep_text(text)

    def check_clicked(self, mouse_x, mouse_y):
        clicked = self.button_rect.collidepoint(mouse_x, mouse_y)
        return clicked

    def draw_button(self, screen):
        """Рисует кнопку"""
        self.screen.fill(self.button_color, self.button_rect)
        self.screen.blit(self.text_image, self.text_image_rect)
        pygame.draw.rect(screen, self.button_frame_color, self.button_rect, 2)

    def prep_text(self, text):
        """Подготовка текста к выводу"""
        self.text_image = self.font.render(text, 1, self.text_color, self.button_color)
        self.text_image_rect = self.text_image.get_rect()
        self.text_image_rect.center = self.button_rect.center
