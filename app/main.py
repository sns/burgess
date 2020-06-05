from fastapi import FastAPI, Depends
from app.database import SessionLocal, engine
from app.routes.inventory import router as inventoryRouter
import logging

api = FastAPI(docs_url="/")
logger = logging.getLogger("api")
logger.setLevel(logging.DEBUG)

api.include_router(
    inventoryRouter,
    responses={404: {"description": "Not found"}},
)
