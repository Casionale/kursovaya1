from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import unittest

# Создаем базу данных
Base = declarative_base()

class Record(Base):
    """
    Класс представляет таблицу records для хранения рекордов игрока
    """
    __tablename__ = 'records'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    time = Column(Float, nullable=False)
    diff = Column(Integer, nullable=False)

# Настройка подключения к базе данных
DATABASE_URL = "sqlite:///records.db"
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

class Database:
    """
    Класс Database занимается добавлением записей в БД с новыми рекордами и выдаёт топ рекордов игроков
    """
    def __init__(self):
        self.session = Session()

    def add_record(self, name: str, time: float, diff: int):
        """
        Добавляет новую запись в таблицу.
        :param name: Имя игрока
        :param time: Время игрока
        :param diff: Сложность игры игрока
        :return:
        """
        new_record = Record(name=name, time=time, diff=diff)
        self.session.add(new_record)
        self.session.commit()

    def get_top_records(self, limit: int = 21):
        """
        Возвращает лучшие результаты в виде списка словарей.
        :param limit:Количество строк рекордов, по-умолчанию 21
        :return:Список рекордов
        """
        records = (
            self.session.query(Record)
            .order_by(Record.diff.asc(), Record.time.asc())  # Сортировка по времени
            .limit(limit)
            .all()
        )

        grouped_records = {}
        for record in records:
            if record.diff not in grouped_records:
                grouped_records[record.diff] = []
            if len(grouped_records[record.diff]) < 7:  # По 7 записей для каждой сложности. 3 сложности = 21 запись
                grouped_records[record.diff].append(record)

        result = [
            {"id": record.id, "name": record.name, "time": record.time, "diff": record.diff}
            for records in grouped_records.values()
            for record in records
        ]
        return result


class TestDatabaseOperations(unittest.TestCase):

    def setUp(self):
        """Инициализация сессии перед каждым тестом"""
        self.session = Session()

    def tearDown(self):
        """Закрытие сессии после каждого теста"""
        self.session.close()

    def test_create_and_delete_record(self):
        """Тест для проверки добавления и удаления записи"""

        # Создание новой записи
        new_record = Record(name="Player1", time=100.5, diff=2)
        self.session.add(new_record)
        self.session.commit()

        # Проверка, что запись добавлена
        saved_record = self.session.query(Record).filter_by(name="Player1").first()
        self.assertIsNotNone(saved_record)
        self.assertEqual(saved_record.name, "Player1")
        self.assertEqual(saved_record.time, 100.5)
        self.assertEqual(saved_record.diff, 2)

        # Удаление записи
        self.session.delete(saved_record)
        self.session.commit()

        # Проверка, что запись удалена
        deleted_record = self.session.query(Record).filter_by(name="Player1").first()
        self.assertIsNone(deleted_record)


if __name__ == "__main__":
    unittest.main()