from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.core.inventory.queries.fetch_items import Handler as FetchItemsHandler
from app.core.inventory.schemas.item import Item
from app.database import get_db
from app.core.inventory.models.item import Item as ItemModel
from app.core.inventory.queries.fetch_item import Query as FetchItemQuery, Handler as FetchItemHandler

router = APIRouter()
@router.get("/inventory", response_model=List[Item])
def fetchInventory(db: Session=Depends(get_db)):
    """
    Fetches the entire inventory
    """
    query = FetchItemsHandler(db)
    return query.execute()

@router.get("/inventory/{itemName}", response_model=Item)
def fetchInventoryItemByName(itemName: str=None, db: Session=Depends(get_db)):
    """
    Fetches an inventory item by name
    """
    query = FetchItemHandler(db, FetchItemQuery(itemName))
    return query.execute()

