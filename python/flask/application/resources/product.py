from app import app
from flask import render_template


@app.route("/products", methods=['GET'])
def get_products():
    return render_template("home.html")


@app.route("/products/{<int:product_id>}", methods=['GET'])
def get_product(product_id):
    return render_template("home.html")


@app.route("/products/{<int:product_id>}}", methods=['POST'])
def add_product(product_id):
    return render_template("home.html")


@app.route("/products/{<int:product_id>}}", methods=['DELETE'])
def delete_product(product_id):
    return render_template("home.html")


@app.route("/products/{<int:product_id>}}", methods=['PATCH'])
def update_product(product_id):
    return render_template("home.html")
