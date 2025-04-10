from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, schemas, database

router = APIRouter()

# Создание списка дел (TodoList)
@router.post("/todolists/", response_model=schemas.TodoList)
def create_todolist(name: str, db: Session = Depends(database.get_db)):
    return crud.create_todolist(db=db, name=name)

# Получение всех TodoList
@router.get("/todolists/", response_model=List[schemas.TodoList])
def get_todolists(db: Session = Depends(database.get_db)):
    return db.query(models.TodoList).all()

# Получение TodoList по id
@router.get("/todolists/{todolist_id}", response_model=schemas.TodoList)
def get_todolist(todolist_id: int, db: Session = Depends(database.get_db)):
    todolist = crud.get_todolist(db, todolist_id)
    if not todolist:
        raise HTTPException(status_code=404, detail="TodoList not found")
    return todolist

# Создание элемента (Item) в TodoList
@router.post("/todolists/{todolist_id}/items/", response_model=schemas.Item)
def create_item(todolist_id: int, name: str, text: str, db: Session = Depends(database.get_db)):
    return crud.create_item(db=db, todolist_id=todolist_id, name=name, text=text)

# Получение элементов списка TodoList
@router.get("/todolists/{todolist_id}/items/", response_model=List[schemas.Item])
def get_items(todolist_id: int, db: Session = Depends(database.get_db)):
    return crud.get_items(db=db, todolist_id=todolist_id)

# Обновление элемента TodoList
@router.patch("/items/{item_id}", response_model=schemas.Item)
def update_item(item_id: int, name: str, text: str, is_done: bool, db: Session = Depends(database.get_db)):
    return crud.update_item(db=db, item_id=item_id, name=name, text=text, is_done=is_done)

# Удаление элемента TodoList
@router.delete("/items/{item_id}", response_model=schemas.Item)
def delete_item(item_id: int, db: Session = Depends(database.get_db)):
    return crud.delete_item(db=db, item_id=item_id)
