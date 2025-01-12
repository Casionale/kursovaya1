from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Создаем базу данных
Base = declarative_base()

class Record(Base):
    __tablename__ = 'records'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    time = Column(Float, nullable=False)

# Настройка подключения к базе данных
DATABASE_URL = "sqlite:///records.db"
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

class Database:
    def __init__(self):
        self.session = Session()

    def add_record(self, name: str, time: float):
        """Добавляет новую запись в таблицу."""
        new_record = Record(name=name, time=time)
        self.session.add(new_record)
        self.session.commit()

    def get_top_records(self, limit: int = 10):
        """Возвращает лучшие результаты в виде списка словарей."""
        records = (
            self.session.query(Record)
            .order_by(Record.time.asc())  # Сортировка по времени
            .limit(limit)
            .all()
        )
        return [{"id": record.id, "name": record.name, "time": record.time} for record in records]
