from sqlalchemy.orm import Session

class RequestHandler:
    def __init__(self, db: Session):
        self.db = db