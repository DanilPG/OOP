from pydantic import BaseModel
from typing import List, Optional


class TodoListCreate(BaseModel):
    name: str

class TodoList(TodoListCreate):
    id: int
    items: List[str] = []

    class Config:
        orm_mode = True


class ItemCreate(BaseModel):
    name: str
    text: str

class Item(ItemCreate):
    id: int
    is_done: bool
    todolist_id: int

    class Config:
        orm_mode = True
