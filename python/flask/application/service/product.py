from application.model.product import Product
from configuration.database import session


class ProductService:
    model = Product

    @classmethod
    def get_products(cls):
        return cls.model.query.all()

    @classmethod
    def get_product(cls, product_id):
        product = cls.model.query.get(product_id)
        return product

    @classmethod
    def delete_product(cls, product_id):
        product = cls.model.query.delete(product_id)

    @classmethod
    def update_product(cls, update_product_request):
        product = cls.model.query.get(update_product_request.name["id"])
        name = update_product_request.name["name"]
        price = update_product_request.name["price"]
        quantity = update_product_request.name["quantity"]

        product.name = name
        product.price = price
        product.quantity = quantity
        return product

    @classmethod
    def add_product(cls, new_product_request):
        name = new_product_request.name["name"]
        price = new_product_request.name["price"]
        quantity = new_product_request.name["quantity"]

        new_product = Product(name, price, quantity)
        saved_product = session.add(new_product)
        session.commit()
        return saved_product
