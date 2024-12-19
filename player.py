import pygame
from settings import *

class Player:
    def __init__(self, radius, x=MAP_WIDTH // 2, y=MAP_HEIGHT // 2):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = PLAYER_SPEED
        self.max_size = 50  # Условие победы
        self.min_size = 5   # Условие поражения

    def update(self):
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

    def grow(self, amount):
        self.radius += amount

    def shrink(self, amount):
        self.radius -= amount
        if self.radius < self.min_size:
            self.radius = self.min_size

    def check_game_state(self):
        if self.radius >= self.max_size:
            return "win"
        elif self.radius <= self.min_size:
            return "lose"
        return "continue"

    def draw(self, screen, camera):
        screen_x = self.x - camera.x_offset
        screen_y = self.y - camera.y_offset
        pygame.draw.circle(screen, PLAYER_COLOR, (screen_x, screen_y), self.radius)
