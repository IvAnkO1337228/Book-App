from pydantic import BaseModel

class BookCreate(BaseModel):
    id: int
    name: str
    author: str
    category: str
    year: int

class FavoriteBook(BaseModel):
    id: int
    name: str
    author: str
    category: str
    year: int