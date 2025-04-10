from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class TodoList(Base):
    __tablename__ = "todolists"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)


    items = relationship("Item", back_populates="todolist")

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    text = Column(String, index=True)
    is_done = Column(Boolean, default=False)
    todolist_id = Column(Integer, ForeignKey("todolists.id"))


    todolist = relationship("TodoList", back_populates="items")
