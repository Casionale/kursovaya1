# Цвета
import pygame

import settings
from game import Game
from settings import MENU_SOUND

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
HOVER_COLOR = (150, 150, 150)
TITLE = (179, 36, 36)

# Настройки кнопок
BUTTON_WIDTH = 450
BUTTON_HEIGHT = 60
BUTTON_MARGIN = 40


class Difficulty:
    """
    Экран выбора сложности игры.

    Attributes
    screen : pygame.screen
        Объект экрана
    """

    def __init__(self, screen):
        """
        Конструктор
        :param screen: объект экрана
        """
        self.screen = screen
        self.font = pygame.font.Font(None, 50)
        self.buttons = [
            {"label": "Легко (2 уровня)", "action": self.start_easy},
            {"label": "Стандарт (5 уровней)", "action": self.start_medium},
            {"label": "Сложно (7 уровней)", "action": self.start_hard},
        ]
        self.bg = pygame.image.load(settings.resource_path("imgs/bg.webp"))

    def draw(self):
        """
        Отрисовывает экран выбора сложности, состоящий из 3 кнопок выбора сложности.
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

        for i, button in enumerate(self.buttons):
            x = (screen_width - BUTTON_WIDTH) // 2
            y = 300 + i * (BUTTON_HEIGHT + BUTTON_MARGIN)
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
        Слушает события управления и выходит в меню по нажатию на Enter
        :param event: Объект событий
        :return:
        """
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for i, button in enumerate(self.buttons):
                x = (self.screen.get_width() - BUTTON_WIDTH) // 2
                y = 300 + i * (BUTTON_HEIGHT + BUTTON_MARGIN)
                button_rect = pygame.Rect(x, y, BUTTON_WIDTH, BUTTON_HEIGHT)
                if button_rect.collidepoint(event.pos):
                    button["action"]()

    def start(self, difficulty):
        """
        Метод запуска игры
        :param difficulty:Сложность игры
        :return:
        """
        settings.CURRENT_SCREEN = "game"
        game = Game(self.screen)
        MENU_SOUND.fadeout(2)
        game.to_game(max_level=difficulty)
        MENU_SOUND.fadeout(2)

    def start_easy(self):
        """
        Метод запуска лёгкой игры из 2 уровней
        :return:
        """
        print("Начинаем лёгкую игру!")
        self.start(2)

    def start_medium(self):
        """
        Метод запуска средней сложности игры из 5 уровней
        :return:
        """
        print("Начинаем стандартную игру!")
        self.start(5)

    def start_hard(self):
        """
        Метод запуска сложной игры из 7 уровней
        :return:
        """
        print("Начинаем сложную игру!")
        self.start(7)
