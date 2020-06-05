from sqlalchemy.orm import Session
from app.core.inventory.models.item import Item
from app.core.request_handler import RequestHandler

class Query():
    name: str
    def __init__(self, name):
        self.name = name

class Handler(RequestHandler):
    def __init__(self, db: Session, request: Query):
        super(Handler, self).__init__(db)
        self.request = request 

    def execute(self):
        return self.db.query(Item).filter(Item.name.ilike(self.request.name)).first()