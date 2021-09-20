import json
from sqlalchemy.sql.expression import except_
from library.extension import db
from library.library_ma import StudentSchema, AuthorSchema, CatSchema, BorrowSchema, BookSchema
from library.models import Students, Category, Author, Books, Borrows
from flask import jsonify, request
from datetime import datetime
from sqlalchemy.exc import IntegrityError

authers_schema = AuthorSchema(many = True)
auther_schema = AuthorSchema()

cats_schema = CatSchema(many = True)
cat_schema = CatSchema()
def get_all_authors_serv():
    authors = Author.query.all()
    return authers_schema.jsonify(authors)
def add_author_serv(): 
    try:
        name = request.json['name']
        new_author = Author(name)
        db.session.add(new_author)
        db.session.commit()
        return "Add success"
    except IntegrityError:
        db.session.rollback()
        return "Can not add author!"
def get_all_categories_serv():
    categories = Category.query.all()
    return cats_schema.jsonify(categories)
def add_category_serv():
    try:
        name = request.json['name']
        new_cate = Category(name)
        db.session.add(new_cate)
        db.session.commit()
        return "Add success"
    except IntegrityError:
        db.session.rollback()
        return "Can not add category!"