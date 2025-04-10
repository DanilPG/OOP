from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.models import Item
from app.schemas import ItemCreate, ItemRead

router = APIRouter()

@router.get("/items/{item_id}", response_model=ItemRead)
async def read_item(item_id: int, db: AsyncSession = Depends(get_db)):
    item = await db.get(Item, item_id)
    if item is None:
        return {"error": "Item not found"}
    return item

@router.post("/items/", response_model=ItemRead)
async def create_item(item: ItemCreate, db: AsyncSession = Depends(get_db)):
    db_item = Item(name=item.name, description=item.description)
    db.add(db_item)
    await db.commit()
    await db.refresh(db_item)
    return db_item
