# Размеры окна
import pygame

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
COLLECT_SOUND = pygame.mixer.Sound("sounds/collect.wav")
SHRINK_SOUND = pygame.mixer.Sound("sounds/shrink.wav")
BONUS_SOUND = pygame.mixer.Sound("sounds/bonus.mp3")
LEVEL_UP_SOUND = pygame.mixer.Sound("sounds/LevelUp.mp3")
VICTORY_SOUND = pygame.mixer.Sound("sounds/Victory.mp3")
GAME_OVER_SOUND = pygame.mixer.Sound("sounds/LevelUp.mp3")
ENDING_SOUND = pygame.mixer.Sound("sounds/ENDING.mp3")
GAME_SOUND = pygame.mixer.Sound("sounds/Blade_DS_Campaign.ogg")
MENU_SOUND = pygame.mixer.Sound("sounds/MENU.mp3")
CREDITS_SOUND = pygame.mixer.Sound("sounds/Dark-Knight-chosic.mp3")

#ТЕКУЩИЙ ЭКРАН
CURRENT_SCREEN = ""

#ВРЕМЯ ИГРЫ
GAME_TIME = 0
