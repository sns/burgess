from sqlalchemy.orm import Session
from app.core.inventory.models.item import Item
from app.core.request_handler import RequestHandler

class Command:
    itemName: str
    def __init__(self, itemName: str):
        self.itemName = itemName

class Handler(RequestHandler):
    def __init__(self, db: Session, command: Command):
        super(Handler, self).__init__(db)
        self.command = command

    def execute(self):
        item = self.db.query(Item).filter(Item.name.ilike(self.command.itemName)).first()
        if item is not None:
            self.db.delete(item)
            self.db.commit()
    
        
            