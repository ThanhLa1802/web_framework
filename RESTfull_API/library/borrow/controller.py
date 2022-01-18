from flask import Blueprint
from .services import get_borrow_author_cat_service
borrow = Blueprint("borrow", __name__)


@borrow.route("/borrow-management/borrow/<string:student_name>", methods=['GET'])
def get_borrow_author_cat(student_name):
    return get_borrow_author_cat_service(student_name)
