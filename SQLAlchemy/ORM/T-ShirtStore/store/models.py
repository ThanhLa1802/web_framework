from enum import unique
from .helper.extension import db

class Product(db.Model):
    product_id = db.Column(db.Integer, primary_key = True)
    product_name = db.Column(db.String(100), nullable = False)
    description = db.Column(db.Text)
    sale_price = db.Column(db.Float, nullable = False)
    add_date = db.Column(db.Date)
    category_id = db.Column(db.Integer, db.ForeignKey('category.category_id'))

    def __init__(self, product_name, description, sale_price, add_date, category_id) :
        self.product_name = product_name
        self.description = description
        self.sale_price = sale_price
        self.add_date = add_date
        self.category_id = category_id

class Category(db.Model):
    category_id = db.Column(db.Integer, primary_key = True)
    category_name = db.Column(db.String(100), nullable = False, unique = True)
    def __init__(self, category_name):
        self.category_name = category_name
        

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key = True)
    user_name = db.Column(db.String(100), nullable = False, unique = True)
    password = db.Column(db.String(255), nullable = False)
    full_name = db.Column(db.String(100), nullable = False)
    phone = db.Column(db.String(20), nullable = False, unique = True)
    email = db.Column(db.String(50), nullable = False, unique = True)
    address = db.Column(db.String(100), nullable = False)

    def __init__(self, user_name , password, full_name, phone, email, address):
        self.user_name = user_name
        self.password = password
        self.full_name = full_name
        self.phone = phone
        self.email = email
        self.address = address
class OrderProduct(db.Model):
    order_id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    coupon = db.Column(db.String(40))
    created_date = db.Column(db.Date)

    def __init__(self, user_id, coupon, created_date):
        self.user_id = user_id
        self.coupon = coupon
        self.created_date = created_date

class OrderDetail(db.Model):
    order_id = db.Column(db.Integer, db.ForeignKey('order_product.order_id'), primary_key = True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.product_id'))
    size = db.Column(db.String(10), nullable = False)
    color = db.Column(db.String(20), nullable = False)
    quantity = db.Column(db.Integer, nullable = False)

    def __init__(self, order_id, product_id, size, color, quantity):
        self.order_id = order_id
        self.product_id = product_id
        self.size = size
        self.color = color
        self.quantity = quantity
