import json
from sqlalchemy.sql.expression import except_
from library.extension import db
from library.library_ma import StudentSchema, AuthorSchema, CatSchema, BorrowSchema, BookSchema
from library.models import Students, Category, Author, Books, Borrows
from flask import jsonify, request
from datetime import datetime
from sqlalchemy.sql import func
from sqlalchemy.exc import IntegrityError
books_schema = BookSchema(many = True)
book_schema = BookSchema()
def get_all_books_serv():
    books = Books.query.all()
    return books_schema.jsonify(books)
def get_book_byid_serv(id):
    book = Books.query.get(id)
    if book:
        return book_schema.jsonify(book)
    else:
       return "Not found book!"
def add_book_serv():
    name = request.json['name']
    page_count = request.json['page_count']
    author_id = request.json['author_id']
    category_id = request.json['category_id']
    try:
        new_book = Books(name, page_count, author_id, category_id)
        db.session.add(new_book)
        db.session.commit() 
        return "Add succsess!"
    except IntegrityError:
        db.session.rollback()
        return "Can not add book!"
def delete_book_serv(id):
    book = Books.query.get(id)
    try:
        db.session.delete(book)
        db.session.commit()
        return "Deleted Book!"
    except:
        db.session.rollback()
        return "Can't Delete Book!"
def update_book_serv(id):
    pass

def get_book_author_serv(author):
    books = Books.query.join(Author).filter(func.lower(Author.name) == author.lower()).all()
    if books:
        return books_schema.jsonify(books)
    else: 
        return f"Not found books by {author}"

def get_book_category_serv(category):
    books = Books.query.join(Category).filter(func.lower(Category.name) == category.lower()).all()
    return books_schema.jsonify(books)