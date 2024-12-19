import pygame

class GameUI:
    def __init__(self, font_size=24):
        self.font = pygame.font.SysFont("Arial", font_size)

    def draw(self, screen, player, timer):
        # Отображение размера игрока
        size_text = self.font.render(f"Size: {player.radius}", True, (255, 255, 255))
        screen.blit(size_text, (10, 10))

        # Отображение таймера
        timer_text = self.font.render(f"Time: {timer:.1f} sec", True, (255, 255, 255))
        screen.blit(timer_text, (10, 40))
