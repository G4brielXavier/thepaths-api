from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.routers import languages

app = FastAPI(
    title="The Paths",
    description="An Api created to The Paths.",
    version="1.0.0"
)

app.include_router(languages.router, prefix="/languages", tags=["languages"])

app.mount("/static", StaticFiles(directory="./app/static"), name="static")