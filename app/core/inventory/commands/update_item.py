from sqlalchemy.orm import Session
from app.core.inventory.models.item import Item
from app.core.request_handler import RequestHandler
from app.core.inventory.schemas.item import Item as ItemSchema

class Command:
    item: ItemSchema
    itemName: str
    def __init__(self, itemName: str, item: ItemSchema):
        self.item = item
        self.itemName = itemName

class Handler(RequestHandler):
    def __init__(self, db: Session, command: Command):
        super(Handler, self).__init__(db)
        self.command = command

    def execute(self):
        item = self.db.query(Item).filter(Item.name.ilike(self.command.itemName)).first()
        if item is not None:
            item.name = self.command.item.name
            item.quantity = self.command.item.quantity
            self.db.commit()
    
        
            