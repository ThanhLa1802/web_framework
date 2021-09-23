import json
from sqlalchemy.sql.expression import except_
from store.helper.extension import db
from store.helper.store_ma import ProductSchema
from store.models import Product 
from flask import jsonify, request
from datetime import datetime
from sqlalchemy.sql import func
from sqlalchemy.exc import IntegrityError
products_schema = ProductSchema(many = True)
product_schema = ProductSchema()
def get_all_products_serv():
    products = Product.query.all()
    if products:
        return products_schema.jsonify(products)
    return "Not found product!"
def get_product_byid_serv(id):
    product = Product.query.get(id)
    if product:
        return product_schema.jsonify(product)
    else:
       return "Not found book!"
def add_product_serv():
    product_name = request.json['product_name']
    description = request.json['description']
    sale_price = request.json['sale_price']
    add_date = datetime.strptime(request.json['add_date'], '%d-%m-%Y').date()
    category_id = request.json['category_id']
    try:
        new_product= Product(product_name, description, sale_price, add_date, category_id)
        db.session.add(new_product)
        db.session.commit() 
        return "Add succsess!"
    except IntegrityError:
        db.session.rollback()
        return "Can not add book!"
def delete_product_serv(id):
    product = Product.query.get(id)
    try:
        db.session.delete(product)
        db.session.commit()
        return "Deleted Product!"
    except IntegrityError:
        db.session.rollback()
        return "Can't Delete Product!"

def update_student_serv(id):
    product = Product.query.get(id)
    product_name = request.json['product_name']
    description = request.json['description']
    sale_price = request.json['sale_price']
    try:
        product.product_name = product_name
        product.description = description
        product.sale_price = sale_price
        db.session.commit()
        return "Updated Product!"
    except IntegrityError:
        db.session.rollback()
        return "Can't Update Product!"