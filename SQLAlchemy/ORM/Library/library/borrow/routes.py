from library.book.services import delete_book_serv
from flask import Blueprint, request
from library.models import Students, Category, Author, Books, Borrows
from library.extension import db
from .services import  (get_all_borrow_serv, add_borrow_serv, get_borrow_byname_serv, 
                        get_borrow_author_cat_serv, get_borrow_byid_serv , delete_borrow_serv)
borrow = Blueprint('borrow', __name__)

#get all students
@borrow.route('/borrow-management/all-borrow', methods = ['GET'])
def get_all_borrow():
    return get_all_borrow_serv()

#add new borrow
@borrow.route('/borrow-management/borrow', methods = ['POST'])
def add_borrow():
    return add_borrow_serv()

#get borrow by ID
@borrow.route('/borrow-management/borrow/<int:id>', methods = ['GET'])
def get_borrow_byid(id):
    return get_borrow_byid_serv(id)
#update borrow by ID
@borrow.route('/borrow-management/borrow/<int:id>', methods = ['PUT'])
def update_borrow_byid():
    pass

@borrow.route('/borrow-management/borrow/<int:id>', methods = ['DELETE'])
def delete_borrow_byid(id):
    return delete_borrow_serv(id)

@borrow.route('/borrow-management/borrow/<string:name>', methods = ['GET'])
def get_borrow_byname(name):
    return get_borrow_byname_serv(name)

@borrow.route('/borrow-management/borrow_student/<string:name>', methods = ['GET'])
def get_borrow_author_cat(name):
    return get_borrow_author_cat_serv(name)


