from flask import Blueprint, request
from library.models import Students, Category, Author, Books, Borrows
from library.extension import db
from .services import (get_all_students_serv, add_student_serv, get_student_serv, delete_student_serv)
student = Blueprint('student', __name__)

#get all students
@student.route('/student-management/students', methods = ['GET'])
def get_all_students():
    return get_all_students_serv()

#add new student
@student.route('/student-management/student', methods = ['POST'])
def add_student():
    return add_student_serv()


#get student by ID
@student.route('/student-management/student/<int:id>', methods = ['GET'])
def get_student_byid(id):
    return get_student_serv(id)

#update student by ID
@student.route('/student-management/student/<int:id>', methods = ['PUT'])
def update_student_byid():
    pass

@student.route('/student-management/student/<int:id>', methods = ['DELETE'])
def delete_student_byid(id):
    return delete_student_serv(id)