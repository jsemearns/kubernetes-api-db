from fastapi import FastAPI

from .person.database import init_db
from .person.router import person_router

app = FastAPI()

@app.on_event('startup')
async def startup():
    await init_db()

app.include_router(person_router)

@app.get("/health", summary="Check that the service is operational")
def health():
    """
    Sanity check - this will let the user know that the service is operational.
    It is also used as part of the HEALTHCHECK. Docker uses curl to check that the API service is still running, by exercising this endpoint.
    """
    return {"status": "OK"}

@app.get("/")
async def index():
    return {"message": "Hello World"}