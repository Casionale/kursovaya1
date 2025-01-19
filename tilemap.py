import random
import pygame

from settings import resource_path


class TileMap:
    """
    Класс, создающий карту из тайлов.
    """
    def __init__(self, rows, cols, tile_size):
        """
        Конструктор. Генерирует карту тайлов.
        :param rows: Количество строк
        :param cols: Количество столбцов
        :param tile_size: Размер тайла (Квадрат)
        """
        self.rows = rows
        self.cols = cols
        self.tile_size = tile_size
        self.imgTiles = self.getImages()
        self.tiles = self.generate_tiles()

    def getImages(self):
        imgs = {
            'grass': [
                pygame.image.load(resource_path("imgs/tiles/grass (1).gif")),
                pygame.image.load(resource_path("imgs/tiles/grass (2).gif")),
                pygame.image.load(resource_path("imgs/tiles/grass (3).gif")),
                pygame.image.load(resource_path("imgs/tiles/grass (4).gif")),
                pygame.image.load(resource_path("imgs/tiles/grass (5).gif")),
                pygame.image.load(resource_path("imgs/tiles/grass (6).gif")),
                pygame.image.load(resource_path("imgs/tiles/grass (7).gif")),
                pygame.image.load(resource_path("imgs/tiles/grass (8).gif")),
                pygame.image.load(resource_path("imgs/tiles/grass (9).gif")),
                pygame.image.load(resource_path("imgs/tiles/grass (10).gif")),
                ],
            'sand': [
                pygame.image.load(resource_path("imgs/tiles/sand.gif")),
                pygame.image.load(resource_path("imgs/tiles/sand.png")),
                pygame.image.load(resource_path("imgs/tiles/sand (1).gif")),
                pygame.image.load(resource_path("imgs/tiles/sand (2).gif")),
            ],
            'stone': [
                pygame.image.load(resource_path("imgs/tiles/stone (1).gif")),
                pygame.image.load(resource_path("imgs/tiles/stone (2).gif")),
                pygame.image.load(resource_path("imgs/tiles/stone (3).gif")),
                pygame.image.load(resource_path("imgs/tiles/stone (4).gif")),
                pygame.image.load(resource_path("imgs/tiles/stone (5).gif")),
                pygame.image.load(resource_path("imgs/tiles/stone (6).gif")),
                pygame.image.load(resource_path("imgs/tiles/stone (7).gif")),
                pygame.image.load(resource_path("imgs/tiles/stone (8).gif")),
            ]
        }
        return imgs

    def generate_tiles(self):
        """
        Генерация тайлов с помощью рандома.
        :return: Список тайлов
        """
        tiles = []
        for row in range(self.rows):
            for col in range(self.cols):
                x = col * self.tile_size
                y = row * self.tile_size
                tile_type = random.choice(["grass", "stone", "sand"])
                tile_image = random.choice(self.imgTiles[tile_type])
                tiles.append((x, y, tile_image))
        return tiles

    def draw(self, screen, camera):
        """
        Отрисовка тайловой карты с эффектом дымки в зависимости от камеры.
        :param screen: Объект дисплея pygame
        :param camera: Объект камеры игры
        """
        screen_width, screen_height = screen.get_size()

        # Слой для дымки
        fog_surface = pygame.Surface((self.tile_size, self.tile_size), pygame.SRCALPHA)

        # Только видимые тайлы
        for x, y, tile_image in self.tiles:
            if (
                    x + self.tile_size > camera.x_offset
                    and x < camera.x_offset + screen_width
                    and y + self.tile_size > camera.y_offset
                    and y < camera.y_offset + screen_height
            ):
                screen_x = x - camera.x_offset
                screen_y = y - camera.y_offset

                # Масштабируем изображение
                scaled_image = pygame.transform.scale(tile_image, (self.tile_size, self.tile_size))

                # Тайл
                screen.blit(scaled_image, (screen_x, screen_y))

                # Применяем эффект дымки
                fog_intensity = 100  # Уровень прозрачности (0 - прозрачный, 255 - непрозрачный)
                fog_surface.fill((0, 0, 0, fog_intensity))  # Слой дымки чёрным с прозрачностью
                screen.blit(fog_surface, (screen_x, screen_y))
