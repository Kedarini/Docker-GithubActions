from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

postgresql_url = "postgresql://postgres:postgres@db:5432/postgres"

engine = create_engine(postgresql_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
