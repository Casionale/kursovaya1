import pygame

import DB
import settings

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
TITLE = (179, 36, 36)


class RecordsScreen:
    """
    Класс экрана рекордов
    """

    def __init__(self, screen):
        """
        Конструктор класса, создаёт экран рекордов
        :param screen: Объект дисплея Pygame
        """
        self.screen = screen
        self.font = pygame.font.Font(None, 50)
        self.records_font = pygame.font.Font(None, 30)
        self.input_box = pygame.Rect((self.screen.get_width() // 2 - 150, 250), (300, 50))
        self.db = DB.Database()
        self.records = self.db.get_top_records()
        self.bg = pygame.image.load(settings.resource_path("imgs/bg.webp"))

    def draw(self):
        """
        Отрисовка экрана таблицы рекордов. Выводит 21 рекорд, полученный от объекта  базы данных
        :return:
        """
        bg = self.bg.convert_alpha()
        transparency = 32
        bg.fill((0, 0, 0, transparency), special_flags=pygame.BLEND_RGBA_MULT)
        self.screen.blit(bg, bg.get_rect())

        # Рисуем заголовок
        title_font = pygame.font.Font(None, 70)
        title = title_font.render("Список локальных рекордов", True, TITLE)
        title_rect = title.get_rect(center=(self.screen.get_width() // 2, 100))
        self.screen.blit(title, title_rect)

        # Подсказка
        hint = self.font.render("Нажмите Enter для выхода в меню", True, TITLE)
        hint_rect = hint.get_rect(center=(self.screen.get_width() // 2, self.screen.get_width() - 600))
        self.screen.blit(hint, hint_rect)

        # Рекорды
        records = self.db.get_top_records()

        for i in range(21):
            if i < len(records):
                name = self.records_font.render(f"{i + 1} {' ' * 5} {records[i]['name']}", True, TITLE)
                name_rect = name.get_rect(topleft=(self.screen.get_width() // 3, 200 + (20 * i)))
                self.screen.blit(name, name_rect)

                time = self.records_font.render(f"{records[i]['time']}", True, TITLE)
                time_rect = time.get_rect(topleft=(self.screen.get_width() -
                                                   self.screen.get_width() // 3, 200 + (20 * i)))
                self.screen.blit(time, time_rect)

                diff = self.records_font.render(f"{records[i]['diff']}", True, TITLE)
                diff_rect = diff.get_rect(topleft=(self.screen.get_width() -
                                                   self.screen.get_width() // 4, 200 + (20 * i)))
                self.screen.blit(diff, diff_rect)
            else:
                name = self.records_font.render(f"{i + 1}", True, TITLE)
                name_rect = name.get_rect(topleft=(self.screen.get_width() // 3, 200 + (20 * i)))
                self.screen.blit(name, name_rect)
        pass

    def handle_event(self, event):
        """
        Слушает события управления и выходит в меню по нажатию на Enter
        :param event: Объект событий
        :return:
        """
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                # Когда нажали Enter, возвращаемся
                settings.CURRENT_SCREEN = "menu"
                return
