import json
from library.extension import db
from library.library_ma import StudentSchema, AuthorSchema, CatSchema, BorrowSchema
from library.models import Students, Category, Author, Books, Borrows
from flask import jsonify, request
from datetime import datetime
from sqlalchemy.exc import IntegrityError

students_schema = StudentSchema(many = True)
student_schema =StudentSchema ()
def get_all_students_serv():
    students = Students.query.all()
    return students_schema.jsonify(students)
def get_student_serv(id):
    student = Students.query.get(id)
    if student:
        return student_schema.jsonify(student)
    else:
        return "Not find student!", 404
def add_student_serv():
    name = request.json['name']
    birth_date = datetime.strptime(request.json['birth_date'], '%d-%m-%Y').date()
    gender = request.json['gender']
    class_name = request.json['class_name']
    try:
        new_student = Students(name, birth_date, gender, class_name)
        db.session.add(new_student)
        db.session.commit()
        return "Add success!"
    except IntegrityError:
        db.session.rollback()
        return "Can't add Student!"
def delete_student_serv(id):
    student = Students.query.get(id)
    try:
        db.session.delete(student)
        db.session.commit()
        return "Deleted Student!"
    except IntegrityError:
        db.session.rollback()
        return "Can't Delete Student!"

def update_student_serv(id):
    pass