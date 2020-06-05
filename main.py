from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from models.item import Item
import json
import logging

app = FastAPI(docs_url="/")
logger = logging.getLogger("api")
logger.setLevel(logging.DEBUG)

def getInventoryData():
    inventoryData = []
    try:
        fake_db = open("./inventory.txt", "r")
        data = json.load(fake_db)
        inventoryData = list(map(lambda x: Item.parse_raw(x), data["inventoryItems"]))
    except:
        logger.error("SOMETHING WENT VERY VERY WRONG WITH THE DATA SOURCE")        
    finally:
        fake_db.close()
    return inventoryData

def UpdateInventoryData(inventoryData: List[Item]):
    items = list(map(lambda x: x.json(), inventoryData))
    try:
        fake_db = open("./inventory.txt", "r")
        data = json.load(fake_db)
        fake_db.close()        
        data["inventoryItems"] = items
        fake_db = open("./inventory.txt", "w")
        json.dump(data, fake_db)
    except:
        logger.error("SOMETHING WENT VERY VERY WRONG WITH THE DATA SOURCE")
    finally:
        fake_db.close()

@app.get("/inventory")
async def fetchInventory():
    """
    Displays the entire inventory
    """
    return getInventoryData()
    
@app.get("/inventory/{item_name}")
async def fetchInventoryItem(item_name: str = None):
    """
    Displays a single inventory item
    """    
    return next((item for item in getInventoryData() if item.name.lower() == item_name.lower()), None)

@app.put("/inventory")
async def updateInventory(inventory: List[Item]):
    """
    Replaces the inventory with the inventory passed in with the request body
    """
    UpdateInventoryData(inventory)

@app.put("/inventory/{item_name}")
async def updateInventoryItem(inventoryItem: Item, item_name: str):
    """
    Replaces the inventory whose name is {item_name} with the inventory passed in with the request body
    """
    inventoryData = getInventoryData()
    for index, item in enumerate(inventoryData):
        if(item.name.lower() == item_name.lower()):
            inventoryData[index] = inventoryItem
            break
    UpdateInventoryData(inventoryData)

@app.post("/inventory")
async def addInventoryItem(inventoryItem: Item):
    """
    creeates a a new inventory item from the data passed in with the request body
    """
    inventoryData = getInventoryData()
    isUpdate = False
    for index, item in enumerate(inventoryData):
        if(item.name.lower() == inventoryItem.name.lower()):
            inventoryData[index] = inventoryItem
            isUpdate = True
    if not isUpdate:
        inventoryData.append(inventoryItem)
    UpdateInventoryData(inventoryData)

@app.delete("/inventory/{item_name}")
async def deleteInventoryItem(item_name: str):
    inventoryData = getInventoryData()
    for index, item in enumerate(inventoryData):
        if(item.name.lower() == item_name.lower()):
            del inventoryData[index]
            UpdateInventoryData(inventoryData)

@app.delete("/inventory")
async def clearInventory():
    UpdateInventoryData([])


import uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8081)