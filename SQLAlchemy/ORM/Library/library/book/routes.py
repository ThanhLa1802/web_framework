from flask import Blueprint, request
from library.models import Students, Category, Author, Books, Borrows
from library.extension import db
from .services import  (get_all_books_serv, get_book_byid_serv, add_book_serv, 
                        delete_book_serv, update_book_serv, get_book_author_serv,
                        get_book_category_serv)
book = Blueprint('book', __name__)

#get all students
@book.route('/book-management/books', methods = ['GET'])
def get_all_books():
    return get_all_books_serv()

#add new book
@book.route('/book-management/book', methods = ['POST'])
def add_book():
    return add_book_serv()


#get student by ID
@book.route('/book-management/book/<int:id>', methods = ['GET'])
def get_book_byid(id):
    return get_book_byid_serv(id)

#update student by ID
@book.route('/book-management/book/<int:id>', methods = ['PUT'])
def update_book_byid():
    pass

@book.route('/book-management/book/<int:id>', methods = ['DELETE'])
def delete_book_byid(id):
    return delete_book_serv(id)

@book.route('/book-management/book-by-author/<string:author>', methods = ['GET'])
def get_book_by_author(author):
    return get_book_author_serv(author)

@book.route('/book-management/book-by-category/<string:cat>', methods = ['GET'])
def get_book_by_category(cat):
    return get_book_category_serv(cat)