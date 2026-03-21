from fastapi import FastAPI
from app.api import parse, validate

app = FastAPI(title="EDI Parser API")

# Register routes
app.include_router(parse.router)
app.include_router(validate.router)


@app.get("/")
def root():
    return {"message": "EDI Parser API is running"}
