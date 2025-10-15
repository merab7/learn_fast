from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

books = [
    {
        "id": 1,
        "title": "The Midnight Library",
        "author": "Matt Haig",
        "publisher": "Viking Press",
        "published_date": "2020-08-13",
        "page_count": 304,
        "language": "English",
    },
    {
        "id": 2,
        "title": "Atomic Habits",
        "author": "James Clear",
        "publisher": "Avery",
        "published_date": "2018-10-16",
        "page_count": 320,
        "language": "English",
    },
    {
        "id": 3,
        "title": "The Silent Patient",
        "author": "Alex Michaelides",
        "publisher": "Celadon Books",
        "published_date": "2019-02-05",
        "page_count": 336,
        "language": "English",
    },
    {
        "id": 4,
        "title": "Educated",
        "author": "Tara Westover",
        "publisher": "Random House",
        "published_date": "2018-02-20",
        "page_count": 334,
        "language": "English",
    },
    {
        "id": 5,
        "title": "Where the Crawdads Sing",
        "author": "Delia Owens",
        "publisher": "G.P. Putnam's Sons",
        "published_date": "2018-08-14",
        "page_count": 384,
        "language": "English",
    },
    {
        "id": 6,
        "title": "The Seven Husbands of Evelyn Hugo",
        "author": "Taylor Jenkins Reid",
        "publisher": "Atria Books",
        "published_date": "2017-06-13",
        "page_count": 388,
        "language": "English",
    },
    {
        "id": 7,
        "title": "Becoming",
        "author": "Michelle Obama",
        "publisher": "Crown Publishing",
        "published_date": "2018-11-13",
        "page_count": 448,
        "language": "English",
    },
    {
        "id": 8,
        "title": "Circe",
        "author": "Madeline Miller",
        "publisher": "Little, Brown and Company",
        "published_date": "2018-04-10",
        "page_count": 400,
        "language": "English",
    },
    {
        "id": 9,
        "title": "The Alchemist",
        "author": "Paulo Coelho",
        "publisher": "HarperOne",
        "published_date": "1988-01-01",
        "page_count": 208,
        "language": "English",
    },
    {
        "id": 10,
        "title": "Project Hail Mary",
        "author": "Andy Weir",
        "publisher": "Ballantine Books",
        "published_date": "2021-05-04",
        "page_count": 496,
        "language": "English",
    },
]


class Book(BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str


class BookUpdateModel(BaseModel):
    title: str
    publisher: str
    page_count: int
    language: str


@app.get("/books", response_model=List[Book])
async def get_all_books():
    return books


@app.post("/books", status_code=status.HTTP_201_CREATED)
async def create_a_book(book_data: Book) -> dict:
    new_book = book_data.model_dump()

    books.append(new_book)
    return new_book


@app.patch("/books/{id}")
async def update_the_book(id: int, book_update_data: BookUpdateModel) -> dict:
    for book in books:
        if id == book["id"]:
            book["title"] = book_update_data.title
            book["publisher"] = book_update_data.publisher
            book["page_count"] = book_update_data.page_count
            book["language"] = book_update_data.language

            return book
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with this {id} not found"
    )


@app.delete("/books/{id}")
async def get_the_book(id: int) -> dict:
    for book in books:
        if id == book["id"]:
            books.remove(book)
            return {}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with this {id} not found"
    )
