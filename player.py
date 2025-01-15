import pygame

import settings
from settings import *

class Player:
    """
    Класс игрока.
    """
    def __init__(self, radius, x=MAP_WIDTH // 2, y=MAP_HEIGHT // 2):
        """
        Конструктор. Создаёт игрока, задаёт размер и спавнит посреди карты.
        :param radius: Размер игрока
        :param x: Координата X, по-умолчанию середина карты
        :param y: Координата Y, по-умолчанию середина карты
        """
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = PLAYER_SPEED
        self.max_size = 50  # Условие победы
        self.min_size = 5   # Условие поражения

    def update(self):
        """
        Класс обновления позиции игрока, а так же выхода из игры в меню при нажатии Esc
        :return:
        """
        keys = pygame.key.get_pressed()
        move_x = 0
        move_y = 0

        if keys[pygame.K_w]:
            move_y = -self.speed
        if keys[pygame.K_s]:
            move_y = self.speed
        if keys[pygame.K_a]:
            move_x = -self.speed
        if keys[pygame.K_d]:
            move_x = self.speed

        # Обновляем позицию
        self.x += move_x
        self.y += move_y


        if keys[pygame.K_ESCAPE]:
            settings.CURRENT_SCREEN = "menu"
            settings.GAME_SOUND.fadeout(1)
            settings.MENU_SOUND.play()

    def grow(self, amount):
        """
        Метод увеличения радиуса игрока
        :param amount: На сколько увеличить радиус игрока
        :return:
        """
        self.radius += amount

    def shrink(self, amount):
        """
        Уменьшение радиуса игрока
        :param amount: Насколько уменьшить радиус игрока
        :return:
        """
        self.radius -= amount
        if self.radius < self.min_size:
            self.radius = self.min_size


    def draw(self, screen, camera):
        """
        Отрисовка игрока в зависимости от положения  и камеры
        :param screen: Объект дисплея pygame
        :param camera: Объект камеры игрока
        :return:
        """
        screen_x = self.x - camera.x_offset
        screen_y = self.y - camera.y_offset
        # Cпрайт  в соответствии с его радиусом
        scaled_sprite = pygame.transform.scale(settings.SPRITE_PLAYER, (self.radius * 2, self.radius * 2))
        sprite_rect = scaled_sprite.get_rect(center=(screen_x, screen_y))
        screen.blit(scaled_sprite, sprite_rect)

