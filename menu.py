import pygame
import sys

import settings
from game import Game
from settings import CURRENT_SCREEN, MENU_SOUND

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
HOVER_COLOR = (150, 150, 150)
TITLE = (179, 36, 36)

# Настройки кнопок
BUTTON_WIDTH = 350
BUTTON_HEIGHT = 50
BUTTON_MARGIN = 20


class Menu:
    """
    Класс экрана меню. Отображает кнопки выбора сложности игры, таблицы рекордов, титров, выхода из игры.
    """
    def __init__(self, screen):
        """
        Конструктор, создаёт кнопки и их обработчики
        :param screen: Объект дисплея
        """
        self.screen = screen
        self.font = pygame.font.Font(None, 50)
        self.buttons = [
            {"label": "Играть", "action": self.play_game},
            {"label": "Таблица рекордов", "action": self.show_highscores},
            {"label": "Титры", "action": self.show_credits},
            {"label": "Выход", "action": self.exit_game},
        ]
        self.bg = pygame.image.load(settings.resource_path("imgs/bg.webp"))
        MENU_SOUND.play(loops=10)

    def draw(self):
        """
        Метод отрисовки экрана меню. Рисует кнопки и текст меню.
        :return:
        """
        self.screen.fill(BLACK)
        self.screen.blit(self.bg, self.screen.get_rect())
        # Рисуем заголовок
        title_font = pygame.font.Font(None, 80)
        title = title_font.render("Katamacy 2D", True, TITLE)
        title_rect = title.get_rect(center=(self.screen.get_width() // 2, 100))
        self.screen.blit(title, title_rect)

        # Рисуем кнопки
        screen_width = self.screen.get_width()
        screen_height = self.screen.get_height()

        for i, button in enumerate(self.buttons):
            x = (screen_width - BUTTON_WIDTH) // 2
            y = 200 + i * (BUTTON_HEIGHT + BUTTON_MARGIN)
            button_rect = pygame.Rect(x, y, BUTTON_WIDTH, BUTTON_HEIGHT)

            # Меняем цвет кнопки при наведении
            if button_rect.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(self.screen, HOVER_COLOR, button_rect)
            else:
                pygame.draw.rect(self.screen, GRAY, button_rect)

            # Текст кнопки
            label = self.font.render(button["label"], True, BLACK)
            label_rect = label.get_rect(center=button_rect.center)
            self.screen.blit(label, label_rect)

    def handle_event(self, event):
        """
        Слушатель событий управления. При клике в область кнопки вызывает её обработчик
        :param event: Объект событий
        :return:
        """
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for i, button in enumerate(self.buttons):
                x = (self.screen.get_width() - BUTTON_WIDTH) // 2
                y = 200 + i * (BUTTON_HEIGHT + BUTTON_MARGIN)
                button_rect = pygame.Rect(x, y, BUTTON_WIDTH, BUTTON_HEIGHT)
                if button_rect.collidepoint(event.pos):
                    button["action"]()

    def play_game(self):
        """
        Метод выбора экрана сложности
        :return:
        """
        print("В сложность")
        settings.CURRENT_SCREEN = "difficulty"

    def show_highscores(self):
        """
        Метод выбора экрана таблицы рекордов
        :return:
        """
        print("Открыть таблицу рекордов")  # Здесь будет логика отображения рекордов
        settings.CURRENT_SCREEN = "records"

    def show_credits(self):
        """
        Метод выбора экрана титров
        :return:
        """
        print("Открыть титры")  # Здесь будет отображение титров
        settings.CURRENT_SCREEN = "credit"
        MENU_SOUND.fadeout(2)
        settings.CREDITS_SOUND.play()

    def exit_game(self):
        """
        Метод завершения игры
        :return:
        """
        pygame.quit()
        sys.exit()
