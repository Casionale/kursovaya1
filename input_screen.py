import pygame

import settings

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

class InputScreen:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 50)
        self.input_box = pygame.Rect((self.screen.get_width() // 2 - 150, 250), (300, 50))
        self.text = ""
        self.active = True

    def draw(self):
        self.screen.fill(BLACK)

        # Рисуем заголовок
        title_font = pygame.font.Font(None, 70)
        title = title_font.render("Введите имя", True, WHITE)
        title_rect = title.get_rect(center=(self.screen.get_width() // 2, 150))
        self.screen.blit(title, title_rect)

        # Рисуем поле ввода
        pygame.draw.rect(self.screen, GRAY, self.input_box)
        text_surface = self.font.render(self.text, True, BLACK)
        self.screen.blit(text_surface, (self.input_box.x + 10, self.input_box.y + 10))

        # Подсказка
        hint = self.font.render("Нажмите Enter для продолжения", True, WHITE)
        hint_rect = hint.get_rect(center=(self.screen.get_width() // 2, 350))
        self.screen.blit(hint, hint_rect)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_RETURN:
                # Когда нажали Enter, возвращаем текст
                settings.CURRENT_SCREEN = "menu"
                return self.text.strip()
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode
        return None
