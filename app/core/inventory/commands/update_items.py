from sqlalchemy.orm import Session
from app.core.inventory.models.item import Item
from app.core.request_handler import RequestHandler
from app.core.inventory.schemas.item import Item as ItemSchema
from typing import List

class Command:
    items: List[ItemSchema]
    def __init__(self, items):
        self.items = items

class Handler(RequestHandler):
    def __init__(self, db: Session, command: Command):
        super(Handler, self).__init__(db)
        self.command = command

    def execute(self):
        try:
            updatedItems = []
            for i in self.command.items:
                updatedItems.append(Item(name=i.name, quantity=i.quantity))
            self.db.query(Item).delete()            
            self.db.bulk_save_objects(updatedItems)
            self.db.commit()
        except:
            self.db.rollback()
    
        
            