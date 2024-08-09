from fastapi import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, HTTPException
from database import get_async_session
from sqlalchemy import select, insert
from operations.models import book, favorite_book
from operations.schemas import BookCreate, FavoriteBook



router = APIRouter(
    prefix="/operations",
    tags=["Operation"]
)



@router.get("")
async def get_book(book_name: str, session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(book).where(book.c.name == book_name)
        result = await session.execute(query)
        return {
            "status": "success",
            "data": result.all()
        }
    except Exception:
        return {
            "status": "error",
            "data": None
        }
    

@router.post("")
async def add_book(new_book: BookCreate, session: AsyncSession = Depends(get_async_session)):
    try:
        stmt = insert(book).values(**new_book.dict())
        await session.execute(stmt)
        await session.commit()
        return {"status": "success"}
    except Exception:
        return {
            "status": "error",
            "data": None
        }
    
@router.post("")
async def add_in_catalog(book_name: FavoriteBook, session: AsyncSession = Depends(get_async_session)):
    try:
        stmt = insert(favorite_book).values(**book_name.dict())
        await session.execute(stmt)
        await session.commit()
        return {"status": "success"}
    except Exception:
        return {
            "status": "error",
            "data": None
        }

@router.get("")
async def get_favorite_book(book_id: FavoriteBook, session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(favorite_book).where(favorite_book.c.book_id == book_id)
        result = await session.execute(query)
        return {
            "status": "success",
            "data": result.all()
        }
    except Exception:
        return {
            "status": "error",
            "data": None
        }