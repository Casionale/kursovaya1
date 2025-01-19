import random
from settings import *
from objects import GameObject, Obstacle, MovingObject, Bonus


class GameMap:
    """
    Класс GameMap генерирует карту и объекты для создания нового уровня
    """
    def __init__(self, num_objects, difficulty=1):
        """
        Конструктор
        :param num_objects: Количество врагов на уровне
        :param difficulty: Сложность (количество уровней в игре)
        """
        self.objects = []
        self.obstacles = []
        self.difficulty = difficulty
        self.generate_objects(num_objects, self.difficulty)
        self.obstacles = self.generate_obstacles(random.randint(30 + 5 * difficulty, 100))
        self.bonuses = self.generate_bonuses(2)
        pass

    def update(self, player):
        """
        Проверяет коллизии объектов и игрока. Увеличивает или уменьшает размер игрока, применяет бонусы и удаляет
        объекты
        :param player: объект игрока
        :return:
        """
        for obj in self.objects[:]:
            if obj.collides_with(player):
                if player.radius > obj.size:  # Игрок поглощает объект
                    player.grow(1)  # Увеличение радиуса
                    COLLECT_SOUND.play()
                    self.objects.remove(obj)
                else:  # Игрок сталкивается с более крупным объектом
                    player.shrink(1)  # Уменьшение радиуса



        # Проверяем столкновение с препятствиями
        for obstacle in self.obstacles:
            if obstacle.collides_with(player):
                # Отталкиваем игрока от препятствия
                if player.x < obstacle.x:
                    player.x -= player.speed
                elif player.x > obstacle.x + obstacle.width:
                    player.x += player.speed
                if player.y < obstacle.y:
                    player.y -= player.speed
                elif player.y > obstacle.y + obstacle.height:
                    player.y += player.speed
                SHRINK_SOUND.play()

        #Столкновение с бонусом
        for bonus in self.bonuses:
            if bonus.collides_with(player):
                print('Коллизия с бонусом')
                bonus.apply_effect(player)
                BONUS_SOUND.play()
                self.bonuses.remove(bonus)

    def draw(self, screen, camera):
        """
        Вызывает метод отрисовки объекта, но только если он находится в области камеры
        :param screen: Объект pygame.display
        :param camera: Объект класса Camera - камера игры
        :return:
        """
        for obstacle in self.obstacles:
            obstacle.draw(screen, camera)
        for obj in self.objects:
            obj.draw(screen, camera)
        for bonus in self.bonuses:
            bonus.draw(screen, camera)

    def generate_objects(self, num_objects, difficulty):
        """
        Собственно генерация врагов. С некоторым шансом создаёт движущихся врагов
        :param num_objects: Количество врагов
        :param difficulty: Сложность уровня
        :return:Список врагов
        """
        for _ in range(num_objects):
            size = random.randint(5 + 3 * difficulty, 30 + 2 * difficulty) + self.difficulty
            x = random.randint(0, MAP_WIDTH)
            y = random.randint(0, MAP_HEIGHT)
            if random.random() < 0.2 * self.difficulty:  # Вероятность появления движущихся объектов
                speed = random.randint(1, 3)
                direction = (random.choice([-1, 1]), random.choice([-1, 1]))
                self.objects.append(MovingObject(x, y, size, speed, direction))
            else:
                self.objects.append(GameObject(x, y, size))

    def generate_obstacles(self, count):
        """
        Метод генерации препятствий на уровне
        :param count: Количество препятствий
        :return:Список препятствий
        """
        obstacles = []
        for _ in range(count):
            x = random.randint(0, MAP_WIDTH)
            y = random.randint(0, MAP_HEIGHT)
            width = random.randint(20, 50)
            height = random.randint(20, 50)
            obstacles.append(Obstacle(x, y, width, height))
        return obstacles

    def generate_bonuses(self, count):
        """
        Метод генерации бонусов
        :param count: Количество бонусов
        :return:Список бонусов
        """
        bonuses = []
        for _ in range(count):
            x = random.randint(0, MAP_WIDTH)
            y = random.randint(0, MAP_HEIGHT)
            bonuses.append(Bonus(x, y, 10, 'yellow'))
        return bonuses
