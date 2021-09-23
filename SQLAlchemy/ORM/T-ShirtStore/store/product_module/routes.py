from flask import Blueprint, request
from store.models import Product
from store.helper.extension import db
from .services import (get_all_products_serv, add_product_serv, get_product_byid_serv, 
                        delete_product_serv, update_student_serv)
product = Blueprint('product', __name__)

#get all students
@product.route('/product-management/products', methods = ['GET'])
def get_all_products():
    return get_all_products_serv()

#add new book
@product.route('/product-management/product', methods = ['POST'])
def add_product():
    return add_product_serv()

#get student by ID
@product.route('/product-management/product/<int:id>', methods = ['GET'])
def get_product_byid(id):
    return get_product_byid_serv(id)

#update student by ID
@product.route('/product-management/product/<int:id>', methods = ['PUT'])
def update_product_byid(id):
    return update_student_serv(id)

@product.route('/book-management/book/<int:id>', methods = ['DELETE'])
def delete_product_byid(id):
    return delete_product_serv(id)

@product.route('/book-management/book-by-author/<string:author>', methods = ['GET'])
def get_product_by_author(author):
    pass

@product.route('/book-management/book-by-category/<string:cat>', methods = ['GET'])
def get_product_by_category(cat):
    pass