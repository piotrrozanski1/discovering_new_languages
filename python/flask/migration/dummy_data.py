from app import app, db
from application.model import product
from application.model.product import ProductCategoryEnum, ProductTypeEnum


def add_dummy_data():
    app.app_context().push()
    db.session.add(product.Product("Cauliflower", 10, 10, ProductCategoryEnum.cauliflowers, ProductTypeEnum.vegetables))
    db.session.add(product.Product("Apples ", 10, 10, ProductCategoryEnum.apples, ProductTypeEnum.fruits))
    db.session.add(product.Product("Oranges ", 10, 10, ProductCategoryEnum.oranges, ProductTypeEnum.fruits))
    db.session.commit()

