import math
import random

import pygame
from math import sqrt
from settings import *


class GameObject:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
        self.pulse = 0  # Для анимации пульсации

    def draw(self, screen, camera):
        # Координаты объекта с учетом камеры
        screen_x = self.x - camera.x_offset
        screen_y = self.y - camera.y_offset

        # Анимация пульсации
        pulse_effect = 3 * math.sin(pygame.time.get_ticks() / 500)
        pygame.draw.circle(screen, self.color, (int(screen_x), int(screen_y)), int(self.size + pulse_effect))

        # Проверяем, находится ли объект в пределах видимого окна
        if -self.size < screen_x < WINDOW_WIDTH + self.size and -self.size < screen_y < WINDOW_HEIGHT + self.size:
            pygame.draw.circle(screen, OBJECT_COLOR, (screen_x, screen_y), self.size)

    def collides_with(self, player):
        # Проверка коллизии с игроком
        distance = sqrt((self.x - player.x) ** 2 + (self.y - player.y) ** 2)
        return distance < player.radius + self.size

class Obstacle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, screen, camera):
        # Отрисовка с учётом камеры
        screen_x = self.x - camera.x_offset
        screen_y = self.y - camera.y_offset
        pygame.draw.rect(screen, (139, 69, 19), (screen_x, screen_y, self.width, self.height))

    def collides_with(self, player):
        # Проверка коллизии с игроком
        return (
            player.x + player.radius > self.x and
            player.x - player.radius < self.x + self.width and
            player.y + player.radius > self.y and
            player.y - player.radius < self.y + self.height
        )

class MovingObject(GameObject):
    def __init__(self, x, y, size, speed, direction):
        super().__init__(x, y, size)
        self.color = 'lightBlue'
        self.speed = speed
        self.direction = direction  # (dx, dy), направление движения

    def draw(self, screen, camera):
        self.update(self.speed/10)
        super().draw(screen, camera)

    def update(self, dt):
        # Обновляем позицию объекта
        self.x += self.speed * self.direction[0] * dt
        self.y += self.speed * self.direction[1] * dt

        # Отражение от границ карты
        if self.x <= 0 or self.x >= MAP_WIDTH:
            self.direction = (-self.direction[0], self.direction[1])
        if self.y <= 0 or self.y >= MAP_HEIGHT:
            self.direction = (self.direction[0], -self.direction[1])

class Square_interactive_objects:
    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color

    def draw(self, screen, camera):
        # Отрисовка с учётом камеры
        screen_x = self.x - camera.x_offset
        screen_y = self.y - camera.y_offset
        pygame.draw.rect(screen, (self.color), (screen_x, screen_y, self.size, self.size))

    def collides_with(self, player):
        # Проверка коллизии с игроком
        return (
                player.x + player.radius > self.x and
                player.x - player.radius < self.x + self.size and
                player.y + player.radius > self.y and
                player.y - player.radius < self.y + self.size
        )

    def apply_effect(self, player):
        pass

class Bonus(Square_interactive_objects):
    def apply_effect(self, player):
        player.radius += 10  # Увеличение радиуса игрока

class Trap(Square_interactive_objects):
    def apply_effect(self, player):
        player.radius -= 5  # Уменьшение радиуса игрока
