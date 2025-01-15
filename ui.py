import pygame

class GameUI:
    """
    Класс UI игры. Выводит таймер и  размер игрока
    """
    def __init__(self, font_size=24):
        """
        Конструктор задаёт шрифт для элементов UI
        :param font_size: Размер шрифта, по-умолчанию 24
        """
        self.font = pygame.font.SysFont("Arial", font_size)

    def draw(self, screen, player, timer):
        """
        Отрисовка элементов UI
        :param screen: Объект дисплея pygame
        :param player: Объект игрока
        :param timer: Время игрового таймера
        :return:
        """
        # Отображение размера игрока
        size_text = self.font.render(f"Размер: {player.radius}", True, (255, 255, 255))
        screen.blit(size_text, (10, 10))

        # Отображение таймера
        timer_text = self.font.render(f"Время: {timer:.1f} сек", True, (255, 255, 255))
        screen.blit(timer_text, (10, 40))
