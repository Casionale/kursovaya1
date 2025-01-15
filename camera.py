from settings import *


class Camera:
    """
    Класс Camera используется для правильного отображение игрока в центре экрана

    Attributes
    ----------
    player : Player
        Объект игрока
    Methods
    ------
    update()
        Центрирует игрока в окне и ограничивает камеру границей карты
    """

    def __init__(self, player):
        """
        Конкструктор
        :param player: Объект игрока
        """
        self.x_offset = 0
        self.y_offset = 0
        self.player = player

    def update(self):
        """
        Центрирует игрока в окне и ограничивает камеру границей карты
        :return:
        """
        # Центрируем игрока в окне
        self.x_offset = self.player.x - WINDOW_WIDTH // 2
        self.y_offset = self.player.y - WINDOW_HEIGHT // 2

        # Ограничиваем камеру границами карты
        self.x_offset = max(0, min(self.x_offset, MAP_WIDTH - WINDOW_WIDTH))
        self.y_offset = max(0, min(self.y_offset, MAP_HEIGHT - WINDOW_HEIGHT))
