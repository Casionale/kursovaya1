import sys

import pygame
from settings import *
from player import Player
from map import GameMap
from camera import Camera
from ui import GameUI
from tilemap import TileMap

pygame.init()




# Настройка окна
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Katamari 2D")

# Инициализация объектов
clock = pygame.time.Clock()
player = Player(20)
camera = Camera(player)
ui = GameUI()


# Инициализация тайловой карты
tilemap = TileMap(100, 100, 50)


# Игровой цикл
running = True
game_timer = 0  # Счётчик времени
clock = pygame.time.Clock()

current_level = 1
max_level = 5

def load_next_level():
    global game_map, player, current_level, camera

    current_level += 1
    if current_level > max_level:
        print("Поздравляем, вы прошли игру!")
        pygame.quit()
        sys.exit()

    print(f"Переход на уровень {current_level}")
    game_map = GameMap(num_objects=20 + current_level * 5, difficulty=current_level)
    player = Player(x=MAP_WIDTH // 2, y=MAP_HEIGHT // 2, radius=20)  # Обновляем игрока
    camera = Camera(player)
    camera.update()


def show_transition_screen(message):
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 74)
    text = font.render(message, True, (255, 255, 255))
    text_rect = text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
    screen.blit(text, text_rect)
    pygame.display.flip()
    pygame.time.delay(2000)  # Задержка в 2 секунды перед переходом

game_map = GameMap(num_objects=30 + current_level * 5, difficulty=current_level)

while running:
    dt = clock.tick(60) / 1000  # Дельта времени в секундах
    game_timer += dt

    # Очистка экрана
    screen.fill((0, 0, 0))

    # Рисуем тайлы карты
    tilemap.draw(screen, camera)

    # Обновляем и рисуем карту объектов
    game_map.update(player)
    game_map.draw(screen, camera)

    # Рисуем игрока
    player.draw(screen, camera)

    # Рисуем UI
    ui.draw(screen, player, game_timer)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Обновление состояния
    player.update()
    camera.update()
    game_map.update(player)

    # Условие победы
    if player.radius >= 50:
        show_transition_screen(f"Уровень {current_level} пройден!")
        load_next_level()

    # Условие поражения
    if player.radius <= 5:
        show_transition_screen("Вы проиграли!")
        running = False

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()