from flask import render_template, make_response
from flask_restful import Resource


class Home(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('home.html'), 200, headers)


class Shop(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('shop.html'), 200, headers)


class Cart(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('cart.html'), 200, headers)


class Checkout(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('checkout.html'), 200, headers)


class Contact(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('contact.html'), 200, headers)


class ShopDetail(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('shop-detail.html'), 200, headers)


class Testimonial(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('testimonial.html'), 200, headers)
