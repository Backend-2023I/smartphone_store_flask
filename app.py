from flask import Flask, request, jsonify
from db import SmartphoneDB

app = Flask(__name__)
db = SmartphoneDB('/home/backend2023I/smartphone_store_flask/db.json')

## view all smartphone
@app.route('/smartphones', methods=['GET'])
def get_all_smartphones():
    """Returns all smartphones in the database"""
    brands = list(db.brands())
    data = {
        "products": db.all_smartphone(brands)
    }
    return data


# view all brands
@app.route('/smartphones/brands', methods=['GET'])
def get_all_brands():
    """Returns all brands in the database"""
    data = {
        "brands": list(db.brands())
    }
    return data


# view all smartphones by brand
@app.route('/smartphones/<brand>', methods=['GET'])
def get_smartphone_by_brand(brand):
    """Returns all products by brand"""
    data = {
        brand: db.get_smartphone_by_brand(brand)
    }
    return data


# view smartphone by name
@app.route('/smartphones/name/<brand>/<name>', methods=['GET'])
def get_smartphone_by_name(brand, name):
    """Returns a product by name"""

    data = {
        name: db.get_smartphone_by_name(brand, name)
    }
    return data


# view smartphone by price
@app.route('/smartphones/price/<price>', methods=['GET'])
def get_smartphone_by_price(price):
    """Returns a product by price"""
    pass


# view add smartphone
@app.route('/smartphone/add', methods=['POST'])
def add_smartphone():
    """Adds a product to the database"""
    pass


# view delete smartphone
@app.route('/smartphone/delete/<doc_id>', methods=['DELETE'])
def delete_smartphone(doc_id):
    """Deletes a product from the database"""
    pass


if __name__ == '__main__':
    app.run(debug=True)