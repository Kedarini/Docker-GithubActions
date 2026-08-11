from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .database import SessionLocal
from . import models, schemas

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/items", response_model=list[schemas.ItemResponse])
def get_items(db: Session = Depends(get_db)):
    items = db.query(models.User).all()
    return items


@app.post("/items", response_model=schemas.ItemResponse)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    db_item = models.User(name=item.name)

    db.add(db_item)
    db.commit()
    db.refresh(db_item)

    return db_item
