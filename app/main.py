from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from app.routers import languages

origins = [
    "http://localhost:5173",
    "https://thepaths.space"
]

app = FastAPI(
    title="The Paths",
    description="An Api created to The Paths.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)


app.include_router(languages.router, prefix="/languages", tags=["languages"])

app.mount("/static", StaticFiles(directory="./app/static"), name="static")