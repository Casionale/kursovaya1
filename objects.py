import math
import random
from math import sqrt
import settings
from settings import *


class GameObject:
    """
    Класс объектов статичных врагов
    """
    def __init__(self, x, y, size):
        """
        Конструктор. Создаёт объект врага
        :param x: Координата X
        :param y: Координата y
        :param size: Размер объекта
        """
        self.x = x
        self.y = y
        self.size = size
        self.color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
        self.pulse = 0  # Для анимации пульсации
        self.sprite = settings.ENEMY_SPRITES[random.randint(0, len(settings.ENEMY_SPRITES)-1)]
        pass

    def draw(self, screen, camera):
        """
        Отрисовка объекта, учитывая камеру
        :param screen: Объект дисплея pygame
        :param camera: Объект камеры игры
        :return:
        """
        # Координаты объекта с учетом камеры
        screen_x = self.x - camera.x_offset
        screen_y = self.y - camera.y_offset

        # Анимация пульсации
        pulse_effect = 3 * math.sin(pygame.time.get_ticks() / 500)
        pygame.draw.circle(screen, self.color, (int(screen_x), int(screen_y)), int(self.size + pulse_effect))

        # Проверяем, находится ли объект в пределах видимого окна
        if -self.size < screen_x < WINDOW_WIDTH + self.size and -self.size < screen_y < WINDOW_HEIGHT + self.size:
            # Cпрайт  в соответствии с его радиусом
            scaled_sprite = pygame.transform.scale(self.sprite, (self.size * 2, self.size * 2))
            sprite_rect = scaled_sprite.get_rect(center=(screen_x, screen_y))
            screen.blit(scaled_sprite, sprite_rect)

    def collides_with(self, player):
        """
        Проверка коллизии врага с игроком
        :param player: Объект игрока
        :return:
        """
        # Проверка коллизии с игроком
        distance = sqrt((self.x - player.x) ** 2 + (self.y - player.y) ** 2)
        return distance < player.radius + self.size

class Obstacle:
    """
    Класс препятствия на карте
    """
    def __init__(self, x, y, width, height):
        """
        Конструктор, создающий препятствия
        :param x: Координата X
        :param y: Координата Y
        :param width: Ширина препятствия
        :param height: Высота препятствия
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, screen, camera):
        """
        Метод отрисоки препятствия с учётом камеры
        :param screen: Объект дисплее pygame
        :param camera: Объект камеры игры
        :return:
        """
        # Отрисовка с учётом камеры
        screen_x = self.x - camera.x_offset
        screen_y = self.y - camera.y_offset
        pygame.draw.rect(screen, (48, 24, 7), (screen_x, screen_y, self.width, self.height))

    def collides_with(self, player):
        """
        Метод проверки коллизии препятствия и игрока. Останавливает движение игрока в препятствие
        :param player: Объект игрока
        :return:True | False
        """
        # Проверка коллизии с игроком
        return (
            player.x + player.radius > self.x and
            player.x - player.radius < self.x + self.width and
            player.y + player.radius > self.y and
            player.y - player.radius < self.y + self.height
        )

class MovingObject(GameObject):
    """
    Класс движущегося врага в случайном направлении, наследован от GameObject
    """
    def __init__(self, x, y, size, speed, direction):
        """
        Конструктор, создаёт объект движущегося врага
        :param x: Координата X
        :param y: Координата Y
        :param size: Размер врага
        :param speed: Скорость врага
        :param direction: Направление движения
        """
        super().__init__(x, y, size)
        self.color = 'lightBlue'
        self.speed = speed
        self.direction = direction  # (dx, dy), направление движения

    def draw(self, screen, camera):
        """
        Метод отрисовки аналогичный родителю, однако учитывает скорость
        :param screen:
        :param camera:
        :return:
        """
        self.update(self.speed/10)
        super().draw(screen, camera)

    def update(self, dt):
        """
        Класс обновления позиции движущегося врага
        :param dt: Скорость врага (в кадр)
        :return:
        """
        # Обновляем позицию объекта
        self.x += self.speed * self.direction[0] * dt
        self.y += self.speed * self.direction[1] * dt

        # Отражение от границ карты
        if self.x <= 0 or self.x >= MAP_WIDTH:
            self.direction = (-self.direction[0], self.direction[1])
        if self.y <= 0 or self.y >= MAP_HEIGHT:
            self.direction = (self.direction[0], -self.direction[1])

class Square_interactive_objects:
    """
    Виртуальный класс для наследования объектов вроде бонусов или ловушек. Квадрат определённого цвета.
    """
    def __init__(self, x, y, size, color):
        """
        Конструктор. Создаёт объект.
        :param x: Координата Х
        :param y: Координата Y
        :param size: Размер квадрата
        :param color:
        """
        self.x = x
        self.y = y
        self.size = size
        self.color = color

    def draw(self, screen, camera):
        """
        Класс отрисовки объекта.
        :param screen: Объект дисплея pygame
        :param camera: Объект камеры игры
        :return:
        """
        # Отрисовка с учётом камеры
        screen_x = self.x - camera.x_offset
        screen_y = self.y - camera.y_offset
        pygame.draw.rect(screen, (self.color), (screen_x, screen_y, self.size, self.size))

    def collides_with(self, player):
        """
        Метод проверки коллизии игрока и объекта
        :param player: Объект игрока
        :return: True | False
        """
        # Проверка коллизии с игроком
        return (
                player.x + player.radius > self.x and
                player.x - player.radius < self.x + self.size and
                player.y + player.radius > self.y and
                player.y - player.radius < self.y + self.size
        )

    def apply_effect(self, player):
        """
        Метод, который выполняется при коллизии с игроком
        :param player: Объект игрока
        :return:
        """
        pass

class Bonus(Square_interactive_objects):
    """
    Класс бонуса. Добавляет размер игроку при взаимодействии
    """
    def apply_effect(self, player):
        """
        Метод увеличения размера игрока при взаимодействии
        :param player: Объект игрока
        :return:
        """
        player.radius += 10  # Увеличение радиуса игрока

class Trap(Square_interactive_objects):
    """
    Класс ловушки. Убавляет размер игроку при взаимодействии. Не используется
    """
    def apply_effect(self, player):
        """
        Метод уменьшения размера игрока при взаимодействии
        :param player: Объект игрока
        :return:
        """
        player.radius -= 5  # Уменьшение радиуса игрока
