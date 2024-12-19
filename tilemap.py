import random

import pygame


class TileMap:
    def __init__(self, rows, cols, tile_size):
        self.rows = rows
        self.cols = cols
        self.tile_size = tile_size
        self.tiles = self.generate_tiles()

    def generate_tiles(self):
        tiles = []
        for row in range(self.rows):
            for col in range(self.cols):
                x = col * self.tile_size
                y = row * self.tile_size
                tile_type = random.choice(["grass", "stone", "sand"])
                tiles.append((x, y, tile_type))
        return tiles

    def draw(self, screen, camera):
        screen_width, screen_height = screen.get_size()

        # Отображаем только видимые тайлы
        for x, y, tile_type in self.tiles:
            if (
                x + self.tile_size > camera.x_offset
                and x < camera.x_offset + screen_width
                and y + self.tile_size > camera.y_offset
                and y < camera.y_offset + screen_height
            ):
                screen_x = x - camera.x_offset
                screen_y = y - camera.y_offset

                color = (34, 139, 34) if tile_type == "grass" else (169, 169, 169) if tile_type == "stone" else (210, 180, 140)
                pygame.draw.rect(screen, color, (screen_x, screen_y, self.tile_size, self.tile_size))
