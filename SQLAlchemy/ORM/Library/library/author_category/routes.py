from flask import Blueprint, request
from library.models import Students, Category, Author, Books, Borrows
from library.extension import db
from .services import (get_all_authors_serv, add_author_serv, add_category_serv, get_all_categories_serv)
author_cat = Blueprint('author_cat', __name__)

#get all authors
@author_cat.route('/author-management/authors', methods = ['GET'])
def get_all_authors():
    return get_all_authors_serv()

#add category
@author_cat.route('/author-management/author', methods = ['POST'])
def add_author():
    return add_author_serv()

#get all categories
@author_cat.route('/category-management/categories', methods = ['GET'])
def get_all_categories():
    return get_all_categories_serv()

#add category
@author_cat.route('/category-management/category', methods = ['POST'])
def add_category():
    return add_category_serv()
