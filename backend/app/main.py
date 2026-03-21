from fastapi import FastAPI
from app.api import parse

app = FastAPI()

app.include_router(parse.router, prefix="/api")
