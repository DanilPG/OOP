from sqlalchemy.orm import Session
from . import models, schemas

# CRUD для TodoList
def get_todolist(db: Session, todolist_id: int):
    return db.query(models.TodoList).filter(models.TodoList.id == todolist_id).first()

def create_todolist(db: Session, name: str):
    db_todolist = models.TodoList(name=name)
    db.add(db_todolist)
    db.commit()
    db.refresh(db_todolist)
    return db_todolist

def get_items(db: Session, todolist_id: int):
    return db.query(models.Item).filter(models.Item.todolist_id == todolist_id).all()

# CRUD для Item
def create_item(db: Session, todolist_id: int, name: str, text: str):
    db_item = models.Item(todolist_id=todolist_id, name=name, text=text)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update_item(db: Session, item_id: int, name: str, text: str, is_done: bool):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if db_item:
        db_item.name = name
        db_item.text = text
        db_item.is_done = is_done
        db.commit()
        db.refresh(db_item)
    return db_item

def delete_item(db: Session, item_id: int):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if db_item:
        db.delete(db_item)
        db.commit()
    return db_item
