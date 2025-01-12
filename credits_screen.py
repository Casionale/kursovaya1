import pygame
import settings

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class CreditsScreen:
    def __init__(self, screen):
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
            "Главный и не повторимый тестировщик:",
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
            "Фоновое изображение:",
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
        self.screen.fill(BLACK)

        # Рисуем строки с учетом их текущей позиции
        for i, text in enumerate(self.credits):
            rendered_text = self.font.render(text, True, WHITE)
            text_rect = rendered_text.get_rect(center=(self.screen.get_width() // 2, self.y_positions[i]))
            self.screen.blit(rendered_text, text_rect)

    def update(self):
        self.freeze_fps += 1

        if self.freeze_fps % 10 == 0:

            for i in range(len(self.y_positions)):
                self.y_positions[i] -= self.speed

        if self.y_positions[-1] < 0:
            settings.CURRENT_SCREEN = "menu"
            self.y_positions = [self.screen.get_height() + i * 50 for i in range(len(self.credits))]
            settings.CREDITS_SOUND.fadeout(1)
            settings.MENU_SOUND.play()

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                settings.CURRENT_SCREEN = "menu"
                self.y_positions = [self.screen.get_height() + i * 50 for i in range(len(self.credits))]
                settings.CREDITS_SOUND.fadeout(1)
                settings.MENU_SOUND.play()

