from fastapi import FastAPI, Depends
from app.database import SessionLocal, engine
from app.routes.inventory import router as inventoryRouter

api = FastAPI(docs_url="/")

api.include_router(
    inventoryRouter,
    responses={404: {"description": "Not found"}},
)
