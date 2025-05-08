from pydantic import BaseModel

class Language(BaseModel):
    id: int
    title: str
    images: list
    contents: list