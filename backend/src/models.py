from sqlalchemy import Column, Integer, String

from .database import Base, engine


class User(Base):
    __tablename__ = "keys"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)


Base.metadata.create_all(bind=engine)
