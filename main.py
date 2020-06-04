from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from models.item import Item

app = FastAPI()
inventoryData: List[Item] = [Item(name="Apples", quantity=3), Item(name="Oranges", quantity=7), Item(name="Pomegranates", quantity=55)]

@app.get("/")
def index():
    return "Welcome"


@app.get("/inventory")
async def inventory():
    """
    Displays the entire inventory
    """
    return inventoryData
    
@app.get("/inventory/{item_name}")
async def inventory(item_name: str = None):
    """
    Displays a single inventory item
    """    
    return next((item for item in inventoryData if item.name.lower() == item_name.lower()), None)
