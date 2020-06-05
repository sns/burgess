from sqlalchemy.orm import Session
from app.core.inventory.models.item import Item
from app.core.request_handler import RequestHandler

class Handler(RequestHandler):
    def __init__(self, db: Session):
        super(Handler, self).__init__(db)

    def execute(self):
        return self.db.query(Item).all()