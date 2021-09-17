from flask import Blueprint, request
from .models import Students, Category, Author, Books, Borrows
from .extension import db
from .controllers import (get_category, add_category, add_student, 
                        del_student, add_author, add_book, get_book_detail, add_borrow,
                        book_from_borrow)
routes = Blueprint('routes', __name__)

#add category book
@routes.route('/category', methods = ['POST'])
def add_cat():
    add_category()
    return ("Add success!"), 200
@routes.route('/get_category', methods = ['GET'])
def get_cat():
    return get_category()
#get category

@routes.route('/add_student', methods = ['POST'])
def add_stu():
    add_student()
    return ("Add success!"), 200


@routes.route('/del_student/<int:id>', methods = ['PUT'])
def del_stu(id):
    del_student(id)
    return ("Deleted success!"), 200

@routes.route('/add_author', methods = ['POST'])
def add_aut():
    add_author()
    return ("Add success!"), 200

@routes.route('/add_book', methods = ['POST'])
def add_books():
    add_book()
    return ("Add success!"), 200

@routes.route('/get_book_detail/<int:id>', methods = ['GET'])
def get_book(id):
    return get_book_detail(id)

@routes.route('/add_borrow', methods = ['POST'])
def add_borrows():
    add_borrow()
    return ("Add success!"), 200
@routes.route('/get_book_borrow/<int:id>', methods = ['GET'])
def get_book_borrow(id):
    return book_from_borrow(id)
