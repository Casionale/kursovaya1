import settings
from camera import Camera
from map import GameMap
from player import Player
from input_screen import InputScreen
from tilemap import TileMap
from ui import GameUI
from settings import *


class Game:
    """
    Класс самого игрового процесса

    Attributes
    screen : pygame.screen
        Объект экрана
    """
    screen = None
    current_level = None
    max_level = 5
    running = False
    game_timer = 0
    game_map = None

    def __init__(self, screen):
        """
        Конструктор
        :param screen: объект экрана
        """
        # Инициализация объектов
        self.screen = screen
        self.current_level = 1
        self.clock = pygame.time.Clock()
        self.player = Player(20)
        self.camera = Camera(self.player)
        self.ui = GameUI()
        # Инициализация тайловой карты
        self.tilemap = TileMap(100, 100, 50)
        w, h = pygame.display.get_surface().get_size()
        self.defeat = pygame.transform.scale(pygame.image.load(settings.resource_path("imgs/defeat.png")),
                                             (w, h))

        self.victory = pygame.transform.scale(pygame.image.load(settings.resource_path("imgs/victory.png")),
                                              (w, h))

    def to_game(self, max_level=5):
        """
        Класс запуска игрового цикла, запускает таймер, следит за состоянием игрового процесса
        :param max_level: Количество уровней игры, по-умолчанию 5
        :return:
        """
        self.max_level = max_level

        GAME_SOUND.play(loops=10)
        # Игровой цикл
        running = True
        self.game_timer = 0  # Счётчик времени
        self.clock = pygame.time.Clock()
        self.current_level = 1

        self.game_map = GameMap(num_objects=30 + self.current_level * 5, difficulty=self.current_level)

        while running:
            if settings.CURRENT_SCREEN == "menu":
                return
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
                    self.show_transition_screen(f"Финальный уровень пройден!", bg='victory')
                    self.show_transition_screen("Вы прошли игру!",
                                                f"Ваше время {round(self.game_timer, 2)} сек", bg='victory')
                    MENU_SOUND.play(loops=10)
                    settings.CURRENT_SCREEN = "input"
                    settings.GAME_TIME = round(self.game_timer, 2)
                    settings.GAME_DIFF = self.max_level
                    self.running = False
                    return

                self.show_transition_screen(f"Уровень {self.current_level} пройден!", bg='victory')
                self.load_next_level()

            # Условие поражения
            if self.player.radius <= 5:
                GAME_SOUND.fadeout(1)
                GAME_OVER_SOUND.play()
                self.show_transition_screen("Вы проиграли!", bg='defeat')
                MENU_SOUND.play(loops=10)
                settings.CURRENT_SCREEN = "menu"
                self.running = False
                return

            # После всей основной отрисовки затемнение от уровня:
            dark_overlay = pygame.Surface(self.screen.get_size())
            dark_overlay.set_alpha(0 + self.current_level * 10)
            dark_overlay.fill((0, 0, 0))
            self.screen.blit(dark_overlay, (0, 0))

            pygame.display.flip()
            self.clock.tick(FPS)
            #print(self.clock.get_fps())

    def show_transition_screen(self, message, submessage='', bg='default'):
        """
        Метод создаёт экран сообщения между игровыми 'сценами'
        :param message: Сообщение окна
        :param submessage: Подсообщение окна меньшего размера
        :param bg: Выбор фонового изображения:
            default: чёрный экран
            victory: изображение победы
            defeat: изображение проигрыша
        :return:
        """
        if bg == 'default':
            self.screen.fill((0, 0, 0))
            COLOR = (255, 255, 255)
        if bg == 'victory':
            self.screen.blit(self.victory, self.victory.get_rect())
            COLOR = (0, 0, 0)
        if bg == 'defeat':
            self.screen.blit(self.defeat, self.defeat.get_rect())
            COLOR = (255, 255, 255)

        font = pygame.font.Font(None, 74)
        text = font.render(message, True, COLOR)
        text_rect = text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        self.screen.blit(text, text_rect)

        if submessage != '':
            font = pygame.font.Font(None, 34)
            subtext = font.render(submessage, True, COLOR)
            subtext_rect = subtext.get_rect(center=(WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) + 100))
            self.screen.blit(subtext, subtext_rect)

        pygame.display.flip()
        pygame.time.delay(2000)  # Задержка в 2 секунды перед переходом

    def load_next_level(self):
        """
        Метод для перехода на следующий уровень, увеличивает текущий уровень на 1
        :return:
        """
        self.current_level += 1
        print(f"Переход на уровень {self.current_level}")
        self.game_map = GameMap(num_objects=20 + self.current_level * 5, difficulty=self.current_level)
        self.player = Player(x=MAP_WIDTH // 2, y=MAP_HEIGHT // 2, radius=20)  # Обновляем игрока
        self.camera = Camera(self.player)
        self.camera.update()
        LEVEL_UP_SOUND.play()
