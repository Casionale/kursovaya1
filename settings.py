# Размеры окна
import pygame

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

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
COLLECT_SOUND = pygame.mixer.Sound("sounds/collect.wav")
SHRINK_SOUND = pygame.mixer.Sound("sounds/shrink.wav")

# Условия победы