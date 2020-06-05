from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.core.inventory.queries.fetch_items import Handler as FetchItemsHandler
from app.core.inventory.schemas.item import Item
from app.database import get_db
from app.core.inventory.models.item import Item as ItemModel
from app.core.inventory.queries.fetch_item import Query as FetchItemQuery, Handler as FetchItemHandler
from app.core.inventory.commands.update_items import Command as UpdateItemsCommand, Handler as UpdateItemsHandler
from app.core.inventory.commands.update_item import Command as UpdateItemCommand, Handler as UpdateItemHandler
from app.core.inventory.commands.create_item import Command as CreateItemCommand, Handler as CreateItemHandler
from app.core.inventory.commands.delete_items import Handler as DeleteItemsHandler
from app.core.inventory.commands.delete_item import Command as DeleteItemCommand, Handler as DeleteItemHandler

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

@router.put("/inventory")
def updateInventoryItems(items: List[Item], db: Session=Depends(get_db)):
    """
    Updates the inventory items
    """
    command = UpdateItemsHandler(db, UpdateItemsCommand(items))
    return command.execute()

@router.put("/inventory/{itemName}")
def updateInventoryItem(itemName: str, item: Item, db: Session=Depends(get_db)):
    """
    Updates an inventory item by name
    """
    command = UpdateItemHandler(db, UpdateItemCommand(itemName, item))
    return command.execute()

@router.post("/inventory")
def createInventoryItem(item: Item, db: Session=Depends(get_db)):
    """
    Creates an inventory item
    """
    command = CreateItemHandler(db, CreateItemCommand(item))
    return command.execute()

@router.delete("/inventory")
def deleteInventory(db: Session=Depends(get_db)):
    """
    Deletes all the inventory items
    """
    command = DeleteItemsHandler(db)
    return command.execute()

@router.delete("/inventory/{itemName}")
def deleteInventory(itemName: str, db: Session=Depends(get_db)):
    """
    Delete an inventory item by name
    """
    command = DeleteItemHandler(db, DeleteItemCommand(itemName))
    return command.execute() 
