from app import app, db
from application.model import product
from application.model.product import ProductCategoryEnum, ProductTypeEnum


def add_dummy_data():
    app.app_context().push()
    db.session.add(product.Product("Cauliflower", 5, 10, ProductCategoryEnum.cauliflowers, ProductTypeEnum.vegetables))
    db.session.add(product.Product("Apples", 10, 3, ProductCategoryEnum.apples, ProductTypeEnum.fruits))
    db.session.add(product.Product("Oranges", 20, 5, ProductCategoryEnum.oranges, ProductTypeEnum.fruits))
    db.session.add(product.Product("Pumpkins", 2, 8, ProductCategoryEnum.pumpkins, ProductTypeEnum.vegetables))
    db.session.add(product.Product("Strawberries", 4.3, 6, ProductCategoryEnum.strawberries, ProductTypeEnum.fruits))
    db.session.add(product.Product("Bananas", 2.3, 12, ProductCategoryEnum.bananas, ProductTypeEnum.fruits))
    db.session.add(product.Product("Carrots", 6.4, 15, ProductCategoryEnum.carrots, ProductTypeEnum.vegetables))
    db.session.add(product.Product("Pepper", 9, 13, ProductCategoryEnum.pepper, ProductTypeEnum.vegetables))
    db.session.add(product.Product("Potatoes", 2, 12, ProductCategoryEnum.potatoes, ProductTypeEnum.vegetables))
    db.session.add(product.Product("Parsely", 12, 11, ProductCategoryEnum.parsely, ProductTypeEnum.vegetables))
    db.session.add(product.Product("Tomatoes", 20, 20, ProductCategoryEnum.tomatoes, ProductTypeEnum.vegetables))
    db.session.commit()
