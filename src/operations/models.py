from sqlalchemy import Column, Integer, String, Table, MetaData, ForeignKey


metadata = MetaData()

book = Table(
    "book",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("author", String, nullable=False),
    Column("category", String, nullable=False),
    Column("year", Integer, nullable=False),
)

favorite_book = Table(
    "favorite_book",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("book_id", Integer, ForeignKey(book.c.id)),
    Column("book_name", String, nullable=False),
    Column("book_author", String, nullable=False),
    Column("book_category", String, nullable=False),
    Column("book_year", Integer, nullable=False),
)