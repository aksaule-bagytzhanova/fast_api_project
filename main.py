from fastapi import FastAPI, Query, Path, Body
from schemas import Book, Author, Genre, BookOut


app = FastAPI()


@app.get('/')
def home():
    return {'key': 'Hello'}


@app.get('/{pk}')#/5/?q=ttt
def get_item(pk: int, q: str = None):
    return {"key": pk, "q": q}


@app.get('/user/{pk}/items/{item}/')
def get_user_item(pk: int, item: str):
    return {"user": pk, "item": item}


@app.post('/book', response_model=Book, response_model_exclude_unset=True)  #, response_model_include={''})
def create_book(item: Book, author: Author, quantity: int = Body(..., embed=True)):
    return {"item": item, "author": author, 'quantity': quantity}

@app.post('/auther')
def create_author(author: Author):
    return {"author": author}


@app.get('/book')#/book/&g=qwert
def get_book(q: str = Query(None, min_length=2, max_length=5, description="Search book")):
    return q


@app.get('/book/{pk}')
def get_single_book(pk: int = Path(..., gt=1, le=20), pages: int = Query(None, gt=10, le=500)):
    return {"pk":pk, "pages": pages}