from flask import Blueprint, request
from store.models import Product
from store.helper.extension import db

category = Blueprint('category', __name__)

#get all students
@category.route('/category-management/categories', methods = ['GET'])
def get_all_categories():
    pass

#add new book
@category.route('/category-management/category', methods = ['POST'])
def add_category():
    pass

#get student by ID
@category.route('/category-management/category/<int:id>', methods = ['GET'])
def get_category_byid(id):
    pass

#update student by ID
@category.route('/product-management/product/<int:id>', methods = ['PUT'])
def update_product_byid():
    pass

@category.route('/book-management/book/<int:id>', methods = ['DELETE'])
def delete_product_byid(id):
    pass

@category.route('/book-management/book-by-author/<string:author>', methods = ['GET'])
def get_product_by_author(author):
    pass

@category.route('/book-management/book-by-category/<string:cat>', methods = ['GET'])
def get_product_by_category(cat):
    pass