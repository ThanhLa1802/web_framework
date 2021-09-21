import json
from sqlalchemy.sql.expression import except_
from library.extension import db
from library.library_ma import StudentSchema, AuthorSchema, CatSchema, BorrowSchema, BookSchema
from library.models import Students, Category, Author, Books, Borrows
from flask import jsonify, request
from datetime import datetime
from sqlalchemy.sql import func
from sqlalchemy.exc import IntegrityError

borrows_schema = BorrowSchema(many = True)
borrow_schema = BorrowSchema()

def get_all_borrow_serv():
    borrows = Borrows.query.all()
    return borrows_schema.jsonify(borrows)
def get_borrow_byid_serv(id):
    borrow = Borrows.query.get(id)
    if borrow:
        return borrow_schema.jsonify(borrow)
    else:
       return "Not found book!"
def add_borrow_serv():
    book_id = request.json['book_id']
    student_id = request.json['student_id']
    borrow_date = datetime.strptime(request.json['borrow_date'], '%d-%m-%Y').date()
    return_date = datetime.strptime(request.json['return_date'], '%d-%m-%Y').date()
    try:
        new_borrow = Borrows(book_id, student_id, borrow_date, return_date)
        db.session.add(new_borrow)
        db.session.commit() 
        return "Add success!"
    except IntegrityError:
        db.session.rollback()
        return "Can not add borrow!"
def delete_borrow_serv(id):
    book = Borrows.query.get(id)
    try:
        db.session.delete(book)
        db.session.commit()
        return "Deleted Borrow!"
    except:
        db.session.rollback()
        return "Can't Delete Borrow!"


def get_borrow_byname_serv(student_name):
    borrows = Borrows.query.join(Students).filter(func.lower(Students.name) == student_name.lower()).all()
    if borrows:
        return borrows_schema.jsonify(borrows)
    else:
        return "Not found borrow!"

def get_borrow_author_cat_serv(student_name):
    borrows = db.session.query(Borrows.id, Books.name, Category.name, Author.name).join(Students, Borrows.student_id == Students.id).join(Books, Borrows.book_id == Books.id).join\
            (Category, Books.category_id == Category.id).join(Author, Books.author_id == Author.id).filter(func.lower(Students.name) == student_name.lower()).all()
    print(borrows)
    if borrows:
        return jsonify({f"{student_name} borrowed": borrows })
    else:
        return "Not found borrow!"