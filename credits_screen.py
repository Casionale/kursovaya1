import pygame
import settings

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class CreditsScreen:
    """
    Класс окна титров. Выводит на экран титры игры и выходит в меню.
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
        self.font = pygame.font.Font(None, 40)
        self.credits = [
            "Спасибо за игру!",
            "",
            "",
            "Разработчик:",
            "Багров Кирилл Юрьевич",
            "",
            "",
            "Тестирование:",
            "Багров Кирилл Юрьевич",
            "",
            "",
            "Главный и неповторимый тестировщик:",
            "Коротаев Кирилл Андреевич",
            "",
            "",
            "Коллеги по работе, принимавшие участие в",
            "тестировании ранних версий:",
            "Попов Дмитрий Андреевич",
            "Скворцов Александр Викторович",
            "",
            "",
            "Геймдизайн:",
            "Багров Кирилл Юрьевич",
            "",
            "Фоновое изображение и спрайты:",
            "DALL-E",
            "",
            "",
            "Музыка:",
            "Soundsnap",
            "FreeSoundEffects.net",
            "chosic.com",
            "",
            "",
            "Отдельная благодарность",
            "Друзьям и коллегам, которые поддерживали",
            "меня весь этот долгий и упорный путь",
            "в прошлые и будущие годы:",
            "Кузнецов Михаил",
            "Ширшов Илья",
            "Дружин Кирилл",
            "Никита Толкачев",
            "и другие...",
            "",
            "",
            "Специально для",
            "Курсовой работы",
            "САФУ, 2025",
            "",
            "СПАСИБО ЗА ИГРУ!",
        ]

        self.y_positions = [self.screen.get_height() + i * 50 for i in range(len(self.credits))]
        self.speed = 1  # Скорость движения текста вверх
        self.freeze_fps = 0

    def draw(self):
        """
        Отрисовывает титры в правильном месте
        :return:
        """
        self.screen.fill(BLACK)

        # Рисуем строки с учетом их текущей позиции
        for i, text in enumerate(self.credits):
            rendered_text = self.font.render(text, True, WHITE)
            text_rect = rendered_text.get_rect(center=(self.screen.get_width() // 2, self.y_positions[i]))
            self.screen.blit(rendered_text, text_rect)

    def update(self):
        """
        Метод поднимает титры с заданной скоростью (пиксель в несколько кадров),
        следит чтобы при завершении титров открылось меню
        :return:
        """
        self.freeze_fps += 1

        if self.freeze_fps % 1 == 0: # Было замедление титров, сейчас нет

            for i in range(len(self.y_positions)):
                self.y_positions[i] -= self.speed

        if self.y_positions[-1] < 0:
            settings.CURRENT_SCREEN = "menu"
            self.y_positions = [self.screen.get_height() + i * 50 for i in range(len(self.credits))]
            settings.CREDITS_SOUND.fadeout(1)
            settings.MENU_SOUND.play()

    def handle_event(self, event):
        """
        Слушает события управления и выходит в меню по нажатию на Enter
        :param event: Объект событий
        :return:
        """
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                settings.CURRENT_SCREEN = "menu"
                self.y_positions = [self.screen.get_height() + i * 50 for i in range(len(self.credits))]
                settings.CREDITS_SOUND.fadeout(1)
                settings.MENU_SOUND.play()
