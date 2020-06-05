from sqlalchemy.orm import Session
import logging

class RequestHandler:
    logger = logging.getLogger("api")
    logger.setLevel(logging.DEBUG)        
    def __init__(self, db: Session):
        self.db = db