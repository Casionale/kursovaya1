import settings
from camera import Camera
from map import GameMap
from player import Player
from input_screen import InputScreen
from tilemap import TileMap
from ui import GameUI
from settings import *

class Game:
    screen = None
    current_level = None
    max_level = 1
    running = False
    game_timer = 0
    game_map = None

    def __init__(self, screen):
        # Инициализация объектов
        self.screen = screen
        self.current_level = 1
        self.clock = pygame.time.Clock()
        self.player = Player(20)
        self.camera = Camera(self.player)
        self.ui = GameUI()
        # Инициализация тайловой карты
        self.tilemap = TileMap(100, 100, 50)


    def to_game(self):

        GAME_SOUND.play(loops=10)
        # Игровой цикл
        running = True
        self.game_timer = 0  # Счётчик времени
        self.clock = pygame.time.Clock()
        self.current_level = 1

        self.game_map = GameMap(num_objects=30 + self.current_level * 5, difficulty=self.current_level)

        while running:
            dt = self.clock.tick(60) / 1000  # Дельта времени в секундах для таймера
            self.game_timer += dt

            # Очистка экрана
            self.screen.fill((0, 0, 0))

            # Рисуем тайлы карты
            self.tilemap.draw(self.screen, self.camera)

            # Обновляем и рисуем карту объектов
            self.game_map.update(self.player)
            self.game_map.draw(self.screen, self.camera)

            # Рисуем игрока
            self.player.draw(self.screen, self.camera)

            # Рисуем UI
            self.ui.draw(self.screen, self.player, self.game_timer)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Обновление состояния
            self.player.update()
            self.camera.update()
            self.game_map.update(self.player)

            # Условие победы
            if self.player.radius >= 50:

                if self.current_level == self.max_level:
                    GAME_SOUND.fadeout(1)
                    VICTORY_SOUND.play()
                    self.show_transition_screen(f"Финальный уровень пройден!")
                    self.show_transition_screen("Вы прошли игру!", f"Ваше время {round(self.game_timer, 2)} сек")
                    MENU_SOUND.play(loops=10)
                    settings.CURRENT_SCREEN = "input"
                    settings.GAME_TIME = round(self.game_timer, 2)
                    self.running = False
                    return

                self.show_transition_screen(f"Уровень {self.current_level} пройден!")
                self.load_next_level()

            # Условие поражения
            if self.player.radius <= 5:
                GAME_SOUND.fadeout(1)
                GAME_OVER_SOUND.play()
                self.show_transition_screen("Вы проиграли!")
                MENU_SOUND.play(loops=10)
                settings.CURRENT_SCREEN = "menu"
                self.running = False

            pygame.display.flip()
            self.clock.tick(FPS)

    def show_transition_screen(self, message, submessage=''):
        self.screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 74)
        text = font.render(message, True, (255, 255, 255))
        text_rect = text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        self.screen.blit(text, text_rect)

        if submessage != '':
            font = pygame.font.Font(None, 34)
            subtext = font.render(submessage, True, (255, 255, 255))
            subtext_rect = subtext.get_rect(center=(WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) + 100))
            self.screen.blit(subtext, subtext_rect)

        pygame.display.flip()
        pygame.time.delay(2000)  # Задержка в 2 секунды перед переходом

    def load_next_level(self):
        self.current_level += 1
            #pygame.quit()  # ЗАВЕРШЕНИЕ ИГРЫ!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            #sys.exit()

        print(f"Переход на уровень {self.current_level}")
        self.game_map = GameMap(num_objects=20 + self.current_level * 5, difficulty=self.current_level)
        self.player = Player(x=MAP_WIDTH // 2, y=MAP_HEIGHT // 2, radius=20)  # Обновляем игрока
        self.camera = Camera(self.player)
        self.camera.update()
        LEVEL_UP_SOUND.play()