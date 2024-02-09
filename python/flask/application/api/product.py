from flask import render_template, request
from flask_restful import Resource, marshal_with, fields

from application.service.product import ProductService

product_service = ProductService()

product_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'price': fields.Float,
    'quantity': fields.Integer
}


class Products(Resource):
    @marshal_with(product_fields)
    def get(self):
        products = product_service.get_products()
        return products


class Product(Resource):
    @marshal_with(product_fields)
    def get(self, product_id: int):
        product = product_service.get_product(product_id)
        return product

    @marshal_with(product_fields)
    def post(self, product_id: int):
        new_product = product_service.add_product(product_id, request)
        return new_product

    @marshal_with(product_fields)
    def delete(self, product_id: int):
        product_service.delete_product(product_id)
        pass

    @marshal_with(product_fields)
    def put(self, product_id: int):
        updated_product = product_service.update_product(product_id, request)
        return updated_product



