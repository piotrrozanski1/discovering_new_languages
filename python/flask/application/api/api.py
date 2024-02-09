from application.api.product import Product, Products
from application.api.view import *
from flask_restful import Api


class ApiConfig(object):
    def __init__(self, app):
        api = Api(app)
        api.add_resource(Product, "/products/{<int:product_id>}")
        api.add_resource(Products, "/products")
        api.add_resource(Home, "/")
        api.add_resource(ShopDetail, "/shop-detail")
        api.add_resource(Testimonial, "/testimonial")
        api.add_resource(Shop, "/shop")
        api.add_resource(Cart, "/cart")
        api.add_resource(Checkout, "/checkout")
        api.add_resource(Contact, "/contact")

