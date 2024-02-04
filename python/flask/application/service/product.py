from application.model.product import Product
from application.schema.product_schema import ProductSchema


class ProductService:
    model = Product
    model_schema = ProductSchema

    @classmethod
    def get_products(cls):
        all_products = cls.model.query.all()
        return cls.model_schema.jsonify(all_products)

    @classmethod
    def get_product(cls, product_id):
        product = cls.model.query.get(product_id)
        return cls.model_schema.jsonify(product)
