from flask import Flask, request, jsonify

app = Flask(__name__)

products = [
    {"id":1, "name": "BMW", "category":"Luxury Car", "price": 2500000, "instock": 200},
    {"id":2, "name": "iPhone", "category":"Mobile Phones", "price": 45000, "instock": 100},
    {"id":3, "name": "Table", "category":"Household Furniture", "price": 599, "instock": 50},
]

@app.route('/products/', methods=["GET"])
def get_products():
    return jsonify(products)

@app.route('/products/<int:id>', methods=["GET"])
def get_product(id):
    product = next(filter(lambda x: x['id'] == id, products), None)
    if product is None:
        return jsonify({"error": "Product not found"}), 404
    return jsonify(product)

@app.route('/products/', methods=["POST"])
def create_product():
    data = request.get_json()
    product_id = data["id"]
    if any(product for product in products if product['id'] == product_id):
        return jsonify({"error": "Product already exists"}), 400
    products.append(data)
    return jsonify(data), 201

@app.route('/products/<int:id>', methods=["PUT"])
def update_products(id):
    global products
    product = next(filter(lambda x: x['id'] == id, products), None)
    if product is None:
        return jsonify({"error": "Product not found"}), 404
    data = request.get_json()
    product.update(data)
    return jsonify(product), 200


@app.route('/products/<int:id>', methods=["DELETE"])
def delete_product(id):
    product = next(filter(lambda x: x['id'] == id, products), None)
    if product is None:
        return jsonify({"error": "Product not found"}), 404
    products.remove(product)
    return jsonify({"message": "Product deleted"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)



