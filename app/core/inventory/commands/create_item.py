from sqlalchemy.orm import Session
from app.core.inventory.models.item import Item
from app.core.request_handler import RequestHandler
from app.core.inventory.schemas.item import Item as ItemSchema

class Command:
    item: ItemSchema
    def __init__(self, item: ItemSchema):
        self.item = item

class Handler(RequestHandler):
    def __init__(self, db: Session, command: Command):
        super(Handler, self).__init__(db)
        self.command = command

    def execute(self):
        item = Item(name=self.command.item.name, quantity=self.command.item.quantity)
        try:
            self.db.add(item)
            self.db.commit()
        except:
            self.logger.error("There was an error inserting the item into the items table")