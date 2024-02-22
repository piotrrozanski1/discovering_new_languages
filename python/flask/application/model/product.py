import enum
from sqlalchemy import Enum

from configuration.database import db


class ProductCategoryEnum(enum.Enum):
    apples = 1
    oranges = 2
    strawberries = 3
    bananas = 4
    pumpkins = 5
    cauliflowers = 6
    parsely = 7
    pepper = 8
    potatoes = 9
    carrots = 10
    tomatoes = 11


class ProductTypeEnum(enum.Enum):
    vegetables = 1
    fruits = 2
    bread = 3
    meat = 4


class Product(db.Model):
    __tablename__ = "product"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    price = db.Column(db.Float)
    quantity = db.Column(db.Integer)
    category = db.Column('category', Enum(ProductCategoryEnum))
    type = db.Column('type', Enum(ProductTypeEnum))

    def __init__(self, name, price, quantity, category, type):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category
        self.type = type
