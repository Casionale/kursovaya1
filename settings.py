# Размеры окна
import os
import sys

import pygame

#Загрузка файлов для возможности внести в exe
def resource_path(relative_path):
    try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

# Размеры карты
MAP_WIDTH = 2000
MAP_HEIGHT = 2000

# Параметры игрока
PLAYER_RADIUS = 20
PLAYER_SPEED = 5

# Параметры цвета
BG_COLOR = (30, 30, 30)
PLAYER_COLOR = (50, 150, 255)
OBJECT_COLOR = (200, 50, 50)

# FPS
FPS = 60

# SOUND
pygame.mixer.init()
COLLECT_SOUND = pygame.mixer.Sound(resource_path("sounds/collect.wav"))
SHRINK_SOUND = pygame.mixer.Sound(resource_path("sounds/shrink.wav"))
BONUS_SOUND = pygame.mixer.Sound(resource_path("sounds/bonus.mp3"))
LEVEL_UP_SOUND = pygame.mixer.Sound(resource_path("sounds/LevelUp.mp3"))
VICTORY_SOUND = pygame.mixer.Sound(resource_path("sounds/Victory.mp3"))
GAME_OVER_SOUND = pygame.mixer.Sound(resource_path("sounds/LevelUp.mp3"))
ENDING_SOUND = pygame.mixer.Sound(resource_path("sounds/ENDING.mp3"))
GAME_SOUND = pygame.mixer.Sound(resource_path("sounds/Blade_DS_Campaign.ogg"))
MENU_SOUND = pygame.mixer.Sound(resource_path("sounds/MENU.mp3"))
CREDITS_SOUND = pygame.mixer.Sound(resource_path("sounds/Dark-Knight-chosic.mp3"))

# ТЕКУЩИЙ ЭКРАН
CURRENT_SCREEN = ""

# ВРЕМЯ ИГРЫ
GAME_TIME = 0
# СЛОЖНОСТЬ УРОВНЯ
GAME_DIFF = None

# СПРАЙТЫ
SPRITE_PLAYER = pygame.image.load(resource_path("imgs/Шар_03.png"))
SPRITE_ENEMY_1 = pygame.image.load(resource_path("imgs/Шар_05.png"))
SPRITE_ENEMY_2 = pygame.image.load(resource_path("imgs/Шар_07.png"))
SPRITE_ENEMY_3 = pygame.image.load(resource_path("imgs/Шар_09.png"))
SPRITE_ENEMY_4 = pygame.image.load(resource_path("imgs/Шар_11.png"))
SPRITE_ENEMY_5 = pygame.image.load(resource_path("imgs/Шар_13.png"))
SPRITE_ENEMY_6 = pygame.image.load(resource_path("imgs/Шар_21.png"))
SPRITE_ENEMY_7 = pygame.image.load(resource_path("imgs/Шар_22.png"))

ENEMY_SPRITES = [SPRITE_ENEMY_1, SPRITE_ENEMY_2, SPRITE_ENEMY_3, SPRITE_ENEMY_4,
                 SPRITE_ENEMY_5, SPRITE_ENEMY_6, SPRITE_ENEMY_7]
