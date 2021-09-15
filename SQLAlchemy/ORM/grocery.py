from enum import unique
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow 
from datetime import datetime
import json
from marshmallow import fields

app  = Flask(__name__)
app.secret_key = "hello"
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///grocery.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

#init db
db = SQLAlchemy(app)

#Init ma
ma = Marshmallow(app)

@app.before_first_request
def create_tables():
    db.create_all()
class Product(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), unique = True)
    description = db.Column(db.String(200))
    uom_id = db.Column(db.Integer, db.ForeignKey('uom.id'))
    price_per_unit = db.Column(db.Float)

    def __init__(self, name, description, uom_id, price_per_unit):
        self.name = name 
        self.description = description
        self.uom_id = uom_id
        self.price_per_unit = price_per_unit

class Order_sum(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    customer = db.Column(db.String(100), unique = True, nullable=False)
    total = db.Column(db.Float)
    date_time = db.Column(db.DateTime, nullable=False, default = datetime.utcnow)
    def __init__(self, customer, total):
        self.customer = customer
        self.total = total

class Order_detail(db.Model):
    order_id = db.Column(db.Integer, db.ForeignKey('order_sum.id'), primary_key = True,)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    quantity = db.Column(db.Integer, nullable=False)
    total_price = db.Column(db.Float)
    def __init__(self,oder_id, product_id, quantity, total_price):
        self.order_id = oder_id
        self.product_id = product_id
        self.quantity = quantity
        self.total_price = total_price
class Uom(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    uom_name = db.Column(db.String(50), unique = True, nullable=False)
    def __init__(self, uom_name):
        self.uom_name = uom_name

class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'uom_id', 'price_per_unit')

class UomSchema(ma.Schema):
    class Meta:
        fields = ('id', 'uom_name')

class OrderSchema(ma.Schema):
    class Meta:
        fields = ('id', 'customer', 'total','date_time')

class OderDetail(ma.Schema):
    class Meta:
        fields = ('order_id', 'product_id','quantity','total_price')
#Init shema
product_shema = ProductSchema()
products_shema = ProductSchema(many=True)
uom_chema = UomSchema()
order_chema = OrderSchema(many=True)
order_detail_chemas = OderDetail(many=True)
order_detail_chema = OderDetail()
#add unit
@app.route('/uom', methods = ['POST'])
def add_uom():
    uom_name = request.json['uom_name']
    new_uom = Uom(uom_name)
    db.session.add(new_uom)
    db.session.commit()
    return uom_chema.jsonify(new_uom)

#add product
@app.route('/product', methods = ['POST'])
def add_product():
    name = request.json['name']
    description = request.json['description']
    uom_id = request.json['uom_id']
    price_per_unit = request.json['price']
    new_product = Product(name, description, uom_id, price_per_unit)
    db.session.add(new_product)
    db.session.commit()
    return product_shema.jsonify(new_product)

#add order    
@app.route('/addorder', methods = ['POST'])
def add_order():  
    customer = request.json['customer']
    total = request.json['total']
    new_order = Order_sum(customer, total)
    db.session.add(new_order)
    db.session.commit()
    return order_chema.jsonify(new_order)
#get order    
@app.route('/getorder', methods = ['GET'])
def get_order():  
    all_orders = Order_sum.query.all()
    return order_chema.jsonify(all_orders)
#add order detail
@app.route('/order_detail', methods = ['POST'])
def add_order_detail():  
    quantity = request.json['quantity']
    total_price = request.json['total_price']
    oder_id = request.json['order_id']
    product_id = request.json['product_id']
    new_order = Order_detail(oder_id, product_id, quantity, total_price)
    db.session.add(new_order)
    db.session.commit()
    return order_detail_chema.jsonify(new_order)


#get all product
@app.route('/products', methods = ['GET'])
def get_products():
    all_products = Product.query.all()
    #result = products_shema.dump(all_products)
    return products_shema.jsonify(all_products)

#get product name on order_detail
@app.route('/product_name', methods = ['GET'])
def get_product_name():
    all_products = Product.query.join(Uom).filter(Uom.uom_name == 'kg')
    return products_shema.jsonify(all_products)

#get product follow id
@app.route('/product/<id>', methods = ['GET'])
def get_product(id):
    product = Product.query.get(id)
    return product_shema.jsonify(product)

#delete product id
@app.route('/product/<id>', methods = ['DELETE'])
def delete_product(id):
    product = Product.query.get(id)
    db.session.delete(product)
    db.session.commit()
    return product_shema.jsonify(product)
#update product id
@app.route('/product/<id>', methods = ['PUT'])
def update_product(id):
    product = Product.query.get(id)
    name = request.json['name']
    description = request.json['description']
    price_per_unit = request.json['price_per_unit']
    print(product)
    if name:
        product.name = name
    if description:
        product.description = description
    if price_per_unit:
        product.price = price_per_unit
    db.session.commit()
    return product_shema.jsonify(product)

#get detail order by customer name
@app.route('/getorder_detail/<name>', methods = ['GET'])
def get_order_detail(name):
    all_orders = Product.query.join(Order_detail).join(Order_sum).filter(Order_sum.customer == name).first()
    #all_orders = Order_detail.query.all()
    return ({"Product_name": all_orders.name})
# Run Server
if __name__ == '__main__':
    app.run(debug=True)