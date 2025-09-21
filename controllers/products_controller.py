from flask import jsonify, request

from db import product_records

def create_product():
    data = request.form if request.form else request.get_json()

    if not data:
        return({"error": "No input provided"}), 400

    try:
        product ={}
        product['product_id'] = int(data['product_id'])
        product['product_name'] = data['product_name']
        product['description'] = data['description']
        product['price'] = float(data['price'])
        product['active'] = bool(data['active'])
        product_records.append(product)
        return({"message": f"Product {product['product_name']} has been added."}), 200

    except (error) as e :
        return({"error": f" Invalid input: {e}"}), 400


def read_all_products():
    if not product_records:
        return jsonify({"message": "No products found"}), 404
    return jsonify(product_records), 200

def read_product_by_id(product_id):
    for product in product_records:
        if product['product_id'] == int(product_id):
            return jsonify (product), 200
    return jsonify({"message": f'Product {product["product_id"]} not found.'}), 404

    
def read_active_products():
    for product in product_records:
        if product.get("active"):
            return jsonify (product), 200
    return jsonify({"message": "No active product found."}), 404


def update_product_by_id(product_id):
    product_id = int(product_id)
    data = request.json

    for product in product_records:
        if product.get ('product_id') == product_id:
            if "product name" in data:
                product['product_name'] = data['product_name']
            if "description" in data:
                product['description'] = data['description']
            if "price" in data:
                product['price'] = data['price']
            if "active" in data:
                product['active'] = data['active']
            return jsonify({
                "message": f"Product {product_id} updated successfully.",
                "product": product
            }), 200
    return jsonify({"message": f"Product {product_id} not found."}), 404           


def delete_product_by_id(product_id):
    product_id = int(product_id)

    for index, product in enumerate(product_records):
        if product['product_id'] == product_id:
            deleted_product = product_records.pop(index)
        return jsonify({"message":"Product {product_id} has been removed."}), 200
    return jsonify({"message": f"Product {product_id} not found."}), 404