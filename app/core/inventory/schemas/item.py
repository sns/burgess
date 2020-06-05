from pydantic import BaseModel

class Item(BaseModel):
    name: str
    quantity: int
    class Config:
        orm_mode = True
