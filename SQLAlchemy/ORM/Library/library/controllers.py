import json
from .extension import db
from .extension import ma
from .models import Students, Category, Author, Books, Borrows
from flask import jsonify, request
from datetime import datetime

class StudentSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'birth_date', 'gender', 'class_name')

class CatSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')

class AuthorSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')

class BorrowSchema(ma.Schema):
    class Meta:
        fields = ('order_id', 'product_id','quantity','total_price')

category = CatSchema(many = True)
author = AuthorSchema(many = True)
#add category
def add_category():
    name = request.json['name']
    new_cat = Category(name)
    db.session.add(new_cat)
    db.session.commit()
def get_category():
    all_cats = Category.query.all()
    return category.jsonify(all_cats)

def add_student():
    name = request.json['name']
    birth_date = datetime.strptime(request.json['birth_date'], '%d-%m-%Y').date()
    gender = request.json['gender']
    class_name = request.json['class_name']
    new_student = Students(name, birth_date, gender, class_name)
    db.session.add(new_student)
    db.session.commit()

def del_student(id):
    student = Students.query.get(id)
    db.session.delete(student)
    db.session.commit()

def add_author():
    name = request.json['name']
    new_author = Author(name)
    db.session.add(new_author)
    db.session.commit()

def add_book():
    name = request.json['name']
    page_count = request.json['page_count']
    author_id = request.json['author_id']
    category_id = request.json['category_id']
    new_book = Books(name, page_count, author_id, category_id)
    db.session.add(new_book)
    db.session.commit()

def get_book_detail(id):
    book = db.session.query(Books.id, Books.name, Author.name, Category.name).join(Author).join(Category).filter(Books.id == 1).first()
    return ({"Book": book})

#add borrow
def add_borrow():
    book_id = request.json['book_id']
    student_id = request.json['student_id']
    borrow_date = datetime.strptime(request.json['borrow_date'], '%d-%m-%Y').date()
    return_date  = datetime.strptime(request.json['return_date'], '%d-%m-%Y').date()
    new_borrow = Borrows(book_id, student_id, borrow_date, return_date)
    db.session.add(new_borrow)
    db.session.commit()

#get detail book from student

def book_from_borrow(id):
    book = db.session.query(Borrows.id, Students.name, Students.class_name).filter(Borrows.id == 2).first()
    return ({"Book": book})

